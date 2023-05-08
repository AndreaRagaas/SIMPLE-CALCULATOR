#creating the functions
#the function to add two numbers
def add(x, y):
    return x + y

#the function to subtract two numbers
def add(x, y):
    return x - y

#the function to multiply two numbers
def add(x, y):
    return x * y

#the function to divide two numbers
def add(x, y):
    return x / y

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