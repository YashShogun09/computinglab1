from cryptography.fernet import Fernet

with open("shared_.key","rb") as keyf :
    key = keyf.read()
    

fernet =Fernet(key)

with open("emsg.txt","rb") as emsgf :
    msg = emsgf.read()


dmsg = fernet.decrypt(msg)

with open("dmsg.txt","wb") as dmsgf :
    dmsgf.write(dmsg)