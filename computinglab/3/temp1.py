from cryptography.hazmat.primitives.asymmetric import rsa, padding

private = rsa.generate_private_key(public_exponent=3, key_size=1024)
public = private.public_key()

msg = input("enter msg: ").encode()
enc = public.encrypt(msg,padding.PKCS1v15())
dec = private.decrypt(enc,padding.PKCS1v15())

print("Encrypted:", enc[:25], "...")
print("Decrypted:", dec)
