import math
##################################


def toBinary(num):
    a = bin(num)
    b = str(a)
    c = b[2:]
    return c


def toHex(num):
    a = hex(num)
    b = str(a)
    c = b[2:]
    return c


def toOct(num):
    a = oct(num)
    b = str(a)
    c = b[2:]
    return c


def sqRoot(num):
    num = float(num)
    return math.sqrt(num)


def sqR(num):
    num = float(num)
    return pow(num, 2)


def total(eq):
    List = []
    x = 0
    for a in eq:
        if a == '÷':
            List.insert(x, '/')
        elif a == '^':
            List.insert(x, '**')
        elif a == 'x':
            List.insert(x, '*')
        else:
            List.insert(x, a)
    List.reverse()

    x = ''
    for a in List:
        x += a
    ans = eval(x)

    return str(ans)
