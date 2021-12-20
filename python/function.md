## Python Functions

- A function is block of code which only runs when it is called.

- Data passed to function is k/a Arguments.

### Creating a function

In python to define a function we use `def` keyword.

```py
def myFunc():
    print("This a function")
```

### Calling a function

```py
myFunc()
```

### Arguments

Information can be passed into functions as arguments.

Example1:

```py
# a python program to print the string passed
def printString(string1):
    print("Your string is "+string1)

# call the function and pass the arguments
printString("life is on endless track")
```

Example2:

```py
# define a function to calculate simple interest
def calculateSi(rate,time,amount):
    myString = "your amount is {} , your time is {} your interest rate is {} and your simple interest is {}"
    print(myString.format(amount,time,rate,(amount*time*rate/100)))

calculateSi(10,5,100)
```

Output:

```
your amount is 100 , your time is 5 your interest rate is 10 and your simple interest is 50
```

### Arbitrary Arguments, \*args

if you do not know how many arguments that will be passed into your function, add a `*` before the parameters name in the function definition.

```py
def myFun(*strings):
    print("My Name is "+strings[0])
    print("My nick Name is "+strings[1])

myFun("Avinash","Babu","Raunak","Sam")
```

Output:

```
My Name is Avinash
My nick Name is Babu
```

### Keyword Arguments

You can also send arguments with the key = value syntax.

```py
def myFun(name, nickName, brother):
    string1 = "My name is {} \n My nick name is {}\nMy friends name is {}"
    print(string.format(name,nickName,brother))

myFun(name="Avinash",nickName="Babu",brother="Raunak")
```

Output:

```
My name is Avinash
 My nick name is Babu
My friends name is Raunak
```

### Arbitrary Keyword Arguments, \*\*kwargs

If you don't know how many keyword arguments that will be passed into your function, add two asterisk `**` before the parameter name in the function.

This way the function will receive a dictionary of arguments, and can access the items accordingly.

```py
def myFun(**student):
    print("Last name : "+student["lName"])

myFun(fName = "Avinash",lName="Jha")
```

### Default Parameters

If we call the function without arguments, it uses the default value.

```py
def myFun(name="Avinash"):
    print("My name is "+name)

myFun("Sam")
myFun()
```

Output:

```
My name is Sam
My name is Avinash
```

### Passing List as argument

You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

```py
def myFun(list1):
    for x in list1:
        print(x)

list1 = ["Apple","Mango","Banana"]
myFun(list1)
```

Output:

```
Apple
Mango
Banana
```

### The pass Statement

Function definition can not be empty. but if you want to define it later then put pass inside it.

```py
def myFun():
    pass

myFun()# it will not do any thing
```

## Recursion

Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

Example: Factorial Program using recursion

```py
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n-1)
num = 5
print("Factorial of " + str(num) + "is " + str(factorial(num)))
```

Example: Fibonacci Number using recursion

```py
def fibonacci(n):
    # check if n< 0 then Incorrect
    if n < 0:
        print("Invalid Input")

    # if n == 0
    elif n == 0:
        return 0

    # if n == 1 or n == 2
    elif n == 1 or n == 2:
        return 1

    # else recursion
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))
```
