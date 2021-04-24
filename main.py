import createSignature
import verifysignature

print('1.Sign a PDF file\n2.Verify a PDF file')

option = int(input())

if option == 1:
    print("\nEnter name of the PDF file that you want to Sign")
    file_name = input()
    signature, pubkey = createSignature.create_signature(file_name)
    with open('signature.txt','wb') as w:
        w.write(signature)
    with open('publickey.key','wb') as key_file:
        key_file.write(pubkey.save_pkcs1('PEM'))
    

if option == 2:
    print('Enter the name of the pdf file')
    file_name = input()
    print('Enter the name of the signature file')
    signature_file = input()
    print('Enter the name of the Public key file')
    public_key = input()
    try:
        verifysignature.verify_signature(file_name,signature_file,public_key)
    except:
        print('Signature verification failed')
