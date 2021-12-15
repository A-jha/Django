# CHEAT SHEET FOR PYTHON

Python is one of the most popular programming language. It is used in many fields such as Data Science, Machine learning, Web development and Many more.

Django is one of the most popular python framework for web development.

- Python is an object oriented Programming language.

## Basics

### Helloworld Program

```py
print("Hello World!")
```

- This will print hello world

### Comment

Comment are used to explain the code

- Single line comment

  ```py
  # This is a Single line comment
  print("This is a Statement")
  ```

- Multiline comment
  ```py
  """
  This is a Multiline
  comment
  You can explain your code
  in details
  """
  print("This is not a comment")
  ```

### Variable

Variable are like a container which holds data.

Example:

```py
x = 5
y = "Avi"
print(x)
print(y)
y = 56
print(y)
```

Output:

```
5
Avi
56
```

- In python Variable do not need to be declared with certain type
- You can change the type any time in the program

### Casting

If you want to specify the type then you can do it using casting

Example:

```py
x = str(3) # here x = "3"
y = int(5) # hear y = 5
z = float(3) # z = 3.0
```

### Get The Type

- You can get type using `type()` function

Example:

```py
x= 5
y = "Avi"
print(type(x))
print(type(y))
```

output:

```
<type 'int'>
<type 'str'>
```

### Single quote and Double quotes

String variable can be declared within single quotes or more specifically in double quote

```py
x = "john"
y = 'Avinash'
```

### Case Sensitive

Variable names are case Sensitive.

```py
x = 10
X = 30
print(x)
print(X)
```

### Rules of Variable Names

- Name must start with letter and it can not start with number

- A variable name can only contain alpha-numeric characters and underscore(A-z.0-9.\_)

- Variable name are case sensitive

### Multi Word Variable names

There is some need of variable name to understand it better.

#### Camel Case

- Each word expect the first start with capital letter

```py
myFirstLove = "C"
```

#### Pascal Case

- Each word start with capital letter

```py
MySecondLove = "JavaScript"
```

#### Snake Case

- Each word is separated by an Underscore(\_) character.

```py
my_last_love = 'I don\'t Know'
```

### Assigning Multiple Values in single line

Python allows you to assign values to multiple variable in one line

```py
x, y, z = "Avi",5,'a'
print(x)
print(y)
print(z)
```

### One Values to Multiple variable

Python allows you to store one value to multiple variables

```py
x = y = z = "sad life"
print(x)
print(y)
print(z)
```

### Unpack a collection

Python also allows you to unpack a collection of values such as list, tuple, etc

```py
student = ["Sam","Ravi","Avi"]

x, y, z = students

print(x)
print(y)
print(z)
```

### Output variables

The `print` statement is often used as output variables.

- TO combine text and a variable Python used `+` character.

```py
x = "Life is"
print(x+" Awesome")
```

### Global Variable

- If variable is not in side a function then it a global variable.

- Global variable means a variable which can be accessed from any where in the program.

- All Above variables are global

```py
x = "global Variable"

def someFun():
    y = " Variable inside function" # local Variable
    print(x+y) # global variable can be accessed

# call the function
someFun()
```

#### If Global Variable is changed inside function then what will happen

```py
x = "Global Variable"

def fun():
    x = "global changed"
    print(x)

fun()
print(x)
```

Output:

```
global changed
Global Variable
```

- Basically what is happening there is x is a global variable and if we declare a sme name variable inside function then that variable is local variable to that function and can only retain there value inside that function

### Global Keyword

When we create a variable inside a function then that variable is local and it's scope is only inside that function.

- To create a Global Variable inside a function we use the global keyword.

```py
def fun():
    global x
    x = "global inside fun"

# it will throw an error that x is not declared
#print(x)

# first call the function such that x came into existence
print(x)
```

#### Q. How can we change the value of global variable inside a function ?

To change the value og global variable inside a function we have to use global keyword

```py
x = "Global Variable"

def fun():
    global x
    x = "global changed"
    print(x)

fun()
print(x)
```

Output:

```
global changed
global changed
```

### Data Types in Python

Data types is an important concept in programming

Variable can store different types.

| Types    | keyword                      |
| -------- | ---------------------------- |
| Text     | str                          |
| Numeric  | int, float, complex          |
| Sequence | list, tuple, range           |
| Mapping  | dict                         |
| Set      | set, frozenset               |
| Boolean  | bool                         |
| Binary   | bytes, bytearray, memoryview |

- `type()` function is used to get the data types of the variable.

### Example of Data types in Python

