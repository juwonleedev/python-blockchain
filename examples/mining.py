import random
import string 
import hashlib

# 이더리움 네트워크가 낸 문제
PROBLEM_WORD = "a" # 찾아야 하는 단어
PROBLEM_DIFFICULTY = 1 # 난이도 숫자, 숫자가 올라갈 수록 난이도가 올라감
### 위 문제의 경우 해시 값 앞 1번째 자리가 a이면 문제 해결 (채굴 완료)

## 채굴
start_nonce = random.choice(string.ascii_letters)

i=0
while True:
    nonce = start_nonce + str(i)
    nonce_result = hashlib.sha256((nonce).encode()).hexdigest()
    print(i, nonce, nonce_result)
    if nonce_result[0: PROBLEM_DIFFICULTY] == PROBLEM_WORD * PROBLEM_DIFFICULTY:
        nonce = nonce_result
        break
    i += 1