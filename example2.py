# Walrus Operator is also used for
# List Comprehension: to filter or manipulate data
data = [1, 2, 3, 4, 5]
squared = [square for x in data if (square := x ** 2) > 5]
print(squared)

# Comparison Operators
x = 5
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators
# and,or,not operator
x = 5
print(3 < x < 10)
print(x < 3 or x < 10)
print(not (x > 3 and x < 10))

# Identity Operator
# is operator: return true if both variable
# are the same
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
# is not operator: return true if both
# variable are not the same
print(x is not z)
print(x is not y)
print(x != y)

# Membership operator
# in: return true if the sequence with specified
# value is present in the object
x = ["apple", "banana"]
print("banana" in x)

# not in: return true if the sequence with
# specified value is not present in the object
x = ["apple", "banana"]
print("Tomatoes" not in x)

# List are used you store multiple
# item in a single variable
this_list = ['apple', 'banana', 'cherry']
print(this_list)
# to determine the length of list
# use the length() function
print(len(this_list))
# to print the type
print(type(this_list))
# List Constructor
# it used to create a new list
your_list = list(('apple', 'banana', 'cherry'))
print(your_list)
# Access item in list
print(this_list[1])
# Negative indexing
print(your_list[-2])
# Range of index
thislist = ['apple', 'mango', 'cherry', 'kiwi', 'melon', 'orange']
print(thislist[2:5])
print(thislist[:5])
print(thislist[2:])
# Range of Negative indexes
print(thislist[-4:-1])
# to check if item exists,used the in keyword
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
# change list item
mylist = ['apple', 'banana', 'cherry']
mylist[1] = 'blackcurrant'
print(mylist)
# change a range of item values
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist)
# change the 2nd value by replacing
# it with two new values
mylist = ["apple", "cherry", "mango"]
mylist[1:2] = ["blackcurrant", "orange"]
print(mylist)
# change the 2nd and 3rd value
# by replacing it with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# insert() method insert an item
# at the specified index
thislist = ["apple", "mango", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append items : to add an item to the end
# of the list, use the append() method
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# Extend list : to extend from another
# list to the current list,use the extend
# () method
this_list = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
this_list.extend(tropical)
print(this_list)

# Add Any iterable
# the extend() method does not have to append list
# you can add any iterable object
# (tuple, set, dictionaries)
this_list = ['apple', 'banana', 'cherry']
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)

# Remove List item :the remove ()
# method removes the specified item
thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)
# Removes the first occurrence
thislist = ['apple', 'banana', 'cherry', 'banana', 'kiwi']
thislist.remove('banana')
print(thislist)

# Remove Specified index
# the pop() method removes
# the specified index
thislist = ['apple', 'banana', 'cherry']
thislist.pop(1)
print(thislist)
# if you don't specify the index it
# would remove the last item
thislist = ['apple', 'banana', 'cherry']
thislist.pop()
print(thislist)

# The del keyword  also removes
# the specified index
thislist = ['apple', 'banana', 'cherry']
del thislist[0]
print(thislist)
# the del keyword can also delete
# the list completely
thislist = ['apple', 'banana', 'cherry']
del thislist

# the clear() method empties the list.
# the list still remains,but it has no content
thislist = ['apple', 'banana', 'cherry']
thislist.clear()
print(thislist)

# Loop Through a list
# by using for loop
thislist = ['apple', 'banana', 'cherry']
for x in thislist:
    print(x)
# Loop Through the index Numbers
# use the range() and len()
thislist = ['apple', 'banana', 'cherry']
for i in range(len(thislist)):
    print(thislist[i])

# loop Through a list
# using while loop
thislist = ['apple', 'banana', 'cherry']
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# list comprehension
# a concise or short syntax
# for looping through lists
thislist = ['apple', 'banana', 'cherry']
[print(x) for x in thislist]

# based on a list of fruits,
# you want a new list, containing only
# the fruits with the letter "a"
# without list comprehension you
# will have to write a for statement
# with a conditional test
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)
# with list comprehension you
# can do all with only one line of code
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']

new_list = [x for x in fruits if "a" in x]

print(new_list)

# List comprehension using a filter, will
# have iterable based on a condition
number = [1, 2, 3, 4, 5, 6]
even_number = [num for num in number if num % 2 == 0]
print(even_number)

new_list = [x for x in range(10) if x < 5]
print(new_list)

