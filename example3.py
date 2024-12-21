# python Inheritance: it allows us to define a class
# that inherits all the method and properties from
# another class
# parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# child class

class Student(Person):
    pass


x = Student("Adedolapo", "Ayodeji")
x.printname()


# Add the __init__()Function
# super(): inherit the method and
# properties from its parent class


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# child class

class Student(Person):
    def __init__(self, fname, mname, lname):
        super().__init__(fname, lname)
        self.middlename = mname

    def name(self):
        print(self.firstname, self.middlename, self.lastname)


x = Student("Adedolapo", "Ayodeji", "Raheem")
x.name()

# iterator is an object that contain
# a countable numbers of values
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# strings are iterable object
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# create an iterator


class mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


# class polymorphism
# multiple class with the same method
# where the same method behaves differently
# based on the object that is called
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive")


class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail")


class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")


car1 = car("Ford", "Mustang")
boat1 = boat("Ibiza", "Touring 20")
plane1 = plane("Boeing", "747")

print(car1.brand)

for x in (car1, boat1, plane1):
    x.move()


# inheritance class polymorphism
# This is a subclass inherited from
# a superclass with the same method
# but can override them
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move")


class car(Vehicle):
    def move(self):
        print("drive")


class boat(Vehicle):
    def move(self):
        print("sail")


class plane(Vehicle):
    def move(self):
        print("fly")


car1 = car("Toyota", "Camry")
boat1 = boat("Lambo", "Runner20")
plane1 = plane("Jet20", "Bomb-fly")

for x in (car1, boat1, plane1):
    print(x.brand, ": ", x.model)
    x.move()


    class Animal:
        def speak(self):
            print("The animal makes a sound.")


    class Dog(Animal):
        def speak(self):
            print("The dog barks.")


    class Cat(Animal):
        def speak(self):
            print("The cat meows.")

# Creating instances
animal = Animal()
dog = Dog()
cat = Cat()

# Calling overridden methods
animal.speak()  # Outputs: The animal makes a sound.
dog.speak()  # Outputs: The dog barks.
cat.speak()  # Outputs: The cat meows.


# python scope: It is a variable that is only
# available from inside the region it is created

# Local scope : It is a variable created inside a function,
# and can only be used inside that function

def myfunc():
    x = 200
    print(x)


myfunc()


# function inside function

def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

# Global Scope: it also called the global variable
# it can be used within or outside a scope
x = 400


def myfunc():
    print(x)


myfunc()

print(x)

# Naming Variable

x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)

# global keyword
x = 200


def myfunc():
    global x
    x = 500


myfunc()
print(x)


# nonlocal keyword
def myfunc1():
    x = "jane"

    def myfunc2():
        nonlocal x
        x = "hello, my name is jane"

    myfunc2()
    return x


print(myfunc1())

# python modules
# A file containing a set of function
# you want to include in your application

import mymodule

mymodule.greeting("John")

# variable in Modules
a = mymodule.person1["name"]
print(a)

# Re-naming a module
# you can create an alias when you import a module
# by using the as keyword
import mymodule as mx

a = mx.person1["country"]
print(a)

# built-in Modules
import platform

x = platform.system()
print(x)

x = dir(mymodule)
print(x)

# from keyword is used to import part from a module
from mymodule import person1

print(person1["age"])

# python dates
import datetime

x = datetime.datetime.now()
print(x)
print(x.day)
# this is used to print the name of day of the week
print(x.strftime("%A"))

# creating date objects
x = datetime.datetime(2025, 3, 10)
print(x)
print(x.strftime("%A"))
print(x.strftime("%B"))

# Python Math
# built-in Math Function
x = min(5, 10, 12, 2)
y = max(5, 10, 12, 2)

print(x)
print(y)

# absolute function  returns positive value
# of specified number
x = abs(-7.25)
print(x)

# pow(x, y)
x = pow(4, 3)
print(x)

# the math module
import math

x = math.sqrt(64)
y = math.ceil(1.4)
z = math.floor(1.4)
k = math.pi
print(x)
print(y)
print(z)
print(k)

# python json

import json

x = '{"name": "john", "age" : 30, "city": "New york"}'

# parse : convert json to python
y = json.loads(x)

print(y["city"])

x = {
    "name": "john",
    "age": 30,
    "city": "New york"
}
# convert from python to json
y = json.dumps(x)
print(y)

x = {
    "name": "john",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pet": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]

}

# format the result: the json.dumps() has parameter to
# make it easier to read the result
# print(json.dumps(x, indent=2))
# print(json.dumps(x, indent=4, separators=(".", "=")))

# order the result
print(json.dumps(x, indent=4, sort_keys=True))

# Regular Expression: it can be used to check
# if a string contains the specified search pattern

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
if x:
    print("Yes! We have a match!")
else:
    print("No Match!")

x = re.findall("[a-g]", txt)
print(x)

txt = "Believe in The God, All Thing Are Possible "
x = re.findall("[a-zA-z]", txt)
y = re.search("[^Believe]", txt)
z = re.split("\s", txt)
k = re.split("\s", txt, 1)
j = re.sub("\s", "-", txt, 2)
print(x)
if x:
    print("Grateful soul")
else:
    print("you should have trust God")
print(y)
print(z)
print(k)
print(j)

import camelcase

c = camelcase.CamelCase()

txt = "hello world"
print(c.hump(txt))

# try-expect
try:
    print(x)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demo.txt")
    try:
        f.write("lorum Ipsum")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


def fer(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Temperature in  celsius: {celsius:.2f}")


def cel(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Temperature in fahrenheit : {fahrenheit:.2f}")


temp = input("please choose an option: ")

try:
    if temp == "1":
        fc = input("fahrenheit: ")
        fer(int(fc))
    elif temp == "2":
        cf = input("Celsius: ")
        cel(int(cf))
    else:
        print("it looks like you input a a value that wasn't 1 or 2!")

# something is wrong here
except ValueError:
    print("It looks like you input a value that wasn't a number!")

# raise an exception
x = int(input("input number: "))
if x < 0:
    raise x
    print(x)
else:
    print(f"you entered: {x}")

# User Input
username = input("Enter username: ")
print("Username is : " + username)

# file handling
# open a file
x = open("demo.txt")
print(x.read())

# Read line: you can return one line by
# using the readline() method
print(x.readline())
x.close()

# write to an existing file
f = open("demo.txt", "a")
f.write("Now the file has more content")
f.close()
# open and read the file after the appending
f = open("demo.txt", "r")
print(f.read())

# open and overwrite the file
f = open("demo.txt", "w")
f.write("Hello Dondipsy , Jummat Mubarak")
f.close()
# open and read the file after overwrite
f = open("demo.txt", "r")
print(f.read())

# check if file exist
# to delete a file
import os
if os.path.exists("demofile.txt"):
    os.remove("demo.txt")
else:
    print("the file does not exist")
