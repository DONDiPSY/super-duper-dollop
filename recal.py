# define the function
def Add(num1, num2):
    return num1 + num2


def Subtract(num1, num2):
    return num1 - num2


def Multiply(num1, num2):
    return num1 * num2


def Divide(num1,num2):
    if num2 == 0:
        return "Error!, cannot be divided by zero"
    else:
        num1 / num2


# Available selection
print("Select operation")
print("1 is for Add")
print("2 is for Subtract")
print("3 is for Multiply")
print("4 is for Divide")

# take user input for operation choice
choice = input("Enter (1 / 2 / 3 / 4 ): ")

# get the input from the user
num1 = int(input("Enter first number:  "))
num2 = int(input("Enter second number:  "))

# perform operation base on the user choice
if choice == "1":
    print(f" The result for Addition: {Add(num1, num2)}")

elif choice == "2":
    print(f" The result for Subtraction: {Subtract(num1, num2)}")

elif choice == "3":
    print(f" The result for Multiply: {Multiply(num1, num2)}")

elif choice == "4":
    print(f" The result for Division: {Divide(num1, num2)}")

else:
    print("Invalid Operation")