# list comprehension using manipulate, will
# control the outcome of the list item in
# the new list which is on the expression
new_list = [x.upper() for x in fruits]
print(new_list)

number = [1, 2, 3, 4, 5, 6]
square_num = [num ** 2 for num in number]
print(square_num)
# it can also contain a condition
# Return the item if banana is not present
# in the list, if it is present return orange.
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
new_list = [x if x != "banana" else 'orange' for x in fruits]

print(new_list)

# sort list alphanumerically,
# ascending, by default
long = ["orange", "mango", "kiwi", "pineapple", "banana"]
short = [100, 50, 30, 65, 10, 82]
short.sort()
long.sort()
print(long)
print(short)
# to sort descending,use the key
# word argument reverse = True
long.sort(reverse=True)
print(long)
short.sort(reverse=True)
print(short)


# Customize Sort Function
# myfunc takes a single argument
def myfunc(n):
    # it cal the absolute difference btw n and 50
    # this means the function will return how far n is from 50
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
# The key parameter is set to myfunc,
# which means that the list will be
# sorted based on the values returned by myfunc
thislist.sort(key=myfunc)
print(thislist)

# List of dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 25},
]


# Custom sort function
def custom_sort(person):
    return person["age"], person["name"]


# Sorting using sorted() with the custom key function
# the sorted() is a built-in-function that returns a new
# sorted list from the elements of any iterable
#  without modifying the original iterable


sorted_people = sorted(people, key=custom_sort)

# Output the sorted list
for person in sorted_people:
    print(f"{person['name']} - Age: {person['age']}")

# sort () is case-sensitive, resulting
# in all cap letter being sorted before
# lower case letter
thislist = ['banana', 'Orange', 'cherry', 'Kiwi']
thislist.sort()
print(thislist)

# so if you want a case-insensitive
# sort function , use the key parameter
# and set it to str.lower
thislist.sort(key=str.lower)
print(thislist)

# reverse() method reverses the
# current sorting order of the element
thislist = ['banana', 'Orange', 'Kiwi', 'cherry']
thislist.reverse()
print(thislist)

# Copy() method is used to copy a list
thislist = ['apple', 'banana', 'cherry']
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use
# the built-in method list()
thislist = ['apple', 'banana', 'cherry']
mylist = list(thislist)
print(mylist)

# you can use the slice operator
# to copy a list
thislist = ['apple', 'banana', 'cherry']
mylist = thislist[:]
print(mylist)

# join two lists together
# you can use the + operator
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# joining two list  by extend
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# joining two list by append
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)

print(list1)

# tuple is a collection which is
# ordered, unchangeable and allow
# duplicate values.
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)

# tuple length : len()
print(len(this_tuple))

# creating a tuple with one item you have to add
# a comma after the item, otherwise python won't
# recognize it as a tuple.
this_tuple = ("apple",)
my_tuple = ("apple", "banana", "cherry")
print(type(this_tuple))
print(type(my_tuple))

# tuple(()) constructor
my_tuple = tuple(("apple", "banana", "cherry"))
print(my_tuple)

# Access tuple items
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])
# Negative indexing
print(my_tuple[-1])
# Range of indexes
this_tuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(this_tuple[2:5])
print(this_tuple[:4])
print(this_tuple[2:])
# Range of negative indexes
print(this_tuple[-4:-1])

# to check if item exists
# use the in keyword
this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
    print("Yes, \"apple\" is in the fruits tuple ")

# you can convert tuple into list,
# and change list,and convert the back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add item
# convert a tuple to a list in other to
# append the list and convert it back to a
# tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

# Add tuple to a tuple
j = ("apple", "banana", "cherry")
k = ("orange",)
j += k
print(j)

# Remove item
# you can't remove an item in a tuple,
# but you can convert to list , then
# remove the list and convert back to a tuple
j = ("apple", "banana", "cherry")
k = list(j)
k.remove("apple")
j = tuple(k)
print(j)

# del keyword delete the tuple completely
j = ("apple", "banana", "cherry")
del j

# unpacking a tuples
# extracting values back into a variables
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using Asterisk(*)
# if the number of variable  is less than
# the number of values, you can add an
# * to the variable name, and the values
# will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(*green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Loop Tuple
# using a for loop
this_tuple = ("apple", "banana", "cherry")
for x in this_tuple:
    print(x)

