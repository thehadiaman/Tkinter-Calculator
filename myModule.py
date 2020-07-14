from tkinter import *
from config import *
import math
from tkinter import font
from tkinter import filedialog as fd
from tkinter.messagebox import *
from random import *
from sys import *
import numpy as np
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

    if 'sin(' in x:
        num = int(x.split('sin(')[1].split(')')[0])
        x = x.replace(f'sin({str(num)}', f'np.sin(np.deg2rad({str(num)})')


    if 'cos(' in x:
        num = int(x.split('cos(')[1].split(')')[0])
        x = x.replace(f'cos({str(num)}', f'np.cos(np.deg2rad({str(num)})')

    if 'tan(' in x:
        num = int(x.split('tan(')[1].split(')')[0])
        x = x.replace(f'tan({str(num)}', f'np.tan(np.deg2rad({str(num)})')

    if 'sin−¹(' in x:
        num = x.split('sin−¹(')[1].split(')')[0]
        x = x.replace(f'sin−¹({str(num)}', f'np.degrees(np.arcsin(float({num}))')

    if 'cos−¹(' in x:
        num = x.split('cos−¹(')[1].split(')')[0]
        x = x.replace(f'cos−¹({str(num)}', f'np.degrees(np.arccos(float({num}))')

    if 'tan−¹(' in x:
        num = x.split('tan−¹(')[1].split(')')[0]
        x = x.replace(f'tan−¹({str(num)}', f'np.degrees(np.arctan(float({num}))')

    if 'sinh(' in x:
        num = int(x.split('sinh(')[1].split(')')[0])
        x = x.replace(f'sinh({str(num)}', f'np.sinh(np.deg2rad({str(num)})')

    if 'cosh(' in x:
        num = int(x.split('cosh(')[1].split(')')[0])
        x = x.replace(f'cosh({str(num)}', f'np.cosh(np.deg2rad({str(num)})')

    if 'tanh(' in x:
        num = int(x.split('tanh(')[1].split(')')[0])
        x = x.replace(f'tanh({str(num)}', f'np.tanh(np.deg2rad({str(num)})')

    if 'sinh−¹(' in x:
        num = x.split('sinh−¹(')[1].split(')')[0]
        x = x.replace(f'sinh−¹({str(num)}', f'np.degrees(np.arcsinh(float({num}))')

    if 'cosh−¹(' in x:
        num = x.split('cosh−¹(')[1].split(')')[0]
        x = x.replace(f'cosh−¹({str(num)}', f'np.degrees(np.arccosh(float({num}))')

    if 'tanh−¹(' in x:
        num = x.split('tanh−¹(')[1].split(')')[0]
        x = x.replace(f'tanh−¹({str(num)}', f'np.degrees(np.arctanh(float({num}))')

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

def zeroError(x):
    def startsWithZero(x):
        while x.startswith('0'):
            if x.startswith('0+'):
                return x
            else:
                x = x[1:]
        return x

    def zeroSmash(x):
        while '+0' in x:
            x = x.replace('+0', '+')
        while '-0' in x:
            x = x.replace('-0', '-')
        while 'x0' in x:
            x = x.replace('x0', 'x')
        while '/0' in x:
            x = x.replace('/0', '/')
        return x

    def errorSmash(x):
        list0 = ['x', '/']

        for a in list0:
            for b in list0:
                while a+b in x:
                    x = x.replace(a+b, a+'0'+b)
        return x

    return errorSmash(zeroSmash(startsWithZero(x)))


def errortest(y):

    x = y
    x = y.replace('*', 'x')
    x = y.replace('/', '÷')

    list0 = ['x', '÷']

    for a in list0:
        for b in list0:
            if a+b in x:
                flag = 1
                return 'error'
            else:
                flag = 0
    if flag == 0:
        return x



def final(x):
    return zeroError(errortest(x))

