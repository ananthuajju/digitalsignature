import hash
import rsa

def verify_signature(file,signature,public_key):
    hashed = hash.hash_file(file).encode()
    sign = file_open(signature)
    print(sign)
    pubkey = rsa.PublicKey.load_pkcs1(file_open(public_key))
    print(pubkey)
    verification = rsa.verify(hashed,sign,pubkey)

def file_open(file):
    file_data = open(file,'rb').read()
    return file_data
