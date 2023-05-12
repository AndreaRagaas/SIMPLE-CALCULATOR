#2022-09805-MN-0
#RAGAAS, ANDREA 
#BSCPE 1-5
#A program that can get the sum, difference, product, and quotient of two numbers.

#importing tkinter
import tkinter as tk

#creating the functions
#the function to add two numbers
def add():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 + num2
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Invalid input, please try again")

#the function to subtract two numbers
def subtract():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 - num2
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Invalid input, please try again")

#the function to multiply two numbers
def multiply():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Invalid input, please try again")

#the function to divide two numbers
def divide():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 / num2
        result_label.config(text=result)
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero")
    except ValueError:
        result_label.config(text="Invalid input, please try again")

#the function to calculate with whatever operation the user will choose
def calculate():
    operation = operation_var.get()
    if operation == "Add":
        add()
    elif operation == "Subtract":
        subtract()
    elif operation == "Multiply":
        multiply()
    elif operation == "Divide":
        divide()

#creating the main window of the calculator
root = tk.Tk()
root.title("SIMPLE CALCULATOR")

# creating the widgets
num1_label = tk.Label(root, text="Enter the first number: ")
num1_entry = tk.Entry(root)
num2_label = tk.Label(root, text="Enter the second number: ")
num2_entry = tk.Entry(root)

operation_var = tk.StringVar(value="Add")
operation_dropdown = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")

calculate_button = tk.Button(root, text="Calculate", command=lambda: [calculate(), ask_again()])
result_label = tk.Label(root, text="Result:")

#creating the layout of the widgets
num1_label.grid(row=0, column=0, sticky="e")
num1_entry.grid(row=0, column=1)
num2_label.grid(row=1, column=0, sticky="e")
num2_entry.grid(row=1, column=1)
operation_dropdown.grid(row=2, column=0, columnspan=2, pady=5)
calculate_button.grid(row=3, column=0, columnspan=2, pady=5)
result_label.grid(row=4, column=0, columnspan=2)
