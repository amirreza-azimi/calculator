from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Calculator")

# display_button
display = Entry(root, width=32, borderwidth=1, bg='powder blue', font=('arial', 20, 'bold'), bd=30)
last_button_pressed = None
operation = None
first_number = None

def button_handler(number):
    global last_button_pressed
    if last_button_pressed == "=":
        display.delete(0, END)
        display.insert(0, number)
    else:
        current = display.get()
        display.delete(0, END)
        display.insert(0, current + number)
    last_button_pressed = number

def value_error_decorator(func):
    def dec():
        try:
            func()
        except ValueError as err:
            print(f"Value Error ; {err}")
    return dec

@value_error_decorator
def plus_button_handler():
    # 1: save last number
    global first_number
    global operation
    if first_number is not None:
        first_number =  operator_handler(
            operation=operation,
            first_number=first_number,
            second_number=float(display.get())
        )
    else:
        first_number = float(display.get())
    # 2: clean the display
    display.delete(0, END)
    global last_button_pressed
    last_button_pressed = "+"
    operation = "+"

@value_error_decorator
def subtract_button_handler():
    # 1: save last number
    global first_number
    global operation
    if first_number is not None:
        first_number =  operator_handler(
            operation=operation,
            first_number=first_number,
            second_number=float(display.get())
        )
    else:
        first_number = float(display.get())
    # 2: clean the display
    display.delete(0, END)
    global last_button_pressed
    last_button_pressed = "-"
    operation = "-"

@value_error_decorator
def dev_button_handler():
    global first_number
    global operation
    if first_number is not None:
        first_number =  operator_handler(
        operation=operation,
        first_number=first_number,
        second_number=float(display.get())
        )
    else:
        first_number = float(display.get())
    display.delete(0, END)
    global last_button_pressed
    last_button_pressed = "/"
    operation = "/"
    

@value_error_decorator
def multiply_button_handler():
    global first_number
    global operation
    if first_number is not None:
        first_number =  operator_handler(
            operation=operation,
            first_number=first_number,
            second_number=float(display.get())
        )
    else:
        first_number = float(display.get())
    # 2: clean the display
    display.delete(0, END)
    global last_button_pressed
    last_button_pressed = "x"
    operation = "x"

def operator_handler(operation, first_number, second_number):
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "/":
        result = first_number / second_number
    elif operation == "x":
        result = first_number * second_number
    return result

def equal_handler():
    # 1: get current number
    global first_number
    global operation
    current_number = float(display.get())
    # 2: clean the display
    display.delete(0, END)
    # 3: display the result
    if operation == "+":
        result = first_number + current_number
    elif operation == "-":
        result = first_number - current_number
    elif operation == "/":
        result = first_number / current_number
    elif operation == "x":
        result = first_number * current_number
    display.insert(0, str(result))
    global last_button_pressed
    last_button_pressed = "="
    first_number = None


def display_cleaner_button_handler():
    display.delete(0, END)
# number buttons
number_7_button = Button(root, text="7", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("7"))
number_8_button = Button(root, text="8", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("8"))
number_9_button = Button(root, text="9", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("9"))
number_4_button = Button(root, text="4", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("4"))
number_5_button = Button(root, text="5", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("5"))
number_6_button = Button(root, text="6", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("6"))
number_1_button = Button(root, text="1", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("1"))
number_2_button = Button(root, text="2", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("2"))
number_3_button = Button(root, text="3", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("3"))
number_0_button = Button(root, text="0", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=lambda : button_handler("0"))

equal_button = Button(root, text="=", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command= equal_handler)

add_button = Button(root, text="+", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command= plus_button_handler)
display_cleaner_button = Button(root, text="C", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command= display_cleaner_button_handler)

dev_button = Button(root, text="/", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=dev_button_handler)
subtract_button = Button(root, text="-", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=subtract_button_handler)
multiply_button = Button(root, text="x", padx=40, pady=20, font=('arial', 20, 'bold'), bd=10, command=multiply_button_handler)

# display
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# numbers
number_7_button.grid(row=1, column=0)
number_8_button.grid(row=1, column=1)
number_9_button.grid(row=1, column=2)
number_4_button.grid(row=2, column=0)
number_5_button.grid(row=2, column=1)
number_6_button.grid(row=2, column=2)
number_1_button.grid(row=3, column=0)
number_2_button.grid(row=3, column=1)
number_3_button.grid(row=3, column=2)
number_0_button.grid(row=4,column=0)

# equal button
equal_button.grid(row=4, column=2)

add_button.grid(row=1, column=3)
display_cleaner_button.grid(row=4, column=1)
dev_button.grid(row=4, column=3)
subtract_button.grid(row=2, column=3)
multiply_button.grid(row=3, column=3)

root.mainloop()