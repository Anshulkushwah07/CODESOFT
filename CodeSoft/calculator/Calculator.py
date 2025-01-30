import tkinter as tk

calculation = ""

def add_to_calcu(symbol):
    global calculation
    calculation += str(symbol)
    text_res.delete(1.0, "end")
    text_res.insert(1.0, calculation)

def evl_calcu():
    global calculation
    try:
        calculation =  str(eval(calculation))
        text_res.delete(1.0, "end")
        text_res.insert(1.0, calculation)

    except:
        clear_calcu()
        text_res.insert(1.0, 'Error')

def clear_calcu():
    global calculation
    calculation = ""
    text_res.delete(1.0, 'end')

root = tk.Tk()
root.geometry("330x300")
text_res = tk.Text(root, height=2, width=20, font=("Arial", 22))
text_res.grid(columnspan=6)

button_1 = tk.Button(root, text="1", command=lambda: add_to_calcu(1), width=4, font=("Arial", 15))
button_1.grid(row=2, column=1)
button_2 = tk.Button(root, text="2", command=lambda: add_to_calcu(2), width=4, font=("Arial", 15))
button_2.grid(row=2, column=2)
button_3 = tk.Button(root, text="3", command=lambda: add_to_calcu(3), width=4, font=("Arial", 15))
button_3.grid(row=2, column=3)
button_4 = tk.Button(root, text="4", command=lambda: add_to_calcu(4), width=4, font=("Arial", 15))
button_4.grid(row=3, column=1)
button_5 = tk.Button(root, text="5", command=lambda: add_to_calcu(5), width=4, font=("Arial", 15))
button_5.grid(row=3, column=2)
button_6 = tk.Button(root, text="6", command=lambda: add_to_calcu(6), width=4, font=("Arial", 15))
button_6.grid(row=3, column=3)
button_7 = tk.Button(root, text="7", command=lambda: add_to_calcu(7), width=4, font=("Arial", 15))
button_7.grid(row=4, column=1)
button_8 = tk.Button(root, text="8", command=lambda: add_to_calcu(8), width=4, font=("Arial", 15))
button_8.grid(row=4, column=2)
button_9 = tk.Button(root, text="9", command=lambda: add_to_calcu(9), width=4, font=("Arial", 15))
button_9.grid(row=4, column=3)

button_0 = tk.Button(root, text="0", command=lambda: add_to_calcu(0), width=4, font=("Arial", 15))
button_0.grid(row=5, column=2)

button_pl = tk.Button(root, text="+", command=lambda: add_to_calcu("+"), width=4, font=("Arial", 15))
button_pl.grid(row=2, column=4)
button_min = tk.Button(root, text="-", command=lambda: add_to_calcu("-"), width=4, font=("Arial", 15))
button_min.grid(row=3, column=4)
button_mul = tk.Button(root, text="*", command=lambda: add_to_calcu("*"), width=4, font=("Arial", 15))
button_mul.grid(row=4, column=4)
button_div = tk.Button(root, text="/", command=lambda: add_to_calcu("/"), width=4, font=("Arial", 15))
button_div.grid(row=5, column=4)

button_op = tk.Button(root, text="(", command=lambda: add_to_calcu("("), width=4, font=("Arial", 15))
button_op.grid(row=5, column=1)
button_clo = tk.Button(root, text=")", command=lambda: add_to_calcu(")"), width=4, font=("Arial", 15))
button_clo.grid(row=5, column=3)

button_cle = tk.Button(root, text="AC", command=clear_calcu, width=10, font=("Arial", 15))
button_cle.grid(row=6, column=1, columnspan=2)
button_equ = tk.Button(root, text="=", command=evl_calcu, width=10, font=("Arial", 15))
button_equ.grid(row=6, column=3, columnspan=2)


root.mainloop()