# Loop Through the index numbers
# using range() and len() function
this_tuple = ("mango", "date", "pawpaw")
for i in range(len(this_tuple)):
    print(this_tuple[i])

# using a while loop
this_tuple = ("cashew", "melon", "grapes")
i = 0
while i < len(this_tuple):
    print(this_tuple[i])
    i = i + 1

# join two tuples
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# multiply Tuples
fruits = ("apple", "banana", "cherry")
my_tuple = fruits * 2
print(my_tuple)

# count() method
print(my_tuple.count("apple"))

# index() method
print(my_tuple.index("banana"))

# Set are used to store multiple item in
# a single variable. A set is unordered,
# unchangeable*, and duplicate is not allowed
this_set = {"apple", "banana", "cherry"}
print(this_set)

# Duplicate is not allowed
this_set = {"apple", "banana", "cherry", "apple"}
print(this_set)

# the values true and 1 are considered
# the same value in a set, are treated as duplicate
this_set = {"apple", "banana", "cherry", True, 2, 1}
print(this_set)

# the value false and 0 are considered the same
# value in a set and are treated as duplicate
this_set = {"apple", "banana", "cherry", False, 0, True}
print(this_set)

# length of set
this_set = {"apple", "banana", "cherry"}
print(len(this_set))

# A set can contain different data types
set1 = {"abc", True, 40}

# type()
this_set = {"apple", "banana", "cherry"}
print(type(this_set))

# set Constructor
this_set = "apple", "banana", "cherry"
my_set = set(this_set)
print(my_set)

# you can't access the index in a set,
# but you can loop through the set item
# using a for loop or ask if specified
# value is present, by using the in keyword
this_set = {"apple", "banana", "cherry"}
if "apple" in this_set:
    print("yes, apple is a fruit")

this_set = {"apple", "banana", "cherry"}
for x in this_set:
    print(x)

this_set = {"apple", "banana", "cherry"}
print("banana" in this_set)

# add set items:once a set  is created,
# you can't change its item, but you can add new items.
# To add one item to a set use the add() method.
this_set = {"apple", "banana", "cherry"}
this_set.add("orange")
print(this_set)

# To add item from another set into the current set
# use the update() method
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "grapes"}
this_set.update(tropical)
print(this_set)

# Add Any Iterable: the object in the update()
# method doesn't have to be a set, it
# can be any iterable object
# (tuples, lists, dictionaries)
this_set = {"apple", "banana", "cherry"}
tropical = ["pineapple", "mango", "grapes"]
this_set.update(tropical)
print(this_set)

# Remove item: to remove an item in a set
# use the remove() or the discard() method
this_set = {"apple", "banana", "cherry"}
this_set.remove("cherry")
print(this_set)

this_set = {"apple", "banana", "cherry"}
this_set.discard("mango")
print(this_set)

# you can also use the pop() method,
# but it will remove at random because a set
# is un-indexed and unordered
this_set = {"apple", "banana", "cherry"}
x = this_set.pop()
print(x)
print(this_set)

# clear() method empties the set
this_set = {"apple", "banana", "cherry"}
this_set.clear()
print(this_set)

# del: it will delete the set completely
this_set = {"apple", "banana", "cherry"}
del this_set

# loop set
# using a for loop
this_set = {"apple", "banana", "cherry"}
for x in this_set:
    print(x)

# using while loop,but you have to convert
# the set to a list before you can access the item
this_set = {"apple", "banana", "cherry"}
i = 0
while i < len(this_set):
    mylist = list(this_set)
    print(mylist[i])
    i = 1 + i

# Join set:
# union() or |   method
# join all item from both set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2  # only possible when joining a set with another set
# set3 = set1.union(set2)
print(set3)

# the update() method insert a
# set into another set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# set1.update(set2)
set1 |= set2  # only possible when joining a set with another set
print(set1)

# join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"john", "elena"}
set4 = {"apple", "banana", "cherry"}
# myset = set1.union(set2, set3, set4)
myset = set1 | set2 | set3 | set4  # only possible when joining a set with a set
print(myset)

# the union ()method allows to join set with
# other data types, but | operator only allows
# to join set with set
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# intersection()method or & will return a
# new set,that only contains the items
# that are present in both sets.
set1 = {"apple", "banana", "cherry", "goggle"}
set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
set3 = set1.intersection(set2)
print(set3)

