# pip install cryptography
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

# Step 1: Create RSA keys for Alice and Bob
alice_private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
bob_private   = rsa.generate_private_key(public_exponent=65537, key_size=2048)
alice_public = alice_private.public_key()
bob_public   = bob_private.public_key()

# Step 2: Create random numbers (nonces)
na = os.urandom(8)   # Alice's random number
nb = os.urandom(8)   # Bob's random number

# Step 3: Each person signs both random numbers
alice_signature = alice_private.sign(
    na + nb,
    padding.PKCS1v15(),
    hashes.SHA256()
)
bob_signature = bob_private.sign(
    nb + na,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Step 4: Each person checks the other’s signature
try:
    alice_public.verify(alice_signature, na + nb, padding.PKCS1v15(), hashes.SHA256())
    bob_public.verify(bob_signature, nb + na, padding.PKCS1v15(), hashes.SHA256())
    print("✅ Both Alice and Bob are verified!")
except:
    print("❌ Verification failed!")
