#2022-09805-MN-0
#RAGAAS, ANDREA 
#BSCPE 1-5
#A program that can get the sum, difference, product, and quotient of two numbers.

#importing tkinter
import tkinter as tk

#creating the functions
#the function to add two numbers
def add(num_1, num_2):
    return num_1 + num_2

#the function to subtract two numbers
def subtract(num_1, num_2):
    return num_1 - num_2

#the function to multiply two numbers
def multiply(num_1, num_2):
    return num_1 * num_2

#the function to divide two numbers
def divide(num_1, num_2):
    return num_1 / num_2

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