```py
x = "Avinash" #str
x = 20 #int
x = 20.5 #float
x = 1j # complex
x = ["sad","Happy","Fun"] # list
x = ("Sad","Happy","Fun") # tuple
x = range(6) # range
x = {"name":"Avinash", "age":21,"Love":"single"} # dict

x = {"Love","Attraction","Feelings"} # set

x = fronzenset({"apple","Banana","cherry"})

x = True # bool

x = b"Hello" #bytes

x = bytearray(5) # bytearray

x = memoryview(bytes(5)) # memoryview

```

### Setting up Specific data type

```py
x = str("Happy Move")

x = int(34)

x = float(30.5)

x = complex(1j)

x = list(("Apple","Banana","Mango"))

x = tuple(("Apple","Banana","Mango"))

x = range(6)

x = dict((name = "Avinash",age = 21))

x = set(("apple","banana","Mango"))

x = frozenset(("Apple","Banana", "Mango"))

x = bool(5)

x = bytes(5)

x = bytearray(5)

x = memoryview(bytes(5))

```

### Python Numbers

In Python there are three types of numbers

1. int : Integer/positive and Negative / unlimited length / no decimal value

2. float : Containing one or more decimal / Floating point number / positive and Negative

3. complex : complex number is written in `3 + 4j` and here j is imaginary part.

Example:

```py
x = 10 # integer

y = 25.6

z = 3 + 4j

print("X is an Int with value = ",x)
print("Y is a float with value = ",y)
print("Z is a complex number with value = ",z)

# Type of them
print(type(x))
print(type(y))
print(type(z))
```

Output:

```
('X is an Int with value = ', 10)
('Y is a float with value = ', 25.6)
('Z is a complex number with value = ', (3+4j))
<type 'int'>
<type 'float'>
<type 'complex'>
```

### Type Conversion

Python allows us to convert variable from one type to another.

Example:

```py
x = 1
y = 5.6
z = 3 + 4j

# covert from int to float
a = float(x)

# covert float to int
b = int(y)

# convert int to complex
c = complex(x)

# covert complex to float
# d = float(z)

# covert complex to int
# e = int(z)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
```

Output:

```
1.0
5
(1+0j)
<type 'float'>
<type 'int'>
<type 'complex'>
```

- We can not convert complex to int or float

### Random Number in Python

Like in c++ we have a rand() function to produce random number but in python we do not have any such function.

In python there is a built in module to produce random number.

Example:

```py
import random

print(random.randrange(1,10))
```

- This will produce random number between 1 to 9

### Python Casting

Python is an Object oriented programming language and it used class to define data types, including its primitive types.

**Casting in Python is done using Constructor function.**

- int() - Constructs an

  - Integer number from an integer literal,
  - a float literal (by removing all decimal),
  - a string literal(by providing the string represents a whole number)

- float() - Constructs an

  - Float number from an integer literal
  - A string literal to float

- str() - Constructs a string from wide variety of data types, including string, integer and float literals

Example of Int casting

```py
x = int(1) # x = 1
x = int(5.6) # x = 5
x = int("3") # x = 3
```

Example of Float Casting

```py
x = float(1) # x = 1.0
y = float(5.6) # y = 5.6
z = float("3")  # z = 3.0
w = float("4.4") # w = 4.4
```

Example of String casting

```py
x = str("s1") # x = 's1'
y = str(2)  # x = '2'
z = str(3.0) # z = '3.0'
```

## Python String

### Assigning string to a variable

```py
a = "string ha ha ha"
```

### Multiline String variable

```py

a = """
Hi My name is Python
I am an Object oriented programming language
If you want then you can learn
ha ha
ha ha
ha
"""
print(a)
```

### String are Array

String in python is an array of bytes representing unicode characters.

**Note:** Python does not have character data type, a single char is simply a string with length 1.

Example:

```py
a = "Hello, World!"
print(a[1])
```

### Looping thorough String

String is an array so looping through it is easy.

```py
x = "Avinash"

for i in x:
  print(i)
```

Output:

```
A
v
i
n
a
s
h
```

### String Length

To get the length of string we use `len()` function.

```py
x = "Avinash"
print(len(x))
```

### Check sub string in string

To check if a sub string is part of a given string.

- **in** is used

```py
x = "I don't think i am learning i think i am willing to learn"

print("learn" in x)

if "learn" in x:
    print("Yes, 'learn' is present")
```

Output:

```
True
Yes, 'learn' is present
```

### Check if not

To check if certain substring is not part of string.

Example:

```py
x = "I don't think i am learning i think i am willing to learn"

print("love" not in x) # true
```

### Slicing String

This is one of the important concept in python string.

