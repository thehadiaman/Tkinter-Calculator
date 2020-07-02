from myModule import *
#################################################################################################
app = Tk()
app.title(get_app_title())
app.geometry('0x0+500+150')

if platform == 'linux':
    app.maxsize(width='397', height='520')
    app.minsize(width='397', height='520')
elif platform.startswith('win'):
    app.maxsize(width='280', height='520')
    app.minsize(width='280', height='520')
else:
    app.maxsize(width='355', height='520')
    app.minsize(width='355', height='520')

bg_color = get_bg_color()
app.config(bg=bg_color)
##################################################################################################
ebgcolor = get_ebgcolor()
bg_color_btn = get_bg_color_btn()
fg_color_btn = get_fg_color_btn()
activebackground_color = get_activebackground_color()
activeforeground_color = get_activeforeground_color()
################################################################################################

eq = ''

def key(val):
    global eq
    eq = (eqa.get() + val).replace('<', '').replace(' ', '')
    tv.set(eq)


def clrone():
    global eq
    e = onedelete(eqa.get())
    tv.set(e)
    eq = e


def clr():
    global eq
    tv.set('')


def Binary():

    try:
        e = eval(eqa.get())
        tv.set(bin(e)[2:])
    except:
        tv.set('SYNTAX ERROR')


def Hexal():
    try:
        e = eval(eqa.get())
        tv.set(hex(e)[2:])
    except:
        tv.set('SYNTAX ERROR')


def Octal():
    try:
        e = eval(eqa.get())
        tv.set(oct(e)[2:])
    except:
        tv.set('SYNTAX ERROR')


def eql():
    global eq
    x = eqa.get().replace('<', '').replace(' ', '')
    e = bracket(root(pipi(ee(x))))

    if e == '':
        tv.set('')
    else:
        try:
            x = equal(e)
            tv.set(x)
        except:
            tv.set('SYNTAX ERROR')
            eq = ''


def importEquation():
    app.filename = fd.askopenfilename(title='Import Equation',
                                      filetypes=(('text files', '*.txt'), ('all files', '*.*')))
    try:
        with open(app.filename, 'r') as file:
            global eq
            eq = file.read()
            tv.set(eq)
    except:
        pass


def saveEquation():
    app.filename = fd.asksaveasfilename(title='Save Equation',
                                      filetypes=(('text files', '*.txt'), ('all files', '*.*')))
    try:
        with open(app.filename, 'w+') as file:
            file.write(str(eqa.get()))
    except:
        pass


def angle(sign):
    global eq
    eq = eqa.get() + sign
    tv.set(eq)


def Rand():
    tv.set(eqa.get() + str(randrange(0, 9999999999)))


###################################################################################################


menubar = Menu(app, bg=get_bg_menu(), activebackground=get_bg_color())
filemenu = Menu(menubar, tearoff=0, bg=get_bg_menu(), activebackground=get_bg_color())
filemenu.add_command(label='Clear All', command=clr)
filemenu.add_command(label='Import Equation', command=importEquation)
filemenu.add_command(label='Save Equation', command=saveEquation)
filemenu.add_command(label='About Me', command=about)
filemenu.add_command(label='Credit', command=credit)
filemenu.add_separator()
filemenu.add_command(label='Close', command=app.quit)
menubar.add_cascade(label='File', menu=filemenu)

config = Menu(menubar, tearoff=0, bg=get_bg_menu(), activebackground=get_bg_color())
config.add_command(label='Set title', command=set_app_title)
config.add_command(label='Set MenuBar color', command=set_bg_menu)
config.add_command(label='Set background color', command=set_bg_color)
config.add_command(label='Set display color', command=set_ebgcolor)
config.add_command(label='Set color of button', command=set_bg_color_btn)
config.add_command(label='Set foreground color of button', command=set_fg_color_btn)
config.add_command(label='Set activebackground color of button', command=set_activebackground_color)
config.add_command(label='Set activeforeground color of button', command=set_activeforeground_color)
menubar.add_cascade(label='Configure', menu=config)

app.config(menu=menubar)

base3 = Label(app)
base3.place(x=0, y=0)
base3.config(bg=bg_color)

tv = StringVar()
eqa = Entry(base3, border=20, bg=ebgcolor, cursor='pencil', justify='left', textvariable=tv)
eqa.grid(column=0, row=0)
if platform == 'linux':
    eqa.config(width=14)
elif platform.startswith('win'):
    eqa.config(width=10)
else:
    eqa.config(width=14)