# intersection_update()method it will change the
# original set in place to keep the common set
#  instead of returning a new set.
set1 = {"apple", "banana", "cherry", "goggle"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
# set1 &= set2 only possible when joining a set with another set
print(set1)

# Join set that contains the values true and 1 are the same
# false and 0  the same using intersection method
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# difference() method or - will return new set
# that will contain only the item from the first
# set that are not present in other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
# set3 = set1 - set2
print(set3)

# difference_update() method after keeping item that
# are in the first set that is not present in other set ,
# it will change the original set instead of returning a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
# set1 -= set2
print(set1)

# Symmetric_difference() method or ^ will keep only the
# element that are not present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
# set3 = set1 ^ set2
print(set3)

# symmetric_difference_update:  it will
# change the original set  instead of
# returning a new set and element that
# are not present in both
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
# set1 ^= set2
print(set1)

# dictionary are used to store data in key and value pairs
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])

# Duplicate is not allowed
# it overwrite existing values if there is duplicate
thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946,
    "year": 2020
}
print(thisdict)
# print length of dictionaries
print(len(thisdict))

# Dictionary items - data types
# the values in dictionary item can be of any data types
# string, int, boolean,and list data types
thisdict = {
    "brand": "ford",
    "electric": False,
    "year": 1946,
    "colors": ["red", "white", "blue"]
}
print(thisdict["colors"])
# types()
print(type(thisdict))

# the dict() constructor
# it is used to create a new dictionaries
thisdict = dict(name="john", age=36, country="Nigeria")
print(thisdict)

# you can access the items of dict
# by referring to its key name
thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
print(thisdict["model"])
x = thisdict["brand"]
print(x)
# you can also use get() method that would
# access the item of dict
x = thisdict.get("year")
print(x)
# the keys() method will return a list of all
# the keys in the dictionary
x = thisdict.keys()
print(x)

# Add a new item to original dictionary
# and  see that the keys list gets updated
car = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

# get values
# the values() method will return a list
# of all the values in the dict
x = car.values()
print(x)

# make a change in original dict,
# and see that the values list get updated
car = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
x = car.values()
print(x)
car["year"] = 2020
print(x)

# Add a new item to original dict,
# and see that the values list gets
# updated as well
x = car.values()
car["color"] = "red"
print(x)

# get items
# the items() method will return each item
# dict ,as tuples in a list
x = car.items()
print(x)
# make change in original dict, and see that
# the items list gets updated as well
car["year"] = 2024
print(x)
# add a new item to original dict and see that the
# items list gets updated as well
car["electric"] = True
print(x)

# to check if a specified key is present in a dict
# use the in keyword
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
if "model" in motors:
    print("yes , \"model\" is one of the key in motors")

# changing the value of a specific item
# by referring to its key name
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}

motors["brand"] = "benz"
print(motors)

# update Dictionary
# the update() method will update the dict
# with the item from the given argument
# the argument must be a dict
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
motors.update({"year": 2022})
print(motors)

# Add dictionary items
# adding an item to the dictionary is done
# by using a new index and assigning a value
# to it.
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
motors["electric"] = False
print(motors)

# you can also use the update() method
# if item doesn't exist to add an item
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
motors.update({"electric": True})

print(motors)

# Removing items
# using the pop ()method removes the item
# with the specified key name
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
motors.pop("model")
print(motors)
# using the popitem() method removes
# the last inserted item
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
motors.popitem()
print(motors)
# the del keyword removes the item
# with the specified key name
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
del motors["brand"]
print(motors)
# the del can also be used to delete the
# dict completely
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
del motors
# clear () is used to empty the item in
# dict
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
motors.clear()
print(motors)

# looping in dict
# using a for loop to get the key name
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
for x in motors:
    print(x)
# you also use the keys() method to
# get the key name
for x in motors.keys():
    print(x)
# using a for loop to get the values
for x in motors:
    print(motors[x])
# you can also use the  values()
# method to get  values of a dict
for x in motors.values():
    print(x)
# using a for loop to get the
# items of dict
for x, y in motors.items():
    print(x, ":", y)

# copy () method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# another way to copy is to use the
# built-in function dict()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested dictionaries
myfamily = {
    "child1": {
        "name": "emil",
        "year": 2006
    },
    "child2": {
        "name": "tobias",
        "year": 2008
    },
    "child3": {
        "name": "linus",
        "year": 2010
    }
}

"""
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
"""