Specify the starting and end index, separated by colon, to return the part of string

Example:

```py
b = "Avinash"
print(b[2:5])# 2 to 4 note 5 is not included
```

- Slicing From start

  ```py
  b = "sad life"
  print(b[:5])#get char from start to index 4
  ```

- Slicing to the end

  ```py
  b = "Happy coding"
  print(b[4:]) # get char from index 2 to end
  ```

- Negative indexing
  ```
   A   v   i   n   a   s   h
   0   1   2   3   4   5   6
  -7  -6  -5  -4  -3  -2  -1
  ```
  ```py
  b = "mood off"
  print(b[-5])#d
  print(b[-5,-2]) # d 0
  ```

### Modify String

#### Upper case

The `upper()` methods returns string in upper case

```py
a = "Mood off"
print(a.upper())
```

#### Lower Case

The `lower()` methods returns string in lower case

```py
a = "Mood off"
print(a.lower())
```

#### Remove White Space

The `strip()` method removes any white space from beginning and end.

```py
x = "        Avinash  is buddy    "
print(x)
print(x.strip())
```

Output:

```
        Avinash  is buddy
Avinash  is buddy
```

#### Replace String

The `replace()` method replaces a string with another string.

```py
x = "sam is a good boy"
print(x.replace("sam","Avinash"))
```

Output:

```
Avinash is a good boy
```

#### Split String

The `split()` method return a list where the text between the specified separator becomes the list items.

```py
a = "Hey there how are you"
print(a.split(" "))
```

Output:

```
['Hey', 'there', 'how', 'are', 'you']
```

### String Concatenation

Concatenation means combining two string using `+` operator.

```py
a = "Hello"
b = "world"
c = a + b
print(c)
```

### String Format

In Python we can not combine string and numbers.

```py
x = 21
y = "My name is Avinash and I am of age "+age

print(y)
```

Output Error:

```
TypeError: cannot concatenate 'str' and 'int' objects
```

To Solve this issue in python we have a method `format()`

Format method takes passed arguments, formats then, and places them in the string where placeholder `{}` are

```py
x = 21
dob = 21
y = "My name is Avinash and I am of age {} and dob is {}"

print(y.format(x,dob))
```

Output:

```
My name is Avinash and I am of age 21 and dob is 2
```

### Escape Character

