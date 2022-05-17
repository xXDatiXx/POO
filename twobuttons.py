from tkinter import *
from tkinter.ttk import *

bandA = False
bandB = False


class NewWindow(Toplevel):
    def __init__(self, master=None):
        global bandA
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text="This is a new Window for A")
        label.pack()


class NewWindowB(Toplevel):
    def __init__(self, master=None):
        global bandB
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text="This is a new Window for B")
        label.pack()


def on_win_request(parent, a):
    global bandA, bandB
    #dialog = Toplevel()
    if bandA == False and a == 1:
        bandA = True
        parent.wait_window(NewWindow(master))
        bandA = False

    if bandB == False and a == 2:
        bandB = True
        parent.wait_window(NewWindowB(master))
        bandB = False
#https://stackoverflow.com/questions/28388346/what-does-thewait-window-method-do
# De aquí aprendí wait_window

master = Tk()
master.geometry("200x200")
label = Label(master, text="This is the main window")
label.pack(side=TOP, pady=10)


btn = Button(master,
             text="Botton A")
btnB = Button(master,
              text='Botton B')
btn.bind("<Button>",
         lambda e: on_win_request(master, 1))
btnB.bind('<Button>',
          lambda e: on_win_request(master, 2))

btn.pack(pady=15)
btnB.pack(pady=10)
mainloop()