# Access items in Nested Dictionaries
print(myfamily["child2"]["name"])

# changing of item  using the update in a nested dictionaries
myfamily["child2"].update({"name": "Dondipsy", "year": 1996})

print(myfamily)
# to add dict to nested dict
myfamily.update({"child4": {"name": "Tomilola", "age": 22}})
print(myfamily)

# remove an item in nested dict
myfamily.pop("child3")
print(myfamily)

# looping through a nested dict
for x, z in myfamily.items():
    print(x)
    for y in z:
        print(y + ":", z[y])

# to get the keys of nested dict
for x in myfamily.keys():
    print(x)

# dict method
# fromkeys() it used to create a new dict
# with a specified keys and a default value
# it returns a dict where keys are taken from
# the provided iterable and each key assign to
# a default value

keys = ['x', 'y', 'z']
default_value = 0
my_dict = dict.fromkeys(keys, default_value)

print(my_dict)

keys = ("love", "hate", "betrayal")
my_dict = dict.fromkeys(keys, "life")

print(my_dict)

# setdefault() method is used to get the
# value of a key in dict, if the key is not
# present, it will insert the key with a specified
# default value and return that value
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Get value for key 'b' (exists in the dictionary)
result = my_dict.setdefault('b', 10)
print(result)  # Output: 2 (because 'b' exists and its value is 2)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3} (dictionary unchanged)

# Get value for key 'd' (doesn't exist, so add 'd' with default value 5)
result = my_dict.setdefault('d', 5)
print(result)  # Output: 5 (default value added)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 5}

#  Using setdefault() with complex default values (e.g., lists)
my_dict = {'fruits': ['apple', 'banana']}

# Add a new item to the list associated with the key 'fruits'
my_dict.setdefault('fruits', []).append('cherry')
print(my_dict)  # Output: {'fruits': ['apple', 'banana', 'cherry']}

# If 'vegetables' doesn't exist, create an empty list and append a value to it
my_dict.setdefault('vegetables', []).append('carrot')
print(my_dict)  # Output: {'fruits': ['apple', 'banana', 'cherry'], 'vegetables': ['carrot']}

# if statement
a = 33
b = 200
if b > a:
    print("b is greater than a")

# Elif keyword is way of saying
# if the previous conditions where
# not true then try this condition
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else keyword catches anything which
# isn't caught by the preceding conditions
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# you can also have an else without elif
a = 200
b = 33
if b > a:
    print("b is greater than a")

else:
    print("a is greater than b")

# And: it used to combine conditional
# statement
a = 200
b = 33
c = 500
if b >= a >= c:
    pass
else:
    print("both condition are true")

# or is used to combine conditional
# statement
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Nested if
x = 42
if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20!")
else:
    print("but not above 20")

# while loop:with the while loop we can execute
# a set of statement as long as a condition is true
# remember to increment or else the loop will continue
# forever
i = 1
while i < 6:
    print(i)
    i += 1

# break statement it is used stop the loop even
# if the while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue statement is used to stop the current
# iteration, and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# else statement we can run a block of code once
# when the condition is no longer true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("\"i\" is no longer less than 6")

# for loop is used for iterating over a sequence
# list , tuple , set , dictionary , and string
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# break statement can stop the loop before
# it has looped through all the items
# exit the loop when x is mango
fruits = ["orange", "apple", "mango", "cherry"]
for x in fruits:
    print(x)
    if x == "mango":
        break

# exit the loop when x is grapes, this time
# the break come before the print
fruits = ["date", "grapes", "cherry"]
for x in fruits:
    if x == "grapes":
        break
    print(x)

# continue statement we can stop the
# current iteration of the loop and
# continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range() to loop through a set
# of code a specified number of times
for x in range(2, 6):
    print(x)

# increment by 3
for x in range(2, 30, 3):
    print(x)

# else keyword in a for loop specifies
# a block of code to be executed when the
# loop is finished
for x in range(6):
    print(x)
else:
    print("finally finished")

# Nested For loop: a loop inside a loop
# The "inner loop" will be executed one time for
# each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# The Pass Statement
for x in [0, 1, 2]:
    pass


# Function is a block of code which
# only runs when it is called.
# creating a function

def my_function():
    print("Hello from a function")


# calling a function
my_function()


# Arguments:it is specified after
# the function name , inside the parenthesis

def grandchildren(fname):
    print(fname + " Raheem")


