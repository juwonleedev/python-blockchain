
import hashlib
import json

## 블록 해시 함수
def hash (block): 
    # Hashed a Block
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

## 거래 내역 저장 함수
def new_transaction(self, sender, recipient, amount):
    # Adds a new transaction to the list of transaction 
    self.current_transaction.append(
        {
            'sender': sender, # 송신자
            'recipient': recipient, # 수신자 
            'amount': amount, # 금액
            'timestamp': time()
        }
    )
    return self.last_block['index'] + 1

# 채굴 함수
def mine ():
    last_block = blockchain.last_block
    last_proof = last_block['proof']

    proof = blockchain.pow(last_proof) ## 여기가 진정한 채굴 단계

    blockchain.new_transaction(
        sender = mine_owner, #채굴 시 생성되는 transaction (0 = 운영자)
        recipient = node_identifier, # 지갑 주소처럼 사용
        amount = mine_profit # coinbase transaction 코인 1개를 전송
    )

    ## 등록된 노드들을 함께 업데이트
    for node in blockchain.nodes:
        headers = { 'Content-Type' : 'application/json ; charset = utf-8'}
        data = {
            "sender" : mine_owner,
            "recepient": node_identifier,
            "amount"  : mine_profit
        }
        requests.post("https://" + node + "/transactions/new", headers=headers, data=json.dumps(data))

        # Forge the new Block by adding it to the chain                                                                      
        # 전 블록에 대한 hash를 떠 놓고
        previous_hash = blockchain.hash(last_block)
        # 검증하는 걸 넣어서 블록을 새로 생성
        print("MINING STARTED")
        block = blockchain.new_block(proof, previous_hash)
        print("MINING FINISHED")

        ## 채굴 성공 후 동료 노드들에게 새로운 블록 정보를 업데이트
        ## 그렇게 검증도 받아야 하고
        ############
        for node in blockchain.nodes:
            headers = {'Content-Type' : 'application/json; charset=utf-8'}
            data = {
                "miner_node": 'http://' + my_ip + ":" + my_port,
            }

            a = requests.get("https://" + node + "/nodes/resolve", headers=headers, data = json.dumps(data))

            # print (a.text)
            
            # 이상이 없으면 정상 배출
            if "ERROR" not in a.text :
                print ("다른 노드가 내 블록 검증, 결과 정상!")
                # block이 제대로 mine 되었다는 정보를 json 형태로 띄워줌
                response = {
                    'message' : 'new block found',
                    'index' : block['index'],
                    'transactions': block['transactions'],
                    'proof' : block['proof'],
                    'previous_hash' : block['previous_hash']
                }

            # 이상 발생 시
            else:
                1==1
                print ("다른 노드가 내 블록 검증, 에러 발생!!!!")
                # 문제가 있음 전파
                return jsonify(response), 200