eqa.config(fg=bg_color, highlightbackground=bg_color)
eqa['font'] = font.Font(size=30)
eqa.bind('<a>', 'no')
eqa.bind('<b>', 'no')
eqa.bind('<c>', 'no')
eqa.bind('<d>', 'no')
eqa.bind('<e>', 'no')
eqa.bind('<f>', 'no')
eqa.bind('<g>', 'no')
eqa.bind('<h>', 'no')
eqa.bind('<i>', 'no')
eqa.bind('<j>', 'no')
eqa.bind('<k>', 'no')
eqa.bind('<l>', 'no')
eqa.bind('<m>', 'no')
eqa.bind('<n>', 'no')
eqa.bind('<o>', 'no')
eqa.bind('<p>', 'no')
eqa.bind('<q>', 'no')
eqa.bind('<r>', 'no')
eqa.bind('<s>', 'no')
eqa.bind('<t>', 'no')
eqa.bind('<u>', 'no')
eqa.bind('<v>', 'no')
eqa.bind('<w>', 'no')
eqa.bind('<x>', 'no')
eqa.bind('<y>', 'no')
eqa.bind('<z>', 'no')
eqa.bind('<A>', 'no')
eqa.bind('<B>', 'no')
eqa.bind('<C>', 'no')
eqa.bind('<D>', 'no')
eqa.bind('<E>', 'no')
eqa.bind('<F>', 'no')
eqa.bind('<G>', 'no')
eqa.bind('<H>', 'no')
eqa.bind('<I>', 'no')
eqa.bind('<J>', 'no')
eqa.bind('<K>', 'no')
eqa.bind('<L>', 'no')
eqa.bind('<M>', 'no')
eqa.bind('<N>', 'no')
eqa.bind('<O>', 'no')
eqa.bind('<P>', 'no')
eqa.bind('<Q>', 'no')
eqa.bind('<R>', 'no')
eqa.bind('<S>', 'no')
eqa.bind('<T>', 'no')
eqa.bind('<U>', 'no')
eqa.bind('<V>', 'no')
eqa.bind('<W>', 'no')
eqa.bind('<X>', 'no')
eqa.bind('<Y>', 'no')
eqa.bind('<Z>', 'no')
eqa.bind('!', 'no')
eqa.bind('@', 'no')
eqa.bind('$', 'no')
eqa.bind('#', 'no')
eqa.bind('&', 'no')
eqa.bind('_', 'no')
eqa.bind('?', 'no')
eqa.bind(':', 'no')
eqa.bind('j', 'no')
eqa.bind('>', 'no')
eqa.bind('|', 'no')
eqa.bind(']', 'no')
eqa.bind('[', 'no')
eqa.bind('{', 'no')
eqa.bind('}', 'no')
eqa.bind(';', 'no')
eqa.bind(',', 'no')
eqa.bind(''', 'no')
eqa.bind(''', 'no')
eqa.bind('~', 'no')
eqa.bind('`', 'no')
eqa.bind('\\', 'no')


space0 = Label(base3)
space0.grid(column=0, row=1)
space0.config(bg=bg_color)

base = Label(base3)
base.grid(column=0, row=2)
base.config(bg=bg_color)

