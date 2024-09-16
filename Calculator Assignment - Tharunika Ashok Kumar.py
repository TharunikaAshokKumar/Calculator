import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")  # Adjust the window size for better layout
root.configure(bg='#f0f0f0')  # Set background color


# Create an entry widget for the display
display = tk.Entry(root, width=18, borderwidth=5, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')


# Create a label for the history
history_label = tk.Label(root, text="", anchor='e', justify='right', font=('Arial', 12), fg='gray', bg='#f0f0f0')
history_label.grid(row=1, column=0, columnspan=4, padx=10, pady=(0, 10))


# Global variables to store the first number, the operation, and history
f_num = 0
math = ""
history = ""


# Function to add numbers to the display
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))


# Function to clear the display
def button_clear():
    global history
    display.delete(0, tk.END)
    history = ""
    history_label.config(text="")


# Function to handle addition
def button_add():
    global f_num
    global math
    global history
    first_number = display.get()
    math = "addition"
    f_num = float(first_number)
    display.delete(0, tk.END)
    history += f"{first_number} + "
    history_label.config(text=history)


# Function to handle subtraction
def button_subtract():
    global f_num
    global math
    global history
    first_number = display.get()
    math = "subtraction"
    f_num = float(first_number)
    display.delete(0, tk.END)
    history += f"{first_number} - "
    history_label.config(text=history)


# Function to handle multiplication
def button_multiply():
    global f_num
    global math
    global history
    first_number = display.get()
    math = "multiplication"
    f_num = float(first_number)
    display.delete(0, tk.END)
    history += f"{first_number} * "
    history_label.config(text=history)


# Function to handle division
def button_divide():
    global f_num
    global math
    global history
    first_number = display.get()
    math = "division"
    f_num = float(first_number)
    display.delete(0, tk.END)
    history += f"{first_number} / "
    history_label.config(text=history)


# Function to perform the calculation
def button_equal():
    global history
    second_number = display.get()
    display.delete(0, tk.END)
    result = 0
    if math == "addition":
        result = f_num + float(second_number)
    elif math == "subtraction":
        result = f_num - float(second_number)
    elif math == "multiplication":
        result = f_num * float(second_number)
    elif math == "division":
        if float(second_number) == 0:
            display.insert(0, "Error")
            history += "Error"
            history_label.config(text=history)
            return
        else:
            result = f_num / float(second_number)

    display.insert(0, str(result))
    history += f"{second_number} = {result}"
    history_label.config(text=history)


# Button styling
button_style = {'padx': 20, 'pady': 20, 'font': ('Arial', 18), 'bg': '#e6e6e6'}


# Create buttons for digits
button_1 = tk.Button(root, text="1", **button_style, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", **button_style, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", **button_style, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", **button_style, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", **button_style, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", **button_style, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", **button_style, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", **button_style, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", **button_style, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", **button_style, command=lambda: button_click(0))


# Create buttons for operations
button_add = tk.Button(root, text="+", **button_style, command=button_add)
button_equal = tk.Button(root, text="=", **button_style, command=button_equal)
button_clear = tk.Button(root, text="Clear", **button_style, command=button_clear)

button_subtract = tk.Button(root, text="-", **button_style, command=button_subtract)
button_multiply = tk.Button(root, text="*", **button_style, command=button_multiply)
button_divide = tk.Button(root, text="/", **button_style, command=button_divide)


# Put the buttons on the screen with correct alignment
button_1.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
button_2.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)
button_3.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)

button_4.grid(row=3, column=0, sticky='nsew', padx=5, pady=5)
button_5.grid(row=3, column=1, sticky='nsew', padx=5, pady=5)
button_6.grid(row=3, column=2, sticky='nsew', padx=5, pady=5)

button_7.grid(row=4, column=0, sticky='nsew', padx=5, pady=5)
button_8.grid(row=4, column=1, sticky='nsew', padx=5, pady=5)
button_9.grid(row=4, column=2, sticky='nsew', padx=5, pady=5)

button_0.grid(row=5, column=0, sticky='nsew', padx=5, pady=5)
button_clear.grid(row=5, column=1, sticky='nsew', padx=5, pady=5)
button_equal.grid(row=5, column=2, sticky='nsew', padx=5, pady=5)

button_add.grid(row=2, column=3, sticky='nsew', padx=5, pady=5)
button_subtract.grid(row=3, column=3, sticky='nsew', padx=5, pady=5)
button_multiply.grid(row=4, column=3, sticky='nsew', padx=5, pady=5)
button_divide.grid(row=5, column=3, sticky='nsew', padx=5, pady=5)


# Adjust column and row configuration to make buttons expand
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(2, 6):
    root.grid_rowconfigure(i, weight=1)


# Run the application
root.mainloop()
