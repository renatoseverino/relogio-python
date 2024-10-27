'''
AUTOR: RENATO
PROJETO: RELOGIO
VERSÃO: 1.0
'''

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Relógio Digital Python : ")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "#ffd60a")
label.pack(anchor = 'center')
time()

mainloop()