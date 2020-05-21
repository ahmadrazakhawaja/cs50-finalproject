from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib
import random
import getpass
import struct
class encryption:
    def password(self,ps):
       # p = getpass.getpass()
        h= hashlib.sha256(ps.encode())
        return h.digest()
    def encrypt(self,filepath,filepath2,ps):
        chunk=16
        size=os.path.getsize(filepath)
        f= open(filepath,"r")
        fs=open(filepath2,"wb")
        fs.write(struct.pack('<Q', size))
        iv = os.urandom(16)                                    # iv=''.join([chr(random.randint(0,0xFF)) for i in range(16)])
        fs.write(iv)
        en=AES.new(ps,AES.MODE_CBC,iv)
        while True:
            data=f.read(16)
            n=len(data)
            if n==0:   #data +=bytes(0) * (16 - n % 16)
                break
            elif n%16!=0:
                #    for i in range(16 - (n % 16)):
                data +=' '*(16-(n%16))
            print(n)
            out=en.encrypt(data)
            fs.write(out)
        f.close()
        fs.close()

    def decrypt(self,key,filepath,filepath2):
        fs=open(filepath,"rb")
        orisize=struct.unpack('<Q',fs.read(struct.calcsize('Q')))[0]
        iv=fs.read(16)
        h= hashlib.sha256(key.encode())
        l=h.digest()
        aes = AES.new(l, AES.MODE_CBC, iv)
        f=open(filepath2,"wb")
        sk=0
        while(True):
            data=fs.read(16)
            sk+=16
            n=len(data)
            if n==0:
                break
            an=aes.decrypt(data)
            f.write(an)
        c=os.path.getsize(filepath2)
        if c>orisize:
            v=c-orisize
            f.seek(0, os.SEEK_END)
            f.truncate(v)
        f.close()
        fs.close()








if __name__ == "__main__":
    e1=encryption()
    #e1.encrypt("/Users/ahmadrazakhawaja/Downloads/index.php","/Users/ahmadrazakhawaja/Downloads/ko.php",e1.password("hello"))
    e1.decrypt("hello",2973,"/Users/ahmadrazakhawaja/Downloads/ko.php","/Users/ahmadrazakhawaja/Downloads/has.php")





