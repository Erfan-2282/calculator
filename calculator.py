import tkinter as tk


root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="black")
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)


calc_display = tk.Entry(root, width=30, bg="gray10",
                        fg="dodger blue", borderwidth=2)
calc_display.grid(row=0, column=0, columnspan=4,
                  ipady=4, ipadx=54, padx=2, pady=2, sticky="ew")
calc_display.bind("<Key>", lambda e: "break")


def append_to_display(value):
    if calc_display.get() == "Error":
        calc_display.delete(0, tk.END)
    calc_display.insert(tk.END, value)


def calculate_result():
    try:
        result = eval(calc_display.get())
    except Exception:
        result = "Error"
    calc_display.delete(0, tk.END)
    calc_display.insert(0, result)


btn_1 = tk.Button(root, text="1", padx=25, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(1))
btn_2 = tk.Button(root, text="2", padx=25, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(2))
btn_3 = tk.Button(root, text="3", padx=25, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(3))
btn_4 = tk.Button(root, text="4", padx=25, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(4))
btn_5 = tk.Button(root, text="5", padx=25, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(5))
btn_6 = tk.Button(root, text="6", padx=25, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(6))
btn_7 = tk.Button(root, text="7", padx=25, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(7))
btn_8 = tk.Button(root, text="8", padx=25, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(8))
btn_9 = tk.Button(root, text="9", padx=25, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(9))
btn_0 = tk.Button(root, text="0", padx=50, pady=15, bg="gray10",
                  fg="dodger blue", command=lambda: append_to_display(0))
btn_add = tk.Button(root, text="+", padx=25, pady=15, bg="gray10",
                    fg="dodger blue", command=lambda: append_to_display("+"))
btn_subtract = tk.Button(root, text="-", padx=25, pady=15, bg="gray10",
                         fg="dodger blue", command=lambda: append_to_display("-"))
btn_multiply = tk.Button(root, text="×", padx=25, pady=15, bg="gray10",
                         fg="dodger blue", command=lambda: append_to_display("*"))
btn_divide = tk.Button(root, text="÷", padx=25, pady=15, bg="gray10",
                       fg="dodger blue", command=lambda: append_to_display("/"))
btn_decimal = tk.Button(root, text=".", padx=25, pady=15, bg="gray10",
                        fg="dodger blue", command=lambda: append_to_display("."))
btn_clear = tk.Button(root, text="C", padx=25, pady=15, bg="gray10",
                      fg="dodger blue", command=lambda: calc_display.delete(0, tk.END))
btn_backspace = tk.Button(root, text="BS", padx=25, pady=15, bg="gray10", fg="dodger blue",
                          command=lambda: calc_display.delete(len(calc_display.get())-1, tk.END))
btn_equal = tk.Button(root, text="=", padx=25, pady=15,
                      bg="gray10", fg="dodger blue", command=calculate_result)


btn_backspace.grid(row=1, column=3, sticky="nsew",
                   padx=2, pady=2, columnspan=1)
btn_multiply.grid(row=1, column=2, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_divide.grid(row=1, column=1, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_clear.grid(row=1, column=0, sticky="nsew", padx=2, pady=2, columnspan=1)

btn_subtract.grid(row=2, column=3, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_9.grid(row=2, column=2, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_8.grid(row=2, column=1, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_7.grid(row=2, column=0, sticky="nsew", padx=2, pady=2, columnspan=1)

btn_add.grid(row=3, column=3, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_6.grid(row=3, column=2, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_5.grid(row=3, column=1, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_4.grid(row=3, column=0, sticky="nsew", padx=2, pady=2, columnspan=1)

btn_equal.grid(row=4, column=3, sticky="nsew", padx=2,
               pady=2, columnspan=1, rowspan=2)
btn_3.grid(row=4, column=2, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_2.grid(row=4, column=1, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_1.grid(row=4, column=0, sticky="nsew", padx=2, pady=2, columnspan=1)

btn_decimal.grid(row=5, column=2, sticky="nsew", padx=2, pady=2, columnspan=1)
btn_0.grid(row=5, column=0, sticky="nsew", padx=2, pady=2, columnspan=2)


root.mainloop()
