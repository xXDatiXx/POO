import math
from tkinter import *

flg_key = False
arr = ''


def click(e):
    global arr
    e = str(e)
    if e == 'C':
        arr = ' '
        lbl_1.configure(text=arr)
    elif e == '+':
        arr = (arr + e)
        lbl_1.configure(text=arr)
    elif e == '.':
        arr = (arr + e)
        lbl_1.configure(text=arr)
    elif e == '^':
        arr = (arr + '**')
        lbl_1.configure(text=arr)
    elif e == 'borrar':
        arr = arr[:-1]
        lbl_1.configure(text=arr)
    else:
        arr = (arr + e)
        lbl_1.configure(text=arr)


def key_down(e):
    global flg_key, arr
    if not flg_key:
        if e.char.isdigit():
            click(e.char)
        elif e.char == '\r':
            resuelve()
        elif e.char == 'C' or e.char == 'c':
            arr = ' '
            lbl_1.configure(text=arr)
        elif e.char == '+':
            click('+')
        elif e.char == '/':
            click('/')
        elif e.char == '(':
            click('(')
        elif e.char == ')':
            click(')')
        elif e.char == '-':
            click('-')
        elif e.char == '.':
            click('.')
        elif e.char == '%':
            click('/100')
        elif e.char == '^':
            click('^')
        elif e.char == '*' or e.char == 'x':
            click('*')
        elif e.char == '\b':
            click('borrar')
        else:
            pass
        flg_key = True


def key_up(e):
    global flg_key
    flg_key = False


def resuelve():
    global arr
    try:
        resu = str(eval(arr))
        arr = ' '
        lbl_1.configure(text=resu)
    except:
        lbl_1.configure(text='*Syntax ERROR*')
# https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/ para resolver +,-,/,* y por jerarquía de operaciones


window_1 = Tk()
window_1.title('Dati´s calculator')
window_1.bind('<KeyPress>', key_down)
window_1.bind('<KeyRelease>', key_up)
# window_1.geometry('900x700')


lbl_1 = Label(window_1, text='0', font=('Arial Bold', 34), bg='#393433', fg='#FFFFFF', padx=150)
lbl_1.grid(column=0, row=0, columnspan=6)

# botones de la calcu
btn_num1 = Button(window_1, text='1', padx=20, pady=10, command=lambda: click('1'))
btn_num1.grid(column=0, row=3)

btn_num2 = Button(window_1, text='2', padx=20, pady=10, command=lambda: click('2'))
btn_num2.grid(column=1, row=3)

btn_num3 = Button(window_1, text='3', padx=20, pady=10, command=lambda: click('3'))
btn_num3.grid(column=2, row=3)

btn4 = Button(window_1, text='÷', padx=18, pady=10, command=lambda: click('/'))
btn4.grid(column=3, row=1)

btn_num4 = Button(window_1, text='4', padx=20, pady=10, command=lambda: click('4'))
btn_num4.grid(column=0, row=2)

btn_num5 = Button(window_1, text='5', padx=20, pady=10, command=lambda: click('5'))
btn_num5.grid(column=1, row=2)

btn_num6 = Button(window_1, text='6', padx=20, pady=10, command=lambda: click('6'))
btn_num6.grid(column=2, row=2)

btn_mul = Button(window_1, text='x', padx=18, pady=10, command=lambda: click('*'))
btn_mul.grid(column=3, row=2)

btn_num7 = Button(window_1, text='7', padx=20, pady=10, command=lambda: click('7'))
btn_num7.grid(column=0, row=1)

btn_num8 = Button(window_1, text='8', padx=20, pady=10, command=lambda: click('8'))
btn_num8.grid(column=1, row=1)

btn_num9 = Button(window_1, text='9', padx=20, pady=10, command=lambda: click('9'))
btn_num9.grid(column=2, row=1)

btn_suma = Button(window_1, text='+', padx=18, pady=10, command=lambda: click('+'))
btn_suma.grid(column=3, row=3)

btn_num0 = Button(window_1, text='0', padx=20, pady=10, command=lambda: click('0'))
btn_num0.grid(column=1, row=4)

btn_rest = Button(window_1, text='-', padx=18, pady=10, command=lambda: click('-'))
btn_rest.grid(column=3, row=4)

btn_C = Button(window_1, text='C', padx=20, pady=10, bg='#8EB4E5',command=lambda: click('C'))
btn_C.grid(column=0, row=4)

btn_raiz = Button(window_1, text='√', padx=18, pady=10, command=lambda: click('**0.5'))
btn_raiz.grid(column=4, row=1)

btn_expo = Button(window_1, text='^', padx=18, pady=10, command=lambda: click('**'))
btn_expo.grid(column=4, row=2)

btn_ig = Button(window_1, text='=', padx=18, pady=10, bg='#2AFF00', command=lambda: resuelve())
btn_ig.grid(column=4, row=4)

btn_porc = Button(window_1, text='%', padx=18, pady=10, command=lambda: click('/100'))
btn_porc.grid(column=4, row=3)

btn_dott = Button(window_1, text='.', padx=20, pady=10, command=lambda: click('.'))
btn_dott.grid(column=2, row=4)

btn_borr = Button(window_1, text='←', padx=18, pady=10, bg='#FF0000', command=lambda: click('borrar'))
btn_borr.grid(column=5, row=1)

btn_jaja = Button(window_1, text=')', padx=18, pady=10, command=lambda: click(')'))
btn_jaja.grid(column=5, row=3)

btn_jojo = Button(window_1, text='(', padx=18, pady=10, command=lambda: click('('))
btn_jojo.grid(column=5, row=2)


window_1.mainloop()
