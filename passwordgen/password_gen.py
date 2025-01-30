from tkinter import  *
import random
import string
import PySimpleGUI as sg

u = random.sample(string.ascii_uppercase,2)
l = random.sample(string.ascii_lowercase,2)
dig = random.sample(string.digits,2)
sym = random.sample(string.punctuation,2)

t = u+l+dig+sym
t = random.sample(t,len(t))
t = "".join(t)
print(t)

sg.set_options(font="verdana 15")

layout = [
    [sg.Text("Uppercase: "), sg.Push(), sg.Input(size=15, key="-U-")],
    [sg.Text("Lowercase: "), sg.Push(), sg.Input(size=15,key="-L-")],
    [sg.Text("Digits: "), sg.Push(), sg.Input(size=15, key="-Dig-")],
    [sg.Text("Symbols: "), sg.Push(), sg.Input(size=15, key="-Sym-")],
    [sg.Button("Ok"), sg.Button("Cencel")],
    [sg.Text("Password"), sg.Push(), 
    sg.Multiline(size=15, disabled=True, key="-Pass-")]
]

win = sg.Window('Password Generator', layout)

while True:
    event, values = win.read()
    if event == "cancel" or event == sg.WIN_CLOSED:
        break
    
    if event == "Ok":
        try:
            u_upper = int(values["-U-"])
            u = random.sample(string.ascii_uppercase, u_upper)
            u_lower = int(values["-L-"])
            l = random.sample(string.ascii_lowercase, u_lower)
            u_digits = int(values["-Dig-"])
            dig = random.sample(string.digits, u_digits)
            u_symbols = int(values["-Sym-"])
            sym = random.sample(string.punctuation, u_symbols)

            t = u+l+dig+sym
            t = random.sample(t,len(t))
            t = "".join(t)
            win["-Pass-"].update(t)
        except ValueError:
            win["-Pass-"].update("No Valid Number")
            
win.close()
