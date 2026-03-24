from tkinter import*
from math import*
import tkinter as tk

manslogs=Tk()
manslogs.title('Kalkulators')



def btnClick(number):
    current=e.get() # nolasa esošo skaitli
    e.delete(0,END) # nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) # ievieto displejā
    return 0 

def btnCommand (command):
    global number 
    global mathOp
    global num1
    global num3
    mathOp=command
    num1=(float(e.get))
    e.delete(0,END)
    return 0

def Equals():
    global num2
    num2=(float(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0















btn0=Button(manslogs, text='0',padx='40',pady='20', command=lambda:btnClick(0))
btn1=Button(manslogs, text='1',padx='40',pady='20', command=lambda:btnClick(1))
btn2=Button(manslogs, text='2',padx='40',pady='20', command=lambda:btnClick(2))
btn5=Button(manslogs, text='5',padx='40',pady='20', command=lambda:btnClick(5))
btn3=Button(manslogs, text='3',padx='40',pady='20', command=lambda:btnClick(3))
btn4=Button(manslogs, text='4',padx='40',pady='20', command=lambda:btnClick(4))
btn6=Button(manslogs, text='6',padx='40',pady='20', command=lambda:btnClick(6))
btn7=Button(manslogs, text='7',padx='40',pady='20', command=lambda:btnClick(7))
btn8=Button(manslogs, text='8',padx='40',pady='20', command=lambda:btnClick(8))
btn9=Button(manslogs, text='9',padx='40',pady='20', command=lambda:btnClick(9))
btnSum=Button(manslogs, text='+',padx='40',pady='20', command=lambda:btnCommand("+"))
btnSub=Button(manslogs, text='-',padx='40',pady='20',command=lambda:btnCommand("-"))
btnequals=Button(manslogs, text='=',padx='40',pady='20',command=lambda:Equals("="))
btnreiz=Button(manslogs, text='*',padx='40',pady='20',command=lambda:btnCommand("*"))
btndal=Button(manslogs, text='/',padx='40',pady='20',command=lambda:btnCommand("/"))
btnclear=Button(manslogs, text='C',padx='40',pady='20', fg="red", command=lambda:clear("C"))
e=Entry(manslogs, width=15, bd=20, font=("Arial Black", 20))



btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btndal.grid(row=1,column=3)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btnreiz.grid(row=2,column=3)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btnSub.grid(row=3,column=3)
btnclear.grid(row=4,column=0)
btn0.grid(row=4,column=1)
btnequals.grid(row=4,column=2)
btnSum.grid(row=4,column=3)
e.grid(row=0,column=0, columnspan=4)


































































manslogs.mainloop()