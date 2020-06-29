from myModule import *
#################################################################################################
app = Tk()
app.title('Calculator')
app.maxsize(width='394', height='452')
app.minsize(width='394', height='452')
##################################################################################################
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
    e = bracket(root(x))

    if e == '':
        tv.set('')
    else:
        try:
            x = equal(e)
            tv.set(x)
        except:
            tv.set('SYNTAX ERROR')
            eq = ''


pwd = str(os.popen('pwd').read())


def importEquation():
    app.filename = fd.askopenfilename(initialdir=pwd, title="Import Equation",
                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    try:
        with open(app.filename, 'r') as file:
            global eq
            eq = file.read()
            tv.set(eq)
    except:
        pass


def saveEquation():
    app.filename = fd.asksaveasfilename(initialdir=pwd, title="Save Equation",
                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    try:
        with open(app.filename, 'w+') as file:
            file.write(str(eqa.get()))
    except:
        pass


def angle(sign):
    global eq
    eq = eqa.get() + sign
    tv.set(eq)


###################################################################################################


menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Clear All", command=clr)
filemenu.add_command(label="Import Equation", command=importEquation)
filemenu.add_command(label="Save Equation", command=saveEquation)
filemenu.add_command(label="About Me", command=about)
filemenu.add_command(label="Credit", command=credit)
filemenu.add_command(label="Close", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)
app.config(menu=menubar)

tv = StringVar()
eqa = Entry(app, border=20, width=14, bg='white', cursor='pencil', xscroll=True, justify='right', textvariable=tv)
eqa.place(x=0, y=0)
eqa.config(fg='black')
eqa['font'] = font.Font(size=30)
eqa.bind("<a>", "no")
eqa.bind("<b>", "no")
eqa.bind("<c>", "no")
eqa.bind("<d>", "no")
eqa.bind("<e>", "no")
eqa.bind("<f>", "no")
eqa.bind("<g>", "no")
eqa.bind("<h>", "no")
eqa.bind("<i>", "no")
eqa.bind("<j>", "no")
eqa.bind("<k>", "no")
eqa.bind("<l>", "no")
eqa.bind("<m>", "no")
eqa.bind("<n>", "no")
eqa.bind("<o>", "no")
eqa.bind("<p>", "no")
eqa.bind("<q>", "no")
eqa.bind("<r>", "no")
eqa.bind("<s>", "no")
eqa.bind("<t>", "no")
eqa.bind("<u>", "no")
eqa.bind("<v>", "no")
eqa.bind("<w>", "no")
eqa.bind("<x>", "no")
eqa.bind("<y>", "no")
eqa.bind("<z>", "no")
eqa.bind("<A>", "no")
eqa.bind("<B>", "no")
eqa.bind("<C>", "no")
eqa.bind("<D>", "no")
eqa.bind("<E>", "no")
eqa.bind("<F>", "no")
eqa.bind("<G>", "no")
eqa.bind("<H>", "no")
eqa.bind("<I>", "no")
eqa.bind("<J>", "no")
eqa.bind("<K>", "no")
eqa.bind("<L>", "no")
eqa.bind("<M>", "no")
eqa.bind("<N>", "no")
eqa.bind("<O>", "no")
eqa.bind("<P>", "no")
eqa.bind("<Q>", "no")
eqa.bind("<R>", "no")
eqa.bind("<S>", "no")
eqa.bind("<T>", "no")
eqa.bind("<U>", "no")
eqa.bind("<V>", "no")
eqa.bind("<W>", "no")
eqa.bind("<X>", "no")
eqa.bind("<Y>", "no")
eqa.bind("<Z>", "no")
eqa.bind("!", "no")
eqa.bind("@", "no")
eqa.bind("$", "no")
eqa.bind("#", "no")
eqa.bind("&", "no")
eqa.bind("_", "no")
eqa.bind("?", "no")
eqa.bind(":", "no")
eqa.bind("j", "no")
eqa.bind(">", "no")
eqa.bind("|", "no")
eqa.bind("]", "no")
eqa.bind("[", "no")
eqa.bind("{", "no")
eqa.bind("}", "no")
eqa.bind(";", "no")
eqa.bind(",", "no")
eqa.bind("'", "no")
eqa.bind('"', "no")
eqa.bind("~", "no")
eqa.bind("`", "no")
eqa.bind("\\", "no")

eqa.event_add('<<Copy>>', '<Control-c>')
eqa.event_add('<<Paste>>', '<Control-v>')
eqa.event_add('<<Cut>>', '<Control-x>')


base = Label(app)
base.place(x=7, y=100)

key7 = Button(base, text='7', width=5, command=lambda: key('7'))
key7.grid(column=0, row=0)
key7['font'] = font.Font(size=15)

key8 = Button(base, text='8', width=5, command=lambda: key('8'))
key8.grid(column=1, row=0)
key8['font'] = font.Font(size=15)

key9 = Button(base, text='9', width=5, command=lambda: key('9'))
key9.grid(column=2, row=0)
key9['font'] = font.Font(size=15)

key4 = Button(base, text='4', width=5, command=lambda: key('4'))
key4.grid(column=0, row=1)
key4['font'] = font.Font(size=15)

key5 = Button(base, text='5', width=5, command=lambda: key('5'))
key5.grid(column=1, row=1)
key5['font'] = font.Font(size=15)

key6 = Button(base, text='6', width=5, command=lambda: key('6'))
key6.grid(column=2, row=1)
key6['font'] = font.Font(size=15)

key1 = Button(base, text='1', width=5, command=lambda: key('1'))
key1.grid(column=0, row=2)
key1['font'] = font.Font(size=15)

key2 = Button(base, text='2', width=5, command=lambda: key('2'))
key2.grid(column=1, row=2)
key2['font'] = font.Font(size=15)

key3 = Button(base, text='3', width=5, command=lambda: key('3'))
key3.grid(column=2, row=2)
key3['font'] = font.Font(size=15)

dot = Button(base, text='.', width=5, command=lambda: key('.'))
dot.grid(column=0, row=3)
dot['font'] = font.Font(size=15)

key0 = Button(base, text='0', width=5, command=lambda: key('0'))
key0.grid(column=1, row=3)
key0['font'] = font.Font(size=15)

clr = Button(base, text='⌫', width=5, command=clrone)
clr.grid(column=2, row=3)
clr['font'] = font.Font(size=15)

space = Label(base)
space.grid(column=3, row=1)


add = Button(base, text='+', width=5, command=lambda: key('+'))
add.grid(column=4, row=0)
add['font'] = font.Font(size=15)

minus = Button(base, text='-', width=5, command=lambda: key('-'))
minus.grid(column=4, row=1)
minus['font'] = font.Font(size=15)

mul = Button(base, text='x', width=5, command=lambda: key('x'))
mul.grid(column=4, row=2)
mul['font'] = font.Font(size=15)

div = Button(base, text='÷', width=5, command=lambda: key('÷'))
div.grid(column=4, row=3)
div['font'] = font.Font(size=15)

base2 = Label(app)
base2.place(x=7, y=260)

bra_f = Button(base2, text='(', width=5, command=lambda: key('('))
bra_f.grid(column=0, row=0)
bra_f['font'] = font.Font(size=15)

bra_l = Button(base2, text=')', width=5, command=lambda: key(')'))
bra_l.grid(column=1, row=0)
bra_l['font'] = font.Font(size=15)

per = Button(base2, text='%', width=5, command=lambda: key('%'))
per.grid(column=2, row=0)
per['font'] = font.Font(size=15)

sqr = Button(base2, text='X²', width=5, command=lambda: key('²'))
sqr.grid(column=0, row=1)
sqr['font'] = font.Font(size=15)

sqRoot = Button(base2, text='√X', width=5, command=lambda: key('√('))
sqRoot.grid(column=1, row=1)
sqRoot['font'] = font.Font(size=15)

sqrN = Button(base2, text='^', width=5, command=lambda: key('^'))
sqrN.grid(column=2, row=1)
sqrN['font'] = font.Font(size=15)

sin = Button(base2, text='sin', width=5, command=lambda: angle('sin('))
sin.grid(column=0, row=2)
sin['font'] = font.Font(size=15)

cos = Button(base2, text='cos', width=5, command=lambda: angle('cos('))
cos.grid(column=1, row=2)
cos['font'] = font.Font(size=15)

tan = Button(base2, text='tan', width=5, command=lambda: angle('tan('))
tan.grid(column=2, row=2)
tan['font'] = font.Font(size=15)


binary = Button(base2, text='Binary', width=5, command=Binary)
binary.grid(column=0, row=3)
binary['font'] = font.Font(size=15)

Hexal = Button(base2, text='Hexal', width=5, command=Hexal)
Hexal.grid(column=1, row=3)
Hexal['font'] = font.Font(size=15)

octal = Button(base2, text='Octal', width=5, command=Octal)
octal.grid(column=2, row=3)
octal['font'] = font.Font(size=15)

space = Label(base2)
space.grid(column=3, row=0)

eql = Button(app, text='=', height=5, width=5, command=eql)
eql.place(x=292, y=260)
eql['font'] = font.Font(size=15)

app.mainloop()
