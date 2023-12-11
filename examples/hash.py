import hashlib 
print (hashlib.sha256(str("원본 텍스트").encode()).hexdigest())

print (hashlib.sha256(str("원본텍스트").encode()).hexdigest())
