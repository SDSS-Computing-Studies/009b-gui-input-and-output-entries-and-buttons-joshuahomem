"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
#!python3

import tkinter as tk 
from tkinter import *

win=tk.Tk()

win.title("madlib")
win.geometry("1800x1800")

output1 = StringVar()
output2 = StringVar()
output3 = StringVar()
output4 = StringVar()
output5 = StringVar()
output6 = StringVar()
output7 = StringVar()
output8 = StringVar()
output9 = StringVar()




def mad():
    a1=e1.get()
    a2=e2.get()
    a3=e3.get()
    a4=e4.get()
    a5=e5.get()
    a6=e6.get()
    a7=e7.get()
    a8=e8.get()
    a9=e9.get()

    z1.delete(0,END)
    z2.delete(0,END)
    z3.delete(0,END)
    z4.delete(0,END)
    z5.delete(0,END)
    z6.delete(0,END)
    z7.delete(0,END)
    z8.delete(0,END)
    z9.delete(0,END)


    z1.insert(0,a1)
    z2.insert(0,a2)
    z3.insert(0,a3)
    z4.insert(0,a4)
    z5.insert(0,a5)
    z6.insert(0,a6)
    z7.insert(0,a7)
    z8.insert(0,a8)
    z9.insert(0,a9)


b1=Button(win,text="Click this to update",command=mad)

l1=tk.Label(win,text="is having a" )
l2=tk.Label(win,text="party :D!!!!!")
l3=tk.Label(win,text="its going to be at")
l4=tk.Label(win,text="on")
l5=tk.Label(win,text="please make sure to show up at ")
l6=tk.Label(win,text="or else you will be required to")
l7=tk.Label(win,text="a")
l8=tk.Label(win,text="with your")
l9=tk.Label(win,text="rsvp@")

z1=Entry(win, textvariable=output1)
z2=Entry(win, textvariable=output2)
z3=Entry(win, textvariable=output3)
z4=Entry(win, textvariable=output4)
z5=Entry(win, textvariable=output5)
z6=Entry(win, textvariable=output6)
z7=Entry(win, textvariable=output7)
z8=Entry(win, textvariable=output8)
z9=Entry(win, textvariable=output9)

la=Label(win,text="Enter in your name")
lb=Label(win,text="Theme")
lc=Label(win,text="place")
ld=Label(win,text="Day of the week")
le=Label(win,text="Time")
lf=Label(win,text="verb")
lg=Label(win,text="Animal")
lh=Label(win,text="Body Part")
li=Label(win,text="Contact Info")

e1=Entry(win, text="")
e2=Entry(win, text="")
e3=Entry(win, text="")
e4=Entry(win, text="")
e5=Entry(win, text="")
e6=Entry(win, text="")
e7=Entry(win, text="")
e8=Entry(win, text="") 
e9=Entry(win, text="") 

la.grid(row=1,column=1)
e1.grid(row=1,column=2)
lb.grid(row=2,column=1)
e2.grid(row=2,column=2)
lc.grid(row=3,column=1)
e3.grid(row=3,column=2)
ld.grid(row=4,column=1)
e4.grid(row=4,column=2)
le.grid(row=5,column=1)
e5.grid(row=5,column=2)
lf.grid(row=6,column=1)
e6.grid(row=6,column=2)
lg.grid(row=7,column=1)
e7.grid(row=7,column=2)
lh.grid(row=8,column=1)
e8.grid(row=8,column=2)
li.grid(row=9,column=1)
e9.grid(row=9,column=2)

l1.grid(row=1,column=8)
l2.grid(row=3,column=8)
l3.grid(row=5,column=8)
l4.grid(row=7,column=8)
l5.grid(row=9,column=8)
l6.grid(row=11,column=8)
l7.grid(row=13,column=8)
l8.grid(row=15,column=8)
l9.grid(row=17,column=8)

z1.grid(row=2,column=8)
z2.grid(row=4,column=8)
z3.grid(row=6,column=8)
z4.grid(row=8,column=8)
z5.grid(row=10,column=8)
z6.grid(row=12,column=8)
z7.grid(row=14,column=8)
z8.grid(row=16,column=8)
z9.grid(row=18,column=8)














b1.grid(row=10,column=1)
win.mainloop()