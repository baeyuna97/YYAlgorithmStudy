import hashlib

data = input()
en_data = data.encode()
result = hashlib.sha256(en_data).hexdigest()
print(result)