To insert the character that are illegal in a string, we use escape character `\`.

Example:

```py
x = "My  name is "Avinash jha""
print(x)
```

Output:

```
SyntaxError: invalid syntax
```

TO Solve these type of problem we use escape character

```py
x = "My Name is \"Avinash jha\""
print(x)
```

Output:

```
My  name is "Avinash jha"
```

### Escape Characters

| Code | Result          |
| ---- | --------------- |
| \'   | Single Quote    |
| \\   | Backslash       |
| \n   | New Line        |
| \r   | Carriage Return |
| \t   | Tab             |
| \b   | Backspace       |
| \f   | Form Feed       |
| \ooo | Octal Value     |
| \xhh | Hex Value       |

### String Methods

There are many built in method that can be used in python string.

All String method return a new value and they do not change the originam string.

| Method         | Description                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------- |
| capitalize()   | covert the first char to upper case                                                           |
| casefold()     | covert string into lowercase                                                                  |
| center()       | Return centered string                                                                        |
| count()        | return number of times specific value occurs in string                                        |
| encode()       | returns encoded version of string                                                             |
| endswith()     | return true if string ends with specific value                                                |
| expandtabs()   | set tab size to the string                                                                    |
| find()         | searches the string for a specified value and returns the position of where it was found      |
| format()       | Formats specified values in a string                                                          |
| format_map()   | Formats specified values in a string                                                          |
| index()        | Searches the string for a specified value and returns the position of where it was found      |
| isalnum()      | Returns True if all characters in the string are alphanumeric                                 |
| isalpha()      | Returns True if all characters in the string are in the alphabet                              |
| isdecimal()    | Returns True if all characters in the string are decimals                                     |
| isdigit()      | Returns True if all characters in the string are digits                                       |
| isidentifier() | Returns True if the string is an identifier                                                   |
| islower()      | Returns True if all characters in the string are lower case                                   |
| isnumeric()    | Returns True if all characters in the string are numeric                                      |
| isprintable()  | Returns True if all characters in the string are printable                                    |
| isspace()      | Returns True if all characters in the string are whitespaces                                  |
| istitle()      | Returns True if the string follows the rules of a title                                       |
| isupper()      | Returns True if all characters in the string are upper case                                   |
| join()         | Joins the elements of an iterable to the end of the string                                    |
| ljust()        | Returns a left justified version of the string                                                |
| lower()        | Converts a string into lower case                                                             |
| lstrip()       | Returns a left trim version of the string                                                     |
| maketrans()    | Returns a translation table to be used in translations                                        |
| partition()    | Returns a tuple where the string is parted into three parts                                   |
| replace()      | Returns a string where a specified value is replaced with a specified value                   |
| rfind()        | Searches the string for a specified value and returns the last position of where it was found |
| rindex()       | Searches the string for a specified value and returns the last position of where it was found |
| rjust()        | Returns a right justified version of the string                                               |
| rpartition()   | Returns a tuple where the string is parted into three parts                                   |
| rsplit()       | Splits the string at the specified separator, and returns a list                              |
| rstrip()       | Returns a right trim version of the string                                                    |
| split()        | Splits the string at the specified separator, and returns a list                              |
| splitlines()   | Splits the string at line breaks and returns a list                                           |
| startswith()   | Returns true if the string starts with the specified value                                    |
| strip()        | Returns a trimmed version of the string                                                       |
| swapcase()     | Swaps cases, lower case becomes upper case and vice versa                                     |
| title()        | Converts the first character of each word to upper case                                       |
| translate()    | Returns a translated string                                                                   |
| upper()        | Converts a string into upper case                                                             |
| zfill()        | Fills the string with a specified number of 0 values at the beginning                         |

### Python Booleans

In programming boolean means `true` or `false`.

### Python Operators

Operators are used to perform operations on variable and values.

There are following types of operator in python:

- Arithmetic operator : common mathematical operations

  - \+ additions
  - \- subtraction
  - \* multiplication
  - \/ division
  - % modulus
  - \*\* exponent
  - // floor division

- Assignment Operator : used to assign values to the variable.

  - =, +=, -= etc

- Comparison Operator: used to compare two values

  - ==, !=, >, <, >=, <=

- Logical Operator: used to combine conditional logic

  - and : true if both true
  - or : true if one is true
  - not : true if false

- Identity Operator: Used to compare the object, not if they are equal but if they are actually same with same memory location

  - is : return true if both variable are the same object
  - is not : returns true if both variables are not he same object

- Membership Operator : used to test if a sequence is presented in object.

  - in : returns true if sequence with specified value present in the object.
  - not in : Returns true if sequence with the specified value is not present in the object

- Bitwise Operator : used to compare binary number
  |Operator|Name|Description|
  |--------|----|-----------|
  |&|AND|set each bit to 1 if both bit are 1|
  |\||OR|set each bit to 1 if one of two bit is 1|
  |^|XOR|set each bit to one if only one of the bit is 1|
  |~|NOT|inverts all the bit|
  |<<|zero fill left shift |shift left by pushing zero in from the right and left most bits fall off|
  |>>|Signed right shift|Shift right by pushing copies of the leftmost bit in from the left and let the right most bit fall off|

## Python Collections(Arrays)

There are four collection data type in python.

- **List** is a collection which is ordered and changeable. Allows duplicate members.

- **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.

- **Set()** is a collection which is unordered, unchangeable, and unindexed. No duplicate members.

- **Dictionary** is a collection which is ordered and changeable. no duplicate members.

### List

List are used to store multiple items in a single variable

```py
listOfFruits = ["Apple","Banana"]
print(listOfApple)
```

#### List items

List items are ordered, changeable, and allow duplicate value.

List items are indexed 0 to n-1

- Ordered: In List items have a defined order.

- **Changeable** : We can change add and remove items in a list after it has been created.

- **Allow Duplicates** : List can have items with same value

- **List Length** : `len()` function if used to check the length of the list.

- List item can be of any data types

- List are defined as an objects with data type **list**

#### List constructor

It is possible to use the **list()** constructor when creating a new list.

### Access List Items

list items are indexed and we can use index to access the item.

```py
l = [1,2,3,4,5]
print(l[0])# l[0] = 1
```

#### Negative indexing

Negative indexing means start from the end.

-1 means last item
-2 means second last

```py
l = ["apple","banana"]
print(l[-1])# apple
```

#### Range of indexes

Ypu can specify a range of indexes by specifying where to start and where to end.

```py
l = ["apple","mango","nut","banana"]
print(l[1:3])# mango and nut
```

#### Check if item in list

To determine specific item in a list use the `in` keyword.

```py
l = ["apple","mango","nut","banana"]

