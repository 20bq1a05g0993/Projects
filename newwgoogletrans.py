from tkinter import *
import os
os.system("pip install googletrans==3.1.0a0")
import googletrans
d=googletrans.LANGUAGES
lst=list(d.keys())
lst1=list(d.values())
from googletrans import Translator
t=Translator()
root=Tk()
root.title('Translator')
Label(root,text="enter text").grid(row=0,column=0)
a=StringVar()
Entry(root,textvariable=a).grid(row=0,column=1)
Label(root,text="to Language:").grid(row=1,column=0)
clicked=StringVar()
OptionMenu(root,clicked,*lst1).grid(row=1,column=1)
clicked.set('english')
Label(root,text="translated text:").grid(row=2,column=0)
b=StringVar()
Entry(root,textvariable=b,state=DISABLED).grid(row=2,column=1)
Label(root,text="pronunciation:").grid(row=3,column=0)
c=StringVar()
Entry(root,textvariable=c,state=DISABLED).grid(row=3,column=1)
def buttonclicked():
    i=lst1.index(clicked.get())
    out=t.translate(a.get(),dest=lst[i])
    b.set(out.text)
    c.set(out.pronunciation)
Button(root,text="translate",command=buttonclicked).grid(row=4,column=0)
