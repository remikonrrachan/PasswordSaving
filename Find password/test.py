import tkinter as tk
import pyperclip
from tkinter import RIGHT,CENTER,OUTSIDE
def COPYPASS(*args):
    keyword=str(Character_input.get())
    f = open('D:\password(remake).txt', 'r')
    while True:
        s = f.readline()
        if s == '':
            break

        d = s.rstrip().split(',')
        word = keyword
        if d[0] == word:
            result = d[2] 
            break
        else:
            result='Do not have you result in database '
    output = ''
    output += result
    #output_label.configure(text=output)
    pyperclip.copy(output)
    f.close()
def COPYID(*args):
    keyword=str(Character_input.get())
    f = open('D:\password(remake).txt', 'r')
    while True:
        s = f.readline()
        if s == '':
            break

        d = s.rstrip().split(',')
        word = keyword
        if d[0] == word:
            result = d[1] 
            break
        else:
            result='Do not have you result in database '
    output = ''
    output += result
    #output_label.configure(text=output)
    pyperclip.copy(output)
    f.close()
def COPY(*args):
    keyword=str(Character_input.get())
    f = open('D:\password(remake).txt', 'r')
    while True:
        s = f.readline()
        if s == '':
            break

        d = s.rstrip().split(',')
        word = keyword
        if d[0] == word:
            result = d[1] + '\n' + d[2]
            break
        else:
            result='Do not have you result in database '
    output = ''
    output += result
    #output_label.configure(text=output)
    pyperclip.copy(output)
    f.close()
def Show_output(*args):
    keyword=str(Character_input.get())
    f = open('D:\password(remake).txt', 'r')
    while True:
        s = f.readline()
        if s == '':
            break

        d = s.rstrip().split(',')
        word = keyword
        if d[0] == word:
            result = 'ID: ' + d[1] + '\n' + 'Password: ' + d[2]
            break
        else:
            result='Do not have you result in database '
    output =''
    output += result
    output_label.configure(text=output)
    f.close()
window=tk.Tk()
window.title('TEST')
window.minsize(width=40,height=300)

title_label = tk.Label(master=window,text='Choose you program you want to see ID&PASSWORD')
title_label.pack(pady=20)

Character_input =tk.Entry(master=window)
Character_input.bind('<Return>',Show_output)
#Character_input.bind('<Return>',CHECK)
Character_input.pack(pady=20)

Search_button = tk.Button(master=window,text='Search',command=Show_output)
Search_button.pack()

output_label=tk.Label(master=window)
output_label.pack(pady=20)

COPYALL_button = tk.Button(master=window,text='Copy',command=COPY)
COPYALL_button.pack()
COPYALL_button.place(x=125,y=250)

COPYID_button = tk.Button(master=window,text='Copy ID',command=COPYID)
COPYID_button.pack()
COPYID_button.place(x=50,y=251)

COPYPASS_button = tk.Button(master=window,text='Copy PASS',command=COPYPASS)
COPYPASS_button.pack()
COPYPASS_button.place(x=187,y=249)
window.mainloop()

