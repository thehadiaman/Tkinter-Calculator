from tkinter import *
import tkinter.font as font
from tkinter.messagebox import *
from logicModule import *

######################################################################
######################################################################

cal = ''


def btn(val):
    global cal
    cal += val
    tv.set(cal)


def btn_eq():
    global cal, ans
    try:
        ans = total(cal)
        tv.set(ans)
        cal = str(ans)
        cal = ans
    except SyntaxError:
        showerror('SyntaxError', 'Need true mathematical equations')
        cal = ''


def clr():
    global cal
    cal = ''
    tv.set('')


def sqr():
    global cal
    try:
        try:
            n = sqR(cal)
            tv.set(n)
            cal = str(n)
        except OverflowError:
            showerror('OverflowError', 'This much numbers cause OverflowError')
    except ValueError:
        showerror('ValueError', 'Only numbers are allowed')


def sqrt():
    global cal
    try:
        n = sqRoot(cal)
        tv.set(n)
        cal = str(n)
    except ValueError:
        showerror('ValueError', 'Only numbers are allowed')


def binary():
    global cal
    try:
        n = int(cal)
        tv.set(toBinary(n))
    except ValueError:
        showerror('ValueError', 'Only numbers are allowed')
    cal = ''


def hexa():
    global cal
    try:
        n = int(cal)
        tv.set(toHex(n))
    except ValueError:
        showerror('ValueError', 'Only numbers are allowed')
    cal = ''


def octa():
    global cal
    try:
        n = int(cal)
        tv.set(toOct(n))
    except ValueError:
        showerror('ValueError', 'Only numbers are allowed')
    cal = ''

###########################################################################################################
###########################################################################################################


app = Tk()
app.title('Calculator')

tv = StringVar()
equation = Entry(app, width=22, textvariable=tv)
equation.place(x=0, y=10)


num1 = Button(app, text='1', width=2, height=2, command=lambda: btn('1'), activebackground="black",
              activeforeground='white')
num1.grid(column=1, row=2)
num1['font'] = font.Font(size=20)

num2 = Button(app, text='2', width=2, height=2, command=lambda: btn('2'), activebackground="black",
              activeforeground='white')
num2.grid(column=2, row=2)
num2['font'] = font.Font(size=20)

num3 = Button(app, text='3', width=2, height=2, command=lambda: btn('3'), activebackground="black",
              activeforeground='white')
num3.grid(column=3, row=2)
num3['font'] = font.Font(size=20)

num4 = Button(app, text='4', width=2, height=2, command=lambda: btn('4'), activebackground="black",
              activeforeground='white')
num4.grid(column=1, row=3)
num4['font'] = font.Font(size=20)

num5 = Button(app, text='5', width=2, height=2, command=lambda: btn('5'), activebackground="black",
              activeforeground='white')
num5.grid(column=2, row=3)
num5['font'] = font.Font(size=20)

num6 = Button(app, text='6', width=2, height=2, command=lambda: btn('6'), activebackground="black",
              activeforeground='white')
num6.grid(column=3, row=3)
num6['font'] = font.Font(size=20)

num7 = Button(app, text='7', width=2, height=2, command=lambda: btn('7'), activebackground="black",
              activeforeground='white')
num7.grid(column=1, row=4)
num7['font'] = font.Font(size=20)

num8 = Button(app, text='8', width=2, height=2, command=lambda: btn('8'), activebackground="black",
              activeforeground='white')
num8.grid(column=2, row=4)
num8['font'] = font.Font(size=20)

num9 = Button(app, text='9', width=2, height=2, command=lambda: btn('9'), activebackground="black",
              activeforeground='white')
num9.grid(column=3, row=4)
num9['font'] = font.Font(size=20)

num0 = Button(app, text='0', width=2, height=2, command=lambda: btn('0'), activebackground="black",
              activeforeground='white')
num0.grid(column=1, row=5)
num0['font'] = font.Font(size=20)

dot = Button(app, text='.', width=2, height=2, command=lambda: btn('.'), activebackground="black",
             activeforeground='white')
dot.grid(column=2, row=5)
dot['font'] = font.Font(size=20)

eql = Button(app, text='=', width=2, height=2, command=btn_eq, activebackground="black",
             activeforeground='white')
eql.grid(column=3, row=5)
eql['font'] = font.Font(size=20)

lab = Label(app, text=' ', width=2, height=2)
lab.grid(column=4, row=1)
lab['font'] = font.Font(size=20)

btn_plus = Button(app, text='+', width=2, height=2, command=lambda: btn('+'), activebackground="black",
                  activeforeground='white')
btn_plus.grid(column=5, row=2)
btn_plus['font'] = font.Font(size=20)

btn_minus = Button(app, text='-', width=2, height=2, command=lambda: btn('-'), activebackground="black",
                   activeforeground='white')
btn_minus.grid(column=5, row=3)
btn_minus['font'] = font.Font(size=20)

btn_mul = Button(app, text='x', width=2, height=2, command=lambda: btn('x'), activebackground="black",
                 activeforeground='white')
btn_mul.grid(column=5, row=4)
btn_mul['font'] = font.Font(size=20)

btn_div = Button(app, text='÷', width=2, height=2, command=lambda: btn('÷'), activebackground="black",
                 activeforeground='white')
btn_div.grid(column=5, row=5)
btn_div['font'] = font.Font(size=20)

clear = Button(app, text='CLR', width=2, height=2, command=clr, activebackground="black",
               activeforeground='white')
clear.grid(column=5, row=1)
clear['font'] = font.Font(size=20)

lab2 = Label(app, text='')
lab2.grid(column=1, row=6)

sqr = Button(app, text='X²', width=2, height=2, command=sqr, activebackground="black",
             activeforeground='white')
sqr.grid(column=1, row=7)
sqr['font'] = font.Font(size=20)

sqrt = Button(app, text='√X', width=2, height=2, command=sqrt, activebackground="black",
              activeforeground='white')
sqrt.grid(column=2, row=7)
sqrt['font'] = font.Font(size=20)

powN = Button(app, text='X^n', width=2, height=2, command=lambda: btn('^'), activebackground="black",
              activeforeground='white')
powN.grid(column=3, row=7)
powN['font'] = font.Font(size=20)

binary = Button(app, text='bin', width=2, height=2, command=binary, activebackground="black",
                activeforeground='white')
binary.grid(column=1, row=8)
binary['font'] = font.Font(size=20)

hexa = Button(app, text='hex', width=2, height=2, command=hexa, activebackground="black",
              activeforeground='white')
hexa.grid(column=2, row=8)
hexa['font'] = font.Font(size=20)

octa = Button(app, text='oct', width=2, height=2, command=octa, activebackground="black",
              activeforeground='white')
octa.grid(column=3, row=8)
octa['font'] = font.Font(size=20)

app.mainloop()
