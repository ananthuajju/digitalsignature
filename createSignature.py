import hash
import rsa

def create_signature(file):
    hashed = hash.hash_file(file).encode()
    (pubkey, privkey) = rsa.newkeys(528)
    signature = rsa.sign(hashed,privkey,'SHA-1')
    verification = rsa.verify(hashed,signature,privkey)

    return signature, pubkey

create_signature('dummy.pdf')

