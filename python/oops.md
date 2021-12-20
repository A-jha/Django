# Object oriented programming in Python

## Python Classes and Object

- Python is an object oriented programming language.
- Almost everything in python is an object, with its properties and methods.

- A class is like an object constructor or blueprint of creating object.

### Create a class

To create a class we use `class` keyword.

```py
class myClass:
    x = 6
```

### Create Object

Now we can create an object of myClass.

```py
p1 = myClass()
print(p1.x)
```

### The `__init__()` function

TO understand the meaning of class we have to understand the built-in `__init__()` function.

All class have a function called `__init__()`, which is always executed when the class is being initiated.

Use the `__init__()` function to assign values of the object properties, or other operations that are necessary to do when the object is being created.

Example:

```py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age



s1 = Student("Avinash",21)
print(s1.name)# Avinash
print(s1.age)# 21
```

**Note:** The `__init__()` function is called automatically every time the class is being used to create a new object.

### The self Parameter

The `self` parameter is a reference to the current instance of the class, and is used to access variables that belongs to that class.

It is not necessary to write self we can write anything we wish.

```py
class Student:
    def __init__(notSelf,name,age):
        notSelf.name = name
        notSelf.age = age

    def myFunc(itSelf):
        print("Hello is am itSelf but self and my name is "+itSelf.name)

# create an object
s1 = Student("Avinash",21)
s1.myFunc()
```

### Modify object properties

We can change the property of an object.

```py
class Student:
    def __init__(notSelf,name,age):
        notSelf.name = name
        notSelf.age = age

    def myFunc(itSelf):
        print("Hello is am itSelf but self and my name is "+itSelf.name)

# create an object
s1 = Student("Avinash",21)
s1.name = "Arpita"
s1.myFunc()
```

### Delete Object Properties

We can delete object by using `del` keyword.

```py

class Student:
    def __init__(notSelf,name,age):
        notSelf.name = name
        notSelf.age = age

    def myFunc(itSelf):
        print("Hello is am itSelf but self and my name is "+itSelf.name)

# create an object
s1 = Student("Avinash",21)
s1.name = "Arpita"
del s1
s1.myFunc()
```

Output:

```
Error: s1 is not defined
```

### Pass Statement

class definition can not be empty, but if you for some reason want to ignore this class definition then you can add pass inside the class.

```py
class NotInteresting:
    pass
```

## Python Inheritance

Inheritance allows us to define a class that inherits all the method and properties from another class.

**Parent class** is the class being inherited from, also K/A **Base class**

**Child class** is the class that inherits from another class, also called **derived class**.

### Create a Parent Class

Any class can be parent class.

```py
class Person:
    def __init__(self,fName,lName):
        self.fName = fName
        self.lName = lName

    def printName(self):
        print(self.fName, self.lName)

#creating an object of parent class
p1 = Person("Avinash","Jha")
p1.printName()
```

### Create a Child Class

To Create a class that inherits the functionality from another class, send parent class as a parameter when creating child class.

```py
class Student(Person):
    pass

# create an object of Student class
s1 = Student("Avinash","Jha")
s1.printName()# method from parent class
```

### Add the `__init__()` function

So far we have created a child class that inherits the properties and method from its parent.

We want to add the `__init__()` function to the child class

**Note:** The `__init__()` function is called automatically every time the class is being used to create a new object.

```py
class Student(Person):
    def __init__(self,fName,lName):
        self.firstName = fName
        self.lastName = lName

# create an object of Student class
s1 = Student("Avinash","Jha")
```

When we ad the `__init__()` function, the child class will no longer inherit the parent's `__init__()` function.This is called **Function overriding**

To Keep the inheritance of the parent's `__init__()` function, add a call to the parent's `__init__()` function.

```py
class Student(Person):
    def __init__(self,fName,lName):
        Person.__init__(self,fName,lName)
```

Now we have successfully added the `__init__()` function, and kept the inheritance of the parent class, and we are ready to add functionality in the `__init__()` function.

### Use the super() function

Python also has a `super()` function that will make the child class inherit all the methods and properties from its parent.

```py
class Student(Person):
    def __init__(self,fName,lName,year):
        super().__init__(fName,lName)
        self.graduationYear = year
    # this is the method
    def printDetails(self):
        print(self.fName,self.lName,self.year)

# create an object of student class
s1 = Student("Avinash","Jha",2022)
s1.printDetails()
```
