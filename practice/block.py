
# block 1
import hashlib


block1 = {
    'INDEX': 0,
    'buyer': 'irene lee',
    'seller': 'john doe',
    'time': '1990-01-02 01:02:03',
    'previous_block': None
}

# connected by the previous block

block2 = {
    'INDEX': 1,
    'buyer': 'penny',
    'seller': 'sheldon',
    'time': '1990-01-10 13:02:03',
    'previous_block': block1
}

# hash function 

block3 = {
    'INDEX': 1,
    'buyer': 'penny',
    'seller': 'sheldon',
    'time': '1990-01-10 13:02:03',
    'previous_block': hashlib.sha256(str(block2).encode()).hexdigest()
}

print(block3)