if "apple" in l:
  print("yes apple is the part of the list)
else:
  print("No it is not in list")
```

### Change List item

To change specific value refers to the index value

```py
l = ["Avi","Ravi","Kavi"]
l[0] = "Avinash"
print(l[0])#Avinash
```

#### Change Range of items value

```py
l = ["Banana","apple","nut","mango","guava"]
print(l)
l[1:3]=["watermelon","grapes"]
print(l)
```

Output:

```
['Banana', 'apple', 'nut', 'mango', 'guava']
['Banana', 'watermelon', 'grapes', 'mango', 'guava']
```

### Insert item

To insert new item in the list without replacing any of the existing values, we can use the insert method.

The insert method insert item at specific index.

```py
l =["Banana","Apple","Mango"]
l.insert(2,"Watermelon")# insert at index 2
print(l)
```

### Append items

To add item to the end of the list we use `append()` method.

```py
l = ["Apple","orange","banana"]
l.append("watermelon")# insert watermelon at the end of list l
print(l)
```

### Extend List

We can add two list using `extend()` method.

```py
l = ["banana","apple","mango"]
m = ["pineapple","grapes","papaya"]
l.extend(m)
print(l)
```

### add any iterable

`extend()` method can also be used to append any iterable object (tuples, sets, dictionaries etc)

```py
l = ["apple","mango","grapes"]
m = ("kiwi","orange")
l.extend(m)
print(l)
```

### Remove Specified item

The `remove()` method removes the specified item.

Example: Remove "banana"

```py
l = ["apple","banana","cherry"]
l.remove("banana")
print(l)
```

### Remove specific Index

The `pop()` method removes the specified index.

```py
l = ["apple","banana","cherry"]
l.pop(1)# remove index 1
print(l)
```

### Remove last item

The `pop()` method without any args will remove last element from the list.

```py
l = ["apple","banana","cherry"]
l.pop()
print(l)
```

### Remove item using del keyword

The `del` keyword also removes the specified index.

```py
l = ["apple","banana","cherry"]
del l[1] # remove banana from the list
print(l)
```

### Delete the list completely

The `del` key can also delete the list completely.

```py
l = ["banana","apple","cherry"]
del l# this will delete the list completely
```

### clear the list

`clear()` method empties the list.

```py
l = ["banana","apple","cherry"]
l.clear()
print(l)
```

### Loop through the list

#### using for loop

```py
l = ["banana","apple","cherry"]
for x in l:
  print(x)
```

#### Loop through the index numbers

```py
l = ["banana","apple","cherry"]
for i in range(len(l)):
  print(l[i])
```

#### Using a while loop

```py
l = ["banana","apple","cherry"]
i = 0;
while i < len(l):
  print(l[i])
  i = i + 1
```

#### Looping Using list comprehension

A short hand for loop that will print all item in a list.

```py
l = ["banana","apple","cherry"]
[print(x) for x in l]
```

### List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the value of an existing list.

Full code:

```py
l = ["banana","apple","cherry","kiwi","mango"]
newList = []

for x in l:
  if "a" in x:
    newList.append(x)

print(newList)
```

Output:

```
['banana', 'apple', 'mango']
```

Short hand:

```py
l = ["banana","apple","cherry","kiwi","mango"]
newList = [x for x in l if "a" in x]

print(newList)
```

Output:

```
['banana', 'apple', 'mango']
```

### Sort List

#### Sort list Alphanumerically

List objects have a `sort()` method that will sort the list Alphanumerically, ascending, by default.

Example:

```py
l = ["banana","apple","cherry","kiwi","mango"]
l.sort()
print(l)
```

Output:

```
['apple', 'banana', 'cherry', 'kiwi', 'mango']
```

Example:

```py
l = [100,30,50,40,20]
l.sort()
print(l)
```

Output:

```
[20, 30, 40, 50, 100]
```

#### Sort Descending

To sort descending, use the keyword arguments reverse = True:

Example:

```py
l = [100,30,50,40,20]
l.sort(reverse=True)
print(l)
```

Output:

```
[100, 50, 40, 30, 20]
```

### Reverse a list

The `reverse()` method is used to reverse a list

```py
l = ["Apple","Banana","Mango"]
l.reverse()
print(l)
```

### Copy List

You can nto copy list simply list1 = list2, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made.

To copy a list to another list we use `copy()` method.

```py
l = ["Banana", "Apple", "Mango"]
l1 = list(l)
print(l1)
```

### Join List

```py
l1 = [1,2,3,4]
l2 = ["A","B","C"]
l3 = l1 + l2
print(l3)
```

### Python Tuples

Tuples are used to store multiple items in a single variable.

- Unchangeable

```py
t = ("Apple","banana","Cherry")
print(t)
print(type(t))
```

Output:

```
('Apple', 'banana', 'Cherry')
<type 'tuple'>
```
