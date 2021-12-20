## Python Lambda Function

A lambda function is an anonymous function.

A lambda function can take any no of arguments but can have only one expression.

### Syntax

```
lambda arguments : expression
```

the expression is executed and result is returned.

Example: Add 10 to argument and return the result.

```py
x = lambda a : a + 10
print(x(5))#15
```

Example: Multiple arguments

```py
x = lambda a, b: a **b

print(x(2,3))#8
```

### Use of Lambda function

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument and the argument will be multiplied by unknown number.

```py
def myFun(n):
    return lambda a: a * n

myNum = myFun(5)
print(myNum(10))# 50
```
