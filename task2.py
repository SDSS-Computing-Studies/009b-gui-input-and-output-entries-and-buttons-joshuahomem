"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
#!python3
import math
import tkinter as tk 
from tkinter import *

win=tk.Tk()

win.title("factoring trinomials")
win.geometry("800x800")

out=StringVar

def trinomial():
    num1=e1.get()
    num2=e2.get()
    num2=int(num2)
    num1=int(num1)
    x=(-1*num1)+ (math.sqrt((num1**2)-(4*1*num2)))
    x1=x/2
    ans1=x1-x1-x1
    y=(-1*num1)- (math.sqrt((num1**2)-(4*1*num2)))
    x2=y/2
    ans2=x2-x2-x2
    mlist=[]
    mlist.append(ans1)
    mlist.append(ans2)
    
    print(mlist)
    out1.delete(0,END)
    out1.insert(0,mlist)

lin=Label(win,text="This program is to factor the trinomial in the format ax^2+bx+c=0. Enter in your values for B and C and the prgram will factor.")
l1=Label(win,text="a=1")
l2=Label(win,text="Enter in value B here: ")
l3=Label(win,text="Enter in value C here: ")


b1=Button(win,text="Push this to get equations",command=trinomial)

e1= Entry(win,text="",width=50)
e2= Entry(win,text="",width=50)

out1=Entry(win,textvar=out)
lin.grid(row=1,column=1)
l1.grid(row=2,column=1)
e1.grid(row=2,column=2)
l2.grid(row=2,column=3)
e2.grid(row=2,column=4)
l3.grid(row=2,column=5)
b1.grid(row=4,column=2)
out1.grid(row=4,column=3)
win.mainloop()