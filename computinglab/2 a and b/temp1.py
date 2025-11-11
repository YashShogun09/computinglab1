from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("shared_.key","wb") as keyf:
    keyf.write(key)