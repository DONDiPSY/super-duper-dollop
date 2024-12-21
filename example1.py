# this is a comment.
if 5 > 2:
    print("five is greater than two!")
z = "sally"
x = 5
y = "john"
print(x)
print(y)
print(z)

# the variable type int used in the process is called casting
z = int(3)
print(z)
x = 5
y = "john"
print(type(x))
print(type(y))

# many variables to multiple values
x, y, z = "orange", "Banana", "cherry"
print(x)
print(y)
print(z)

# multiple variable to one value
x = y = z = "orange"
print(x)
print(y)
print(z)

# unpack a collection
# extracting values into variable
fruits = ["mango", "watermelon", "garden egg"]
x, y, z = fruits
print(x)
print(y)
print(z)

# the python print() function is often used to output variables.
# print() function
x = "python"
y = "is"
z = "awesome"
j = 50
k = 10
# the best way to output multiple variable in the print() function
# is to separate them with commas
print(x)
print(x + y + z)
print(x, y, z)
print(x, j)
print(j + k)

# Global variables: it can be created outside function
# this variable is created outside a function, it can be use inside
# or outside a function
x = "awesome"


def myfunc():
    print("python is " + x)


myfunc()

# create a variable inside a function ,
# with the same name as the global variable
x = "awesome"


def myfunc():
    x = "fantastic"
    print("python is " + x)


myfunc()
print("python is " + x)


# global keyword(Gk)is used to create a global variable
# inside  a function
def myfunc():
    global x
    x = "cool"


myfunc()
print("python is " + x)

# GK is used to change the value of global variable inside a function
x = "interesting"


def myfunc():
    global x
    x = "easy"


myfunc()
print("python is " + x)

# Data type:
# getting the data type by using type()function
x = 5  # int
y = "Hello World"  # string
z = 20.5  # float
k = 1j  # complex
u = ["apple", "banana", "cherry"]  # list
a = ("apple", "banana", "cherry")  # tuple
b = range(6)  # range
c = {"name": "john", "age": 36}  # dictionary
d = {"apple", "banana", "cherry"}  # set
e = frozenset({"apple", "banana", "cherry"})  # frozenset
f = True  # boolean
g = b"Hello"  # byte
h = bytearray(5)  # bytearray
i = memoryview(bytes(5))  # memory-view
j = None  # None-type

print(type(x))
print(type(y))
print(type(z))
print(type(k))
print(type(u))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))

# conversion from one type to another with float ,int and complex
x = 1
y = 2.8
z = 1j

# convert from int literal to float number
a = float(x)
# convert from float literal to int number
b = int(y)
# convert from int literal to complex number
c = complex(x)

print(a)
print(b)
print(c)

# To print the function type()
print(type(a))
print(type(b))
print(type(c))

#  Random Number
import random

print(random.randrange(1, 10))

# Python String
# Quotes Inside Quotes
print("He is called 'johnny'")
print("It's alright")

# Assign String to Variable
a = "Hello"
print(a)

# Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String are Arrays
# to access the element of a string
a = "Hello ,world!"
print(a[1])

# looping Through a String
# loop through the letter in word "banana"
for x in "banana":
    print(x)

# String Length
# To get the length of a string use the len() function
a = "Hello, World!"
print(len(a))

# check String
# to check if a certain phrase or character is
# present in a string we can use the keyword "in"
txt = "The best things in life are free!"
print("free" in txt)

# the keyword "in" can also be use in an if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("yes, 'free' is present.")

# to check if a certain phrase or character is not
#  present in a string we can use the keyword " not in"
txt = "The best things in life are free!"
print("expensive" not in txt)

# the keyword "not in" can also be use in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is not present.")

# python - slicing strings
# it will print the range from character 2,
# 3, 4 . but it won't print 5
b = "Hello, World!"
print(b[2:5])

# slice from the Start
# the range will start from the first character
b = "Hello, World!"
print(b[:5])

# slice from the end
# the range will go to end
b = "Hello, World!"
print(b[2:])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
print(b[-8:-4])
print(b[-12:-7])

# Python - Modify Strings
# Upper-Case
a = "Hello, World!"
print(a.upper())

# Lower-Case
a = "Hello, World!"
print(a.lower())

# Remove White-Space
a = "  Hello, World! "
print(a.strip())

# Replace() method replace a string
# with another string
a = "Hello, World!"
print(a.replace("H", "J"))

# Split()
# it split the string into substrings
# if it finds an instance of separator ','
a = "Hello, World!"
print(a.split(","))

# Python String Concatenation
# combine two strings use the "+" operator
a = "Hello"
b = "World"
c = a + b
# to add a space between them
d = a + " " + b
print(c)
print(d)

# python format-string: f-string
# in py you can not combine string and number
# but it possible with f-string
# place-holder = {} can contain a variable,
# operation, function and modifiers to
# format a value
age = 36
txt = f"My name is John, I am {age} years "
print(txt)

# modifier
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59:.2f} dollars"
print(txt)


# placeholder containing a function


def myfunc(date):
    return f"i'm {date} years of age"


result = myfunc(28)
print(result)


def display_message(name):
    """Displays a greeting message."""
    # Placeholder for future logic
    placeholder_result = None  # This is a placeholder variable
    print(f"Hello, {name}! Your request is being processed.")
    print("Functionality to handle your request will be implemented soon.")
    return placeholder_result  # Return the placeholder


# Example of calling the function
result = display_message("Alice")
print(result)  # Output: None (since it's a placeholder)

# Escape character
txt = "We are the so-called \"Viking\" from the north."
print(txt)

txt = 'It\'s alright.'
print(txt)

# \\ backslash
txt = "This will insert one \\ (backslash)"
print(txt)

# \n new line
txt = "Hello\nWorld!"
print(txt)

# \r carriage Return
txt = "Hello\rWorld!"
print(txt)

# \t tab
txt = "Hello\tWorld!"
print(txt)

# \b backspace
txt = " Hello World!\b"
print(txt)

# A backslash followed by three integers
# will result in an octal value:
txt = "\110\145\154\154\157"
print(txt)

# A backslash followed by an 'x' and
# a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# String Method
# check string method note on your desktop

# Boolean Value
print(10 > 8)
print(10 == 9)
print(10 < 9)
# print a message based on whether the condition
# true or false
a = 200
b = 33

if b > a:
    print("b is greater than a")

else:
    print("b is not greater than a")
# The bool() function allows you to evaluate any value
# and give you true or false in return
print(bool("Hello"))
print(bool(15))
# the bool() function allows you to evaluate variable
x = "Hello"
y = 54
print(bool(x))
print(bool(y))


# you can execute code based on the boolean answer
# of a function
# Print 'Yes!',if the function returns True,otherwise print"No!"
def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")


# using an object made from a class that is
# evaluated to false
class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))

# python have a built-in function that return a
# boolean value isinstance() function which is used
# to determine if an object is of a certain data type
x = 200
y = "Hello"
print(isinstance(x, int))
print(isinstance(y, str))

# Arithmetic operators
# floor division
# the floor division // rounds the result down
# to the nearest whole number
x = 15
y = 2

print(x // y)

z = 10
y = 6
x = 5
x += 3
y -= 4
z **= 6
print(y)
print(x)
print(z)
# Assignment operators
# bitwise and &=
v = 5
v &= 3
# bitwise or |=
u = 5
u |= 4

print(v)
print(u)

# bitwise XOR ^=
a = 5
a ^= 3
print(a)

# XOR can be use for toggle the
# second bit  of  a number
# 1<<1 perform a left shift and shift the binary reps
# to right by 1 position
num = 5
num ^= (1 << 1)
print(num)

# XOR can be use for swapping values
a = 10
b = 5
a ^= b
b ^= a
print(a)
print(b)

#  Finding the Unique Element in a List
# In a list where every element appears
# twice except for one, you can use XOR
# to find the unique element efficiently.
# any number XORed with itself is 0
# any number XORed with 0 remains unchanged
numbers = [4, 1, 2, 1, 2]
unique_number = 0
for num in numbers:
    unique_number ^= num

print(unique_number)

# Rightshift Assignment operator
# Initial value
# In binary: 10000
a = 16
# Using >>= operator to shift right by 2 bits
# mean removing 2 bit from the right adding to left
# Equivalent to a = a >> 2
a >>= 2
# Output: 4 (00100)
print(a)

# Leftshift Assignment operator
# Initial value
# In binary: 0000 0011
a = 3

# Using <<= operator to shift left by 2 bits3
# mean adding 2 zero to right
# Equivalent to a = a << 2
a <<= 2

print(a)

# Walrus Operator or Assignment expression :=
# it used to assign and use a value in a single line
# 10 and 5 is assign to n and f respectively
# it is used to print out the statement
if (n := 10) > (f := 5):
    print(f"n is {n} and greater than f which is {f}")

# Walrus Operator is used in Loop
# when reading from a file or processing items
# until a certain condition is met
# It gets user input and saves it in the variable line.
# It checks if that input is not equal to 'exit'
while (line := input("Enter a line(or 'exit' to quit): ")) != 'exit':
    print(f"you entered: {line}")

# the comment below show the code above without walrus operator
# line = input("Enter a line (or 'exit' to quit): ")
# while line != 'exit':
#    print(f"You entered: {line}")
#    line = input("Enter a line (or 'exit' to quit): ")
