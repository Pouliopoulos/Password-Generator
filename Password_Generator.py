from random import choice
from tkinter import *
import requests
from tkinter.ttk import Combobox



root = Tk()
root.title("Best p@S$wOrD GenERat0r 0nG")

var = IntVar()
root.title("Random Password Generator")

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()"

def generate():
    entry.delete(0,END)
    pass_type = var.get()
    lenght = int(combo.get())

    password = ''


    if pass_type == 1:
        c = letters
    elif pass_type == 2:
        c = letters + numbers
    elif pass_type == 3:
        c = letters + numbers + symbols

    for i in range(lenght):
        character = choice(c)
        password += character
    entry.insert(0,password)

Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)


generate_button = Button(root, text="Generate",command = generate)
generate_button.grid(row=0, column=3)
lenghtlbl = Label (root,text = "Password Lenght")
lenghtlbl.grid(row = 1,column = 1)
lowrbt=Radiobutton(root,text = "Low",variable=var,value = 1)
lowrbt.grid(row=1, column=3)
medrbt=Radiobutton(root,text = "Medium",variabl =var,value = 2)
medrbt.grid(row=1, column= 4)
strrbt = Radiobutton(root,text = "Strong",variable=var,value = 3)
strrbt.grid(row = 1,column = 5)
combo = Combobox(root)
combo['values'] = (8,10,12,14,16)
combo.grid(column=2, row=1)

print(choice(letters))

root.mainloop()