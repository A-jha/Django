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
