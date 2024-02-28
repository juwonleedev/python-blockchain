import datetime
import hashlib

block_body =  { "transaction1": {
                            '판매자' : '파이썬',
                            '구매자' : '김민수',
                            '개수' : '3개',
                            'timestamp' : 1652247422892844,
                            'smart_contract' : {}
                               },
                "transaction2": {
                            '판매자' : '파이썬',
                            '구매자' : '이영호',
                            '개수' : '3개',
                            'timestamp' : 165224743233231,
                            'smart_contract' : {
                                '함수명': 'DEFI',
                                '함수 설명': '어쩌구 디파이 프로젝트',
                                'input 변수': ['사용자 지갑 주소', '요청 구분(예금 or 대출)', '금액'],
                                '함수내용': '만약 ~하면 사용자에게 이자를~'
                                    }
                               }
}

block_header =  {  'Block_height' : 0,
                   'Block_created_at' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                   'Miner' : "0xea674fdde714fd979de3edf0f56aa9716b898ec8",
                   'Block_Reward' : 2.132,
                   'Difficulty' : 12382889997310022,
                   'Nonce'  : '0x7ccf42b8e05d031f',
                   'Block_size' : '178556 bytes',
                   'Parent_hash' : '0xe1f3d0e83542e20735d453006cc6d8975920e7aec951c3b974eade52901e97e7',
                   'Body_hash' : hashlib.sha256(str(block_body).encode()).hexdigest()
                }

body_hash = hashlib.sha256(str(block_body).encode()).hexdigest()

block1 =  { 'header' : block_header,
            'transaction' : block_body
           }
block1