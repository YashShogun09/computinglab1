from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import os
a_private = rsa.generate_private_key(public_exponent=3,key_size=1024)
a_public = a_private.public_key()

b_private = rsa.generate_private_key(public_exponent=3,key_size=1024)
b_public = b_private.public_key()

n1 = os.urandom(8)
n2= os.urandom(8)

a_sign = a_private.sign(n1+n2, padding.PKCS1v15(), hashes.SHA256())
b_sign = b_private.sign(n2+n1, padding.PKCS1v15(), hashes.SHA256())

try:
    a_public.verify(a_sign,n1+n2, padding.PKCS1v15(), hashes.SHA256())
    b_public.verify(b_sign,n2+n1, padding.PKCS1v15(), hashes.SHA256())
    print("both parties verified")


except:
    print("verification failed")
