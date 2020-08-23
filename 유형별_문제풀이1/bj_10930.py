import hashlib

def de():
    string = str(input())
    encoded_string = string.encode()
    hexdigest = hashlib.sha256(encoded_string).hexdigest()
    print(hexdigest)
    
de()    