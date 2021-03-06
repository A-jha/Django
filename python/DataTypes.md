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