grandchildren("Adedolapo")
grandchildren("Tomilola")
grandchildren("Titilayo")
grandchildren("Samod")


# Arbitrary Arguments: *args
# if you don't know how many arguments
# that will be passed into your function
# add * before the parameter name in the function
# definition

def my_functions(*kids):
    print("The youngest child is " + kids[2])


my_functions("mike", "john", "jamal", "favour")


# keyword Argument: you can also send
# arguments with the key = value syntax
# this way order of the argument does not matter

def my_function(child3, child2, child1):
    print("The oldest child is  " + child1)


my_function(child1="peter", child2="tobias", child3="love")


# Arbitrary keyword Arguments:**kwargs,
# if you don't know how many keyword argument
# that would be passed into your function,add
# ** before the parameter name in the function
# definition

def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Gabriel")


# Default parameter Value
# if we call the function without
# argument it uses the default value

def my_function(country="Norway"):
    print("I am from  " + country)


my_function("Sweden")
my_function("Spain")
my_function()
my_function("Brazil")


# passing a list as an Argument

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values

def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# The pass statement

def myfunction():
    pass


# positional only argument:
# the means that argument before the /
# must be provided by position not by keyword

def my_function(x, /):
    print(x)


my_function(3)


def greet(name, age, /):
    print(f"Hello, {name}! You are {age} years old.")


# Calling the function with positional only arguments
greet("Alice", 30)  # Correct usage


# Attempting to call the function with keyword arguments will raise an error
# greet(name="Alice", age=30)   This will raise a TypeError

# keyword only argument
# this means that arguments after * must be passed as keyword
# argument when calling the function, and not by position

def greet(name, age, *, country):
    print(f"Hello, {name}! You are {age} years old, and you are from {country}.")


# Correct usage with keyword argument for `country`
greet("Alice", 30, country="Canada")  # Works fine


# Attempting to pass `country` as a positional argument will raise an error
# greet("Alice", 30, "Canada")  # This will raise a TypeError


def my_function(*, x):
    print(x)


my_function(x=3)


# combine positional-only and keyword-only

def my_function(a, b, /, *, c, d):
    print(a + b + c + d)


my_function(5, 6, c=3, d=4)


# Recursion is a defined function that
# can call itself
def myfunc(k):
    if k > 0:
        result = k + myfunc(k - 1)
        print(result)
    else:
        result = 0
    return result


print(myfunc(6))



def factorial(n):
    # Base case: when n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)


# Test the function
print(factorial(5))  # Output: 120

# A lambda function is small anonymous function
# it can take any number of arguments, but can
# only have one expression
x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# the power of lambda is shown when you use
# them as an unknown function inside another
# function

def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)
my_tripler = myfunc(3)

print(my_doubler(100))
print(my_tripler(100))

# Array are used to store multiple values
# in a single variable
# Access the element of an array by referring
# to the index number
cars = ["Ford", "BMW", "Volvo"]
x = cars[0]
print(x)
# Modify the value of first array item
cars[0] = "Toyota"
print(cars)
print(cars[0])
# length of an array
x = len(cars)
print(x)
# looping Array Elements
for x in cars:
    print(x)
# Adding Array Elements
cars.append("Honda")
print(cars)
# Removing Array Elements
cars.pop(2)
print(cars)


# Python Classes/ objects
# class is instance of an object
# A class act as a blueprint or template
# an object is a concrete instance created from the blueprint
class myclass:
    x = 5


p1 = myclass()
print(p1.x)


# __init__ : it is used to assign
# values to object properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("john", 36)
print(p1.name)
print(p1.age)


# __str__(): controls what should be
# returned when the class object is
# represented as string.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"({self.name})({self.age})"


p1 = Person("john", 36)
print(p1)


# Object Methods: method in objects are
# function that belong to the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name}, i'm  {self.age}  years of age")


p1 = Person("Dipsy", 28)
p1.myfunc()


# modify a object properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

p1.age = 40

print(p1.age)
print(p1.myfunc())
# delete objects
del p1


# static method & class method


class Myclass:
    class_variable = 42

    @staticmethod
    def static_method():
        print("static method, doesn't have access to class or instance data.")

    @classmethod
    def class_method(cls):
        print("Class method, has access to class data:")
        print("Class variable: ", cls.class_variable)


# using static method

Myclass.static_method()

# using class method

Myclass.class_method()


# pass statement

class Person:
    pass
