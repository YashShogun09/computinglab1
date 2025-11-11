from cryptography.fernet import Fernet

with open("shared_.key","rb") as keyf :
    key = keyf.read()
    

fernet =Fernet(key)

msg = input("enter msg: ").encode()


emsg = fernet.encrypt(msg)

with open("emsg.txt","wb") as emsgf :
    emsgf.write(emsg)