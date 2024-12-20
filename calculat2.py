# define the function
def expo(num1, num2):
    return num1 ** num2



def add(num1, num2):
    return num1 + num2



def floor(num1, num2):
    if num2 == 0:
        return "Error can't  be divisible by zero"
    else:
        return num1 // num2


def modulus(num1, num2):
    return num1 % num2


choice = input("Enter between 1- 4: ")

num1 = int(input("Enter first number:  "))
num2 = int(input("Enter second number: "))

if choice == "1":
    print(f"the result of expo:{expo(num1,num2)}")
elif choice == "2":
    print(f"the result of floor- division:{floor(num1, num2)}")
elif choice == "3":
    print(f"the result of modulus: {modulus(num1,num2)}")
elif choice == "4":
    print(f"the result of add: {add(num1,num2)}")
else:
    print("invalid choice of calculator")

