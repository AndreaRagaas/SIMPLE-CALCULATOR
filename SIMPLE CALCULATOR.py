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

#creating options
print("CHOOSE AN OPERATION")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

#creating an area to put the option
while True:
    # take input from the user
    choice = input("Enter the choosen operation : ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        # check if user wants to try again
        # exit if the answer is no
        try_again = input("Let's do next calculation? (yes/no): ")
        if try_again == "no":
            #display thank you message
            print("Thank You!")
            break
          
    else:
        print("Invalid Input")
