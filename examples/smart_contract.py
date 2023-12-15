#  스마트 컨트렉트가 있는 블록체인의 블록 구조 

# block architecture
import datetime
import hashlib

block_body = {
    "거래내역1": {
        '판매자': '파이썬',
        '구매자' : '김민수',
        '개수': '3개',
        '거래시간' : '1990년 1월 1일 00시 00분 00초',
        '거래 수수료': '0.001개',
        'smart contract': {
            '토큰명' : 'PGB',
            '개수': '10개',
            '토큰 설명': '파공블 코인'
        } ## smart contract
    },
    "거래내역2": {
        '판매자': '김민수',
        '구매자' : '김영수',
        '개수': '3개',
        '거래시간' : '1990년 1월 2일 01시 02분 03초',
        '거래 수수료': '0.001개',
        'smart contract': {} ## smart contract
    }
}

block_header = {
    '블록의 생성 번호' : 0,
    '블록의 생성 시간': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    '블록의 채굴자' : "", # 이런식으로 정보가 들어감
}

body_hash = hashlib.sha256(str(block_body).encode()).hexdigest()

block1 = {
    'header' : block_header,
    'transaction' : block_body
}

print(block1)