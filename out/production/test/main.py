from tkinter import *
import tkinter as tk
import tkinter
import aes
import rsa
ae=aes.encryption
rs=rsa.rsa

               #/Users/ahmadrazakhawaja/Downloads/project test/test.txt
def main():
    top = tkinter.Tk()
    top.title("choose technique")
    top.geometry("400x500")
    top.configure(background="powder blue")
    but1=Button(top,text='RSA',width=10,height=5,command=rsa1)
    but2=Button(top,text='AES',width=10,height=5, command=top1 )
    lab1=Label(text="Choose Encryption Technique")
    lab1.pack()
    but1.pack()
    but2.pack()
    top.mainloop()

def top1():
    tp=tk.Toplevel()
    tp.title("encrypt or decrypt")
    tp.geometry("400x500")
   # widget = Entry(tp, show="*", width=15)
    but3=Button(tp,text="encryption",width=10,height=5,command=top2)
    but4=Button(tp,text="decryption",width=10,height=5,command=top3)
    but3.pack()
    but4.pack()
    tp.mainloop()

def top2():
    ts=tk.Toplevel()
    ts.title("encryption")
    ts.geometry("400x500")
    lab3=Label(ts,text="filepath:")
    lab4=Label(ts,text="password:")
    widget = Entry(ts, show="*", width=15)
    lab5=Label(ts,text="output filepath")
    but4=Button(ts,text="next",width=10,height=5,command=lambda :aes1(widget.get(),text.get(),text2.get()))
    text=Entry(ts)
    text2=Entry(ts)
    lab3.pack()
    text.pack()
    lab4.pack()
    widget.pack()
    lab5.pack()
    text2.pack()
    but4.pack()
    ts.mainloop()


def aes1(w,t1,t2):
    ae.encrypt(ae,t1,t2,ae.password(ae,w))
    success()

def top3():
    tm=tk.Toplevel()
    tm.title("decryption")
    tm.geometry("400x500")
    lab3=Label(tm,text="filepath:")
    lab4=Label(tm,text="password:")
    widget = Entry(tm, show="*", width=15)
    lab5=Label(tm,text="output filepath")
    but4=Button(tm,text="next",width=10,height=5,command=lambda :aes2(widget.get(),text.get(),text2.get()))
    text=Entry(tm)
    text2=Entry(tm)
    lab3.pack()
    text.pack()
    lab4.pack()
    widget.pack()
    lab5.pack()
    text2.pack()
    but4.pack()
    tm.mainloop()

def aes2(w,t,t2):
    ae.decrypt(ae,w,t,t2)
    success()

def rsa1():
    tl=tk.Toplevel()
    tl.title("encrypt or decrypt")
    tl.geometry("400x500")
    # widget = Entry(tp, show="*", width=15)
    but3=Button(tl,text="encryption",width=10,height=5,command=rsa2)
    but4=Button(tl,text="decryption",width=10,height=5,command=rsa4)
    but3.pack()
    but4.pack()
    tl.mainloop()

def rsa2():
    tj=tk.Toplevel()
    tj.title("encryption")
    tj.geometry("400x500")
    text9=Entry(tj)
    lab10=Label(tj,text="enter plaintext")
    cipher,privatekey,publickey=rs.encoding(rs,text9.get())
    but=Button(tj,text="next",width=10,height=5,command=lambda :rsan(text9.get()))
    lab10.pack()
    text9.pack()
    but.pack()
    tj.mainloop()

def rsa3(cipher,privatekey,publickey):
    tf=tk.Toplevel()
    tf.title("keys")
    tf.geometry("400x500")
    f,e=publickey
    h,e=privatekey
    lab3=Label(tf,text="publickey:"+"  "+"e:"+str(f)+"  "+"n:"+str(e))
    lab4=Label(tf,text="privatekey:"+"  "+"d:"+str(h)+"  "+"n:"+str(e))
    lab5=Label(tf,text="ciphertext:"+str(cipher))
    lab3.pack()
    lab4.pack()
    lab5.pack()
    tf.mainloop()

def rsa4():
    tg=tk.Toplevel()
    tg.title("decryption")
    tg.geometry("400x500")
    text=Entry(tg)
    lab3=Label(tg,text="enter ciphertext")
    lab4=Label(tg,text="enter d")
    lab5=Label(tg,text="enter n")
    text1=Entry(tg)
    text2=Entry(tg)
    but4=Button(tg,text="next",width=10,height=5,command=lambda :rsam(text.get(),text1.get(),text2.get()))
    lab3.pack()
    text.pack()
    lab4.pack()
    text1.pack()
    lab5.pack()
    text2.pack()
    but4.pack()
    tg.mainloop()

def rsa5(message):
    ta=tk.Toplevel()
    ta.title("original text")
    ta.geometry("400x500")
    lab1=Label(ta,text=message)
    lab1.pack()
    but4=Button(ta,text="finish",width=10,height=5)
    but4.pack
    ta.mainloop()

def success():
    td=tk.Toplevel()
    td.title("method successful")
    td.geometry("400x500")
    lab1=Label(td,text="Success")
    lab1.pack()
    td.mainloop()

def rsan(text):
    cipher,privatekey,publickey=rs.encoding(rs,text)
    rsa3(cipher,privatekey,publickey)

def rsam(text,d,n):
    privatekey=d,n
    tex=text.split(",")
    message=rs.decode(rs,tex,privatekey)
    rsa5(message)














if __name__ == "__main__":
    main()

