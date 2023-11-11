import datetime
import hashlib

block_body = {
    'transaction1': {
        'seller': 'Jone Doe',
        'buyer': 'Irene Lee',
        'amount': '3',
        'time': '1990-1-1-00:00:00',
        'fee': '0.001'
    },
    'transaction2': {
        'seller': 'Wonbin Park',
        'buyer': 'Chanyeong Lee',
        'amount': '5',
        'time': '1990-1-3-13:00:00',
        'fee': '0.003'
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