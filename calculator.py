from tkinter import *
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        tot=str(eval(expression))
        equation.set(tot)
        expression=""
    except:
        equation.set("error")
        expression=""
def clear():
    global expression
    expression=""
    equation.set("")
if __name__=="__main__":
 gui= Tk()
gui.configure(background="black")
gui.title("CALCULATOR")
gui.geometry("300x190")
equation=StringVar()
expression_field=Entry(gui,textvariable=equation, font=('Arial', 25, 'bold'), width=12, )
expression_field.grid(rowspan=5,columnspan=4,ipadx=5,ipady=5) 
button1 = Button(gui, text=' 1 ', fg='black', bg='orange',command=lambda: press(1), height=1, width=7,)
button1.grid(row=10, column=1)
button2 = Button(gui, text=' 2 ', fg='black', bg='orange',command=lambda: press(2), height=1, width=7,)
button2.grid(row=10, column=2)
button3 = Button(gui, text=' 3 ', fg='black', bg='orange',command=lambda: press(3), height=1, width=7,)
button3.grid(row=10, column=3)
button4 = Button(gui, text=' 4 ', fg='black', bg='orange',command=lambda: press(4), height=1, width=7,)
button4.grid(row=20,column=1)
button5 = Button(gui, text=' 5 ', fg='black', bg='orange',command=lambda: press(5), height=1, width=7,)
button5.grid(row=20,column=2)
button6 = Button(gui, text=' 6 ', fg='black', bg='orange',command=lambda: press(6), height=1, width=7,)
button6.grid(row=20,column=3)
button7 = Button(gui, text='7', fg='black', bg='orange',command=lambda: press(7), height=1, width=7,)
button7.grid(row=30,column=1)
button8 = Button(gui, text=' 8 ', fg='black', bg='orange',command=lambda: press(8), height=1, width=7,)
button8.grid(row=30,column=2)
button9= Button(gui, text=' 9 ', fg='black', bg='orange',command=lambda: press(9), height=1, width=7,)
button9.grid(row=30,column=3)
button0 = Button(gui, text=' 0 ', fg='black', bg='orange',command=lambda: press(0), height=1, width=7,)
button0.grid(row=40,column=2)
plus = Button(gui, text=' + ', fg='black', bg='purple',command=lambda: press("+"), height=1, width=7,)
plus.grid(row=10,column=4)
minus= Button(gui, text=' -', fg='black', bg='purple',command=lambda: press("-"), height=1, width=7,)
minus.grid(row=20,column=4)
multipy= Button(gui, text='*', fg='black', bg='purple',command=lambda: press("*"), height=1, width=7,)
multipy.grid(row=30,column=4)
divide= Button(gui, text=' /', fg='black', bg='purple',command=lambda: press("/"), height=1, width=7,)
divide.grid(row=40,column=4)
braket= Button(gui, text=' (', fg='black', bg='orange',command=lambda: press("("), height=1, width=7,)
braket.grid(row=40,column=1)
braket2= Button(gui, text=' )', fg='black', bg='orange',command=lambda: press(")"), height=1, width=7,)
braket2.grid(row=40,column=3)
modulus= Button(gui, text=' %', fg='black', bg='red',command=lambda: press("%"), height=1, width=7,)
modulus.grid(row=50,column=3)
decimal= Button(gui, text=' .', fg='black', bg='yellow',command=lambda: press("."), height=1, width=7,)
decimal.grid(row=50,column=2)
clear = Button(gui, text='Clear', fg='black', bg='light green',command=clear, height=1, width=7)
clear.grid(row=50, column=1)
equal = Button(gui, text=' = ', fg='black', bg='blue',command=equalpress, height=1, width=7)
equal.grid(row=50, column=4)
gui.mainloop()