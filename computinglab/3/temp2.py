from cryptography.hazmat.primitives.asymmetric import rsa,padding

private_key = rsa.generate_private_key(public_exponent=3,key_size=1024)

public_key = private_key.public_key()

msg = input("entr msg :  ").encode()

enc = public_key.encrypt(msg,padding.PKCS1v15())
dec = private_key.decrypt(enc,padding.PKCS1v15())

print(enc)
print(dec)