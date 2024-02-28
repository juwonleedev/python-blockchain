import datetime

# 블록체인이라는 객체 선언
class Blockchain(object):
    ## 블록체인의 기본 특징 선언
    def __init__(self):
        self.chain = [] # 블록을 연결하는 체인. 처음에는 빈 리스트
        self.current_transaction = [] # 블록 내에 기록되는 tx. 초기값은 빈 리스트
    
    # tx가 추가됨
    def new_transaction(self, sender, recipient, amount):
        # 거래 내역을 추가하기
        ## 현재의 tx 리스트에 송신자, 수신자 등의 거래 내역을 입력한다
        self.current_transaction.append(
            {
                'sender': sender, # 송신자
                'recipient': recipient, # 수신자
                'amount': amount, # 금액
                'timestamp': datetime.datetime.now().timestamp() # 시간
            }
        )
        return self.last_block['index'] + 1
    
    # 새 블록을 만드는 함수
    def new_block(self, proof, previous_hash=None):
        # 지금 블록에 이어질 새로운 블록을 만든다
        block = {
            'index': len(self.chain)+1, # 지금까지의 체인의 숫자 + 1 = 새로운 블록의 인덱스
            'timestamp': datetime.datetime.now().timestamp(), # 지금 시간
            'transactions': self.current_transaction, # 지금까지의 tx 넣기 
        }

        self.current_transaction = [] # 새로 블록이 생겼으니 tx은 다시 초기화
        self.chain.append(block) # 기존 체인에 블록을 넣어 연결! 블록체인
        return block
    
    @property
    def last_block(self):
        # 체인의 마지막 블록 가져오기
        return self.chain[-1]

# Test Code

# 블록체인 객체 선언
sample_blockchain = Blockchain()

# (1) 블록에 새로운 블록 만들기
sample_blockchain.new_block(proof = "1")
print (sample_blockchain.chain)

sample_blockchain.new_block(proof = "1")
print (sample_blockchain.chain)

# (2) 블록에 새로운 거래 내역 입력하기
sample_blockchain.new_transaction(sender = "김민수", recipient = "박철수", amount = 10)

## 블록에 새로운 블록 만들기
sample_blockchain.new_block(proof = "1")
print (sample_blockchain.chain)