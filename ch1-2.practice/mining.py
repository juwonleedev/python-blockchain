import hashlib
import random
import string

# problem
PROBLEM_WORD = "a" # the answer
PROBLEM_DIFFICULTY = 1 # difficulty. higher number, higher difficulty
## in this case, hash value starting with 'a' works

## mining
start_nonce = random.choice(string.ascii_letters)

i = 0

# while true : infinite loop
while True:
    # start_nonce: random start point. We'll add one by one at this
    nonce = start_nonce + str(i)
    nonce_result = hashlib.sha256((nonce).encode()).hexdigest()
    print(i,nonce, nonce_result)
    # 해시 결과값 앞에 n (난이도, PROBLEM_DIFFICULTY = 1)자리 숫자가 동일 (PROBLEM_WORLD=a)
    if nonce_result[0: PROBLEM_DIFFICULTY] == PROBLEM_WORD * PROBLEM_DIFFICULTY: 
        nonce = nonce_result
        break
    i += 1
