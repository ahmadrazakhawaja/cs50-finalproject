from Crypto.PublicKey import RSA
import random
import math
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from Crypto.Util import number
from base64 import b64encode, b64decode
import sys

class rsa:

    def checkprime(self, num):
        for i in range(2, math.sqrt(num)):
            if num % i == 0:
                return false
        return true

    def checkprime2(selfself, size, num):
        siev = [true] * size
        siev[0] = false
        siev[1] = false

        for i in range(2, math.sqrt(num) + 1):
            pointer = i * 2
            while pointer < size:
                siev[pointer] = false
                pointer += i
        primes = []
        for i in range(size):
            if siev[i] == true:
                primes.append(i)
        return primes

    def rabinMiller(self,n, k):
        if n < 6:
            return [False, False, True, True, False, True][n]
        elif n & 1 == 0:
            return False
        else:
            s, d = 0, n - 1
            while d & 1 == 0:
                s, d = s + 1, d >> 1

            for a in random.sample(range(2, min(n - 2, sys.maxsize)), min(n - 4, k)):
                x = pow(a, d, n)
                if x != 1 and x + 1 != n:
                    for r in range(1, s):
                        x = pow(x, 2, n)
                        if x == 1:
                            return False
                        elif x == n - 1:
                            a = 0
                            break
                    if a:
                        return False
            return True


    def generateprime(self):
        keysize =10
        while True:
            num = random.randrange(pow(2,(keysize - 1)), pow(2, (keysize)))
            print(num)
            if  self.rabinMiller(self,num,k=7)==True:
                break
        return num

    def keypair(self):
        while True:
            num1=self.generateprime(self)
            num2=self.generateprime(self)
            if num1!=num2:
                break
        n=num1*num2
        phi=(num1-1)*(num2-1)
        f=0
        while True:
             i=random.randint(2,phi-1)
             if self.gcd(self,i,phi)==1:
                 f=i
                 break
        h=self.multiplicative_inverse(self,f,phi)
        privatekey=h,n
        publickey=f,n
        return publickey,privatekey


    def encoding(self,message):
        pk,a=self.keypair(self)
        f,n=pk
        cipher = [(pow(ord(char),f)) % n for char in message]
        return cipher,a,pk

    def decode(self,message,d):
        h,n=d
        plain = [chr((pow(int(char),int(h))) % int(n)) for char in message]
        return ''.join(plain)

    def gcd(self,num,num2):
        if num2==0:
            return num
        return self.gcd(self,num2, num % num2)

    def multiplicative_inverse(self,e, phi):
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        temp_phi = phi

        while e > 0:
            temp1 = temp_phi//e
            temp2 = temp_phi - temp1 * e
            temp_phi = e
            e = temp2

            x = x2- temp1* x1
            y = d - temp1 * y1

            x2 = x1
            x1 = x
            d = y1
            y1 = y

        if temp_phi == 1:
            return d + phi


if __name__ == '__main__':
    j=rsa
    m,d,_=j.encoding(j,"disco")
    print(j.decode(j,m,d))







