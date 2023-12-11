block1 = {
    'INDEX': 0,
    '판매자': '파이썬',
    '구매자': '이찬영',
    '개수': '3개',
    '시간': '1990-01-01 00:00:00',
    'previous_block': None # previous_block이 chain 역할을 한다
}

# block architecture
import datetime
import hashlib

block_body = {
    "거래내역1": {
        '판매자': '파이썬',
        '구매자' : '김민수',
        '개수': '3개',
        '거래시간' : '1990년 1월 1일 00시 00분 00초',
        '거래 수수료': '0.001개'
    },
    "거래내역2": {
        '판매자': '김민수',
        '구매자' : '김영수',
        '개수': '3개',
        '거래시간' : '1990년 1월 2일 01시 02분 03초',
        '거래 수수료': '0.001개'
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