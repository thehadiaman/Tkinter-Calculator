from tkinter import *
from config import *
import math
from tkinter import font
from tkinter import filedialog as fd
from tkinter.messagebox import *
from random import *
from sys import *
from tkinter import ttk
##################################################################

def about():
    app = Tk()
    app.title('AboutMe')
    app.geometry('0x0+500+150')
    app.maxsize(width='300', height='150')
    app.minsize(width='300', height='150')
    app.config(bg='#042000')
    l0 = Label(app, text='Hello, I am HADI AMAN. I am a student.')
    l0.place(x=5, y=10)
    l0.config(bg='#042000')
    l1 = Label(app, text='Email     : hadiaman2.0@gmail.com')
    l1.place(x=5, y=30)
    l1.config(bg='#042000')
    l2 = Label(app, text='Mobile    : 8281177057')
    l2.place(x=5, y=50)
    l2.config(bg='#042000')
    l3 = Label(app, text='Instagram : _hadi.aman_')
    l3.place(x=5, y=70)
    l3.config(bg='#042000')
    l4 = Label(app, text=':::Be my friend:::')
    l4.place(x=5, y=90)
    l4.config(bg='#042000')
    app.mainloop()


def equal(z):
    global eqa
    List = []
    x = 0
    for a in z:
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
        elif a == 'e':
            List.insert(x, str(math.e))
        elif a == 'π':
            List.insert(x, str(math.pi))
        else:
            List.insert(x, a)
    List.reverse()

    x = ''
    for a in List:
        x += a
    eqa = x



    if '%' in eqa:
        e = eqa.split('%')
        x = (eval(e[0])*eval(e[1]))/100
        return str(round(x, 7))

    elif 'sin' in eqa:
        e = int(eqa.split('sin(')[1].split(')')[0])
        return round(math.sin(math.pi/(e/5)), 7)

    elif 'cos' in eqa:
        e = int(eqa.split('cos(')[1].split(')')[0])
        return round(math.cos(math.pi/(e/5)), 7)

    elif 'tan' in eqa:
        e = int(eqa.split('tan(')[1].split(')')[0])
        return round(math.tan(math.pi/(e/5)), 7)

    res = eval(x)
    return str(round(res, 7))


def onedelete(equ):
    if equ == 'SYNTAX ERROR':
        return ''
    length = len(equ)
    return equ[0: length-1]


def credit():
    app = Tk()
    app.title('Credit')
    app.geometry('0x0+500+150')
    app.maxsize(width='650', height='150')
    app.minsize(width='650', height='150')
    app.config(bg='#042000')
    l = Label(app, text='This is my first project on python tkinter I tried to make it better,there is only one organiz'
                        'ation\ni give all the credit to That is CROSS_ROAD and the motive behind the project is to acc'
                        'ept and\ncomplete the challenge of our teacher Nikhil sir', justify=LEFT)
    l.place(x=0, y=0)
    l.config(bg='#042000')
    app.mainloop()


def root(x):
    flag = 0
    if '√' in x:
        for a in range(0, 9):
            w = ''
            w = str(a)+'√'
            if w in x:
                z = x.replace(w, w[0]+'x√')
                flag = 1
            else:
                zz = x
    else:
        zz = x

    if flag == 1:
        return z
    else:
        return zz


def bracket(x):
    flag = 0
    if '(' in x:
        for a in range(0, 9):
            w = ''
            w = str(a)+'('
            if w in x:
                z = x.replace(w, w[0]+'x(')
                flag = 1
            else:
                zz = x
    else:
        zz = x

    if flag == 1:
        return z
    else:
        return zz

def pipi(x):
    flag = 0
    if 'π' in x:
        for a in range(0, 9):
            w = ''
            w = str(a)+'π'
            if w in x:
                z = x.replace(w, w[0]+'xπ')
                flag = 1
            else:
                zz = x
    else:
        zz = x

    if flag == 1:
        return z
    else:
        return zz

def ee(x):
    flag = 0
    if 'e' in x:
        for a in range(0, 9):
            w = ''
            w = str(a)+'e'
            if w in x:
                z = x.replace(w, w[0]+'xe')
                flag = 1
            else:
                zz = x
    else:
        zz = x

    if flag == 1:
        return z
    else:
        return zz


def epi(x):
    if 'eπ' in x:
        return 'exπ'
    elif 'πe' in x:
        return 'πxe'
    else:
        return x
