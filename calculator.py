import tkinter as tk
from tkinter import filedialog,Text
import os

root = tk.Tk()
root.title("Tan Cal")
e = tk.Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

def click(nubmer):
    inputted = e.get()
    e.delete(0,'end')
    e.insert(0,str(inputted)+str(nubmer))
def add():
    global method
    method = 'add'
    global first_num
    first_num = e.get()
    e.delete(0,'end')
def mins():
    global method
    method = 'mins'
    global first_num
    first_num = e.get()
    e.delete(0,'end')
def muitiply():
    global method
    method = 'muitiply'
    global first_num
    first_num = e.get()
    e.delete(0,'end')
def divide():
    global method
    method = 'divide'
    global first_num
    first_num = e.get()
    e.delete(0,'end')
def clear():
    e.delete(0,'end')
def equal():
    num = e.get()
    e.delete(0,'end')
    if 'mins'== method:
        e.insert(0,str(int(first_num) - int(num)))
    if 'add'== method:
        e.insert(0,str(int(first_num) + int(num)))
    if 'muitiply' == method:
        e.insert(0,str(int(first_num) * int(num)))
    if 'divide' == method:
        e.insert(0,str(int(first_num) / int(num)))
        
        

b1 = tk.Button(root,text="1",fg = 'white',bg = 'green',padx=30,pady=20,command=lambda:click(1))
b2 = tk.Button(root,text='2',fg = 'white',bg = 'blue',padx=30,pady=20,command=lambda:click(2))
b3 = tk.Button(root,text='3',fg = 'white',bg = 'yellow',padx=30,pady=20,command=lambda:click(3))
b4 = tk.Button(root,text='4',fg = 'white',bg = 'red',padx=30,pady=20,command=lambda:click(4))
b5 = tk.Button(root,text='5',fg = 'white',bg = 'purple',padx=30,pady=20,command=lambda:click(5))
b6 = tk.Button(root,text='6',fg = 'white',bg = 'pink',padx=30,pady=20,command=lambda:click(6))
b7 = tk.Button(root,text='7',fg = 'white',bg = 'orange',padx=30,pady=20,command=lambda:click(7))
b8 = tk.Button(root,text='8',fg = 'white',bg = 'black',padx=30,pady=20,command=lambda:click(8))
b9 = tk.Button(root,text='9',fg = 'white',bg = 'gray',padx=30,pady=20,command=lambda:click(9))
b0 = tk.Button(root,text='0',fg = 'white',bg = 'brown',padx=30,pady=20,command=lambda:click(0))
badd = tk.Button(root,text='+',padx=30,pady=20,command=add)
bmin = tk.Button(root,text='-',padx=30,pady=20,command=mins)
bmuit = tk.Button(root,text="*",padx=30,pady=20,command=muitiply)
bdivi = tk.Button(root,text="/",padx=30,pady=20,command=divide)
bclear = tk.Button(root,text="Clear",padx=57,pady=20,command=clear)
bequal = tk.Button(root,text='=',padx=30,pady=20,command=lambda: equal())


bclear.grid(row=4,column=1,columnspan=2)
bequal.grid(row=5,column=3,columnspan=2)
bmuit.grid(row=3,column=3)
bdivi.grid(row=4,column=3)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
badd.grid(row=1,column=3)
bmin.grid(row=2,column=3)


root.mainloop()