key7 = Button(base, text='7', width=5, command=lambda: key('7'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key7.grid(column=0, row=0)
key7['font'] = font.Font(size=15)

key8 = Button(base, text='8', width=5, command=lambda: key('8'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key8.grid(column=1, row=0)
key8['font'] = font.Font(size=15)

key9 = Button(base, text='9', width=5, command=lambda: key('9'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key9.grid(column=2, row=0)
key9['font'] = font.Font(size=15)

key4 = Button(base, text='4', width=5, command=lambda: key('4'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key4.grid(column=0, row=1)
key4['font'] = font.Font(size=15)

key5 = Button(base, text='5', width=5, command=lambda: key('5'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key5.grid(column=1, row=1)
key5['font'] = font.Font(size=15)

key6 = Button(base, text='6', width=5, command=lambda: key('6'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key6.grid(column=2, row=1)
key6['font'] = font.Font(size=15)

key1 = Button(base, text='1', width=5, command=lambda: key('1'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key1.grid(column=0, row=2)
key1['font'] = font.Font(size=15)

key2 = Button(base, text='2', width=5, command=lambda: key('2'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key2.grid(column=1, row=2)
key2['font'] = font.Font(size=15)

key3 = Button(base, text='3', width=5, command=lambda: key('3'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key3.grid(column=2, row=2)
key3['font'] = font.Font(size=15)

dot = Button(base, text='.', width=5, command=lambda: key('.'), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
dot.grid(column=0, row=3)
dot['font'] = font.Font(size=15)

key0 = Button(base, text='0', width=5, command=lambda: key('0'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
key0.grid(column=1, row=3)
key0['font'] = font.Font(size=15)

clr = Button(base, text='⌫', width=5, command=clrone, bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
clr.grid(column=2, row=3)
clr['font'] = font.Font(size=15)

space = Label(base)
space.grid(column=3, row=1)
space.config(bg=bg_color)


add = Button(base, text='+', width=5, command=lambda: key('+'), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
add.grid(column=4, row=0)
add['font'] = font.Font(size=15)

minus = Button(base, text='-', width=5, command=lambda: key('-'), bg=bg_color_btn, border=2, fg=fg_color_btn,
               activebackground=activebackground_color, activeforeground=activeforeground_color)
minus.grid(column=4, row=1)
minus['font'] = font.Font(size=15)

mul = Button(base, text='x', width=5, command=lambda: key('x'), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
mul.grid(column=4, row=2)
mul['font'] = font.Font(size=15)

div = Button(base, text='÷', width=5, command=lambda: key('÷'), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
div.grid(column=4, row=3)
div['font'] = font.Font(size=15)

base0 = Label(base3)
base0.grid(column=0, row=3)
base0.config(bg=bg_color)

base2 = Label(base0)
base2.grid(column=0, row=0)
base2.config(bg=bg_color)

bra_f = Button(base2, text='(', width=5, command=lambda: key('('), bg=bg_color_btn, border=2, fg=fg_color_btn,
               activebackground=activebackground_color, activeforeground=activeforeground_color)
bra_f.grid(column=0, row=0)
bra_f['font'] = font.Font(size=15)

bra_l = Button(base2, text=')', width=5, command=lambda: key(')'), bg=bg_color_btn, border=2, fg=fg_color_btn,
               activebackground=activebackground_color, activeforeground=activeforeground_color)
bra_l.grid(column=1, row=0)
bra_l['font'] = font.Font(size=15)

per = Button(base2, text='%', width=5, command=lambda: key('%'), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
per.grid(column=2, row=0)
per['font'] = font.Font(size=15)

pi = Button(base2, text='π', width=5, command=lambda: key('π'), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
pi.grid(column=0, row=1)
pi['font'] = font.Font(size=15)

e = Button(base2, text='e', width=5, command=lambda: key('e'), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
e.grid(column=1, row=1)
e['font'] = font.Font(size=15)

tan = Button(base2, text='Random', width=5, command=Rand, bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
tan.grid(column=2, row=1)
tan['font'] = font.Font(size=15)

sqr = Button(base2, text='X²', width=5, command=lambda: key('²'), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
sqr.grid(column=0, row=2)
sqr['font'] = font.Font(size=15)

sqRoot = Button(base2, text='√X', width=5, command=lambda: key('√('), bg=bg_color_btn, border=2, fg=fg_color_btn,
                activebackground=activebackground_color, activeforeground=activeforeground_color)
sqRoot.grid(column=1, row=2)
sqRoot['font'] = font.Font(size=15)

sqrN = Button(base2, text='^', width=5, command=lambda: key('^'), bg=bg_color_btn, border=2, fg=fg_color_btn,
              activebackground=activebackground_color, activeforeground=activeforeground_color)
sqrN.grid(column=2, row=2)
sqrN['font'] = font.Font(size=15)

sin = Button(base2, text='sin', width=5, command=lambda: angle('sin('), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
sin.grid(column=0, row=3)
sin['font'] = font.Font(size=15)

cos = Button(base2, text='cos', width=5, command=lambda: angle('cos('), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
cos.grid(column=1, row=3)
cos['font'] = font.Font(size=15)

tan = Button(base2, text='tan', width=5, command=lambda: angle('tan('), bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
tan.grid(column=2, row=3)
tan['font'] = font.Font(size=15)


binary = Button(base2, text='Binary', width=5, command=Binary, bg=bg_color_btn, border=2, fg=fg_color_btn,
                activebackground=activebackground_color, activeforeground=activeforeground_color)
binary.grid(column=0, row=4)
binary['font'] = font.Font(size=15)

Hexal = Button(base2, text='Hexal', width=5, command=Hexal, bg=bg_color_btn, border=2, fg=fg_color_btn,
               activebackground=activebackground_color, activeforeground=activeforeground_color)
Hexal.grid(column=1, row=4)
Hexal['font'] = font.Font(size=15)

octal = Button(base2, text='Octal', width=5, command=Octal, bg=bg_color_btn, border=2, fg=fg_color_btn,
               activebackground=activebackground_color, activeforeground=activeforeground_color)
octal.grid(column=2, row=4)
octal['font'] = font.Font(size=15)

space2 = Label(base2)
space2.grid(column=3, row=0)
space2.config(bg=bg_color)

eql = Button(base0, text='=', height=8, width=5, command=eql, bg=bg_color_btn, border=2, fg=fg_color_btn,
             activebackground=activebackground_color, activeforeground=activeforeground_color)
eql.grid(column=1, row=0)
eql['font'] = font.Font(size=15)

app.mainloop()

