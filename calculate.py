# define the function for each operation
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."

    else:
        return num1 / num2


# display the available operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# take user input for operation choice
choice = input("Enter choice (1 / 2 / 3 / 4): ")

#get input number from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# perform the operation based on the user's choice
if choice == "1":
    print(f"The result is : {add(num1, num2)}")

elif choice == "2":
    print(f"The result is : {subtract(num1, num2)}")

elif choice == "3":
    print(f"The result is : {multiply(num1, num2)}")

elif choice == "4":
    print(f"The result is : {divide(num1, num2)}")

else:
    print("Invalid input")