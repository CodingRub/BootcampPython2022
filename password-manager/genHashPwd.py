import hashlib

def gen_hash(pwd: str):
    plaintext = pwd.encode()
    d = hashlib.sha512(plaintext)
    hash = d.hexdigest()
    return hash
