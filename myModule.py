from tkinter import *
import math
from tkinter import font
from tkinter import filedialog
from tkinter import filedialog as fd
from tkinter.messagebox import *
import os


def about():
    app = Tk()
    app.title('AboutMe')
    app.geometry('270x100')
    l0 = Label(app, text='Hello, I am HADI AMAN. I am a student.')
    l0.place(x=5, y=10)
    l1 = Label(app, text='Email   : hadiaman2.0@gmail.com')
    l1.place(x=5, y=30)
    l2 = Label(app, text='Mobile : 8281177057')
    l2.place(x=5, y=50)

    app.mainloop()


def equal(eqa):
    if '%' in eqa:
        e = eqa.split('%')
        x = (int(e[0])*int(e[1]))/100
        return str(x)

    elif 'sin' in eqa:
        e = int(eqa.split('sin(')[1].split(')')[0])

        if len(eqa.split('sin(')) >= 3:
            return 'x'

        return math.sin(math.pi/(e/5))

    elif 'cos' in eqa:
        e = int(eqa.split('cos(')[1].split(')')[0])

        if len(eqa.split('cos(')) >= 3:
            return 'x'

        return math.cos(math.pi/(e/5))

    elif 'tan' in eqa:
        e = int(eqa.split('tan(')[1].split(')')[0])

        if len(eqa.split('tan(')) >= 3:
            return 'x'

        return math.tan(math.pi/(e/5))

    else:
        List = []
        x = 0
        for a in eqa:
            if a == '÷':
                List.insert(x, '/')
            elif a == '^':
                List.insert(x, '**')
            elif a == 'x':
                List.insert(x, '*')
            elif a == '²':
                List.insert(x, '**2')
            elif a == '√':
                List.insert(x, 'math.sqrt')
            else:
                List.insert(x, a)
        List.reverse()

        x = ''
        for a in List:
            x += a
        ans = eval(x)

        return str(ans)


def onedelete(equ):
    length = len(equ)
    return equ[0: length-1]


def credit():
    app = Tk()
    app.title('Credit')
    app.geometry('620x100')
    l = Label(app, text='''This is my first project on python tkinter I tried to make it better,there is only one organization\ni give all the credit to That is CROSS_ROAD and the motive behind the project is to accept and\ncomplete the challenge of our teacher Nikhil sir''', justify=LEFT)
    l.place(x=0, y=0)

    app.mainloop()

