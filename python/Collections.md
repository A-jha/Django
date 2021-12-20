## Python Collections(Arrays)

There are four collection data type in python.

- **List** is a collection which is ordered and changeable. Allows duplicate members.

- **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.

- **Set()** is a collection which is unordered, unchangeable, and unindexed. No duplicate members.

- **Dictionary** is a collection which is ordered and changeable. no duplicate members.

## Python List

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

## Python Tuples

Tuples are used to store multiple items in a single variable.

- Unchangeable
- A tuple can contain items of different data types.

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

### Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values.

first item [0]

### Tuple length

- len() function can be used to count no of items in tuple.

```py
t = ("apple","banana","mango")
print(len(t))
```

### Tuple with one item

```py
t1 = ("Apple",)
t2 = ("Apple")
print(type(t1))
print(type(t2))
```

Output:

```
<type 'tuple'>
<type 'str'>
```

### Access Tuple Items

- We can access item using index.

```py
t = ("Apple","Mango","banana")
print(t[0])# Apple
```

### Negative Indexing

- Negative indexing means start from end.

```py
t = ("Apple","Mango","banana")
print(t[-1])# Banana
```

### Range of Indexes

When specifying a range, the return value will be a new tuple with the specified items.

```py
t = ("Apple","Mango","banana","cherry","watermelon")
print(t[1:3])
```

Output:

```
('Mango', 'banana')
```

### Check if item Exists

```py
t = ("Apple","Mango","banana","cherry","watermelon")
if "Apple" in t:
  print("Yes Apple is a part of tuple")
```

### Update Tuples

- Tuples are **unchangeable** or **immutable** as it also called.

- To Update the tuple we can covert into list and then change it and then covert it into tuple.

```py
t = ("apple","banana","mango")
l = list(t)
y[1] = "watermelon"
t = tuple(l)
print(t)
```

**Note:** adding removing methods can be used on tuple by converting it into list and after the change made covert back to tuple.

### Unpack Tuple

- Direct Method

```py
t = ("Apple","Mango","banana")
(apple,mango,banana) = t
print(apple)
print(mango)
print(banana)
```

- Using Asterisk*
  If there are many items in a tuple then it is better to use * such that we can get some specific value and a list of remaining items.

```py
t = ("apple", "banana", "cherry", "strawberry", "raspberry")
(apple, banana, *others) = t
print(apple)
print(banana)
print(others)
```

### Join Tuples

TO join two or more tuples you can use `+` operator.

```py
t = ("a","b","c")
t2 = (1,2,3)

t3 = t1 + t2
print(t3)
```

### Multiply tuples

```py
t = ("a","b","c")
t2 = t * 2
print(t2)
```

## Python Sets

Sets are also used to store multiple items in a single variable.

- Set items are Unordered
- Unchangeable
- No duplicate item allowed

```py
s = {"apple","banana","nuts"}
print(s)
```

- len() function can be used to get the length of set

- Set item can be of any data types.

```py
set1 = {1,"Avi",2,"sam"}
```

### Access the set Items

- We can not access set using index.
- We can loop through the items using for loop and access item using `in` keyword.

```py
set1 = {"Apple","banana","mango"}
for x in set1:
    print(x)
```

### Check if an item is in set

```py
set1 = {"Apple","banana","mango"}
print("Apple" in set1)
```

### Change Items of Set

- We can not change the item inside set, but we can add new items.

### Add Items

- We can add items in a set using `add()` method.

```py
set1 = {"Apple","banana","mango"}
set1.add("orange")
print(set1)
```

### Add sets

To add items from another set into current set, use `update()` method.

```py
set1 = {"Apple","banana","mango"}
set2 = {"Apple","pineapple","orange","papaya"}
set1.update(set2)
print(set1)
```

Output:

```
set(['mango', 'papaya', 'Apple', 'pineapple', 'orange', 'banana'])
```

### Add Any Iterable

The object in the `update()` method does not have to be a set.

```py
set1 = {"Apple","pineapple","orange","papaya"}
list1 = ["Apple","banana","mango"]

set1.update(list1)
print(set1)
```

Output:

```
set(['papaya', 'Apple', 'mango', 'pineapple', 'orange', 'banana'])
```

### Remove Set Items

To remove set items use `remove()` or `discard()` method.

```py
set1 = {"Apple","pineapple","orange","papaya"}
set1.remove("pineapple")
print(set1)

set1.discard("Apple")
```

Output:

```
set(['orange', 'papaya', 'Apple'])
```

- **pop()** method is also used to remove an item, but this method will remove the last item.

```py
set1 = {"Apple","pineapple","orange","papaya"}
set1.pop()
print(set1)
```

**Note:** Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

- **clear()** method is used to empty the set.

- **del** keyword will delete the set completely.

### Join Sets

There are many way to join two or more sets in Python.

- **union()**
- **update()**

#### Join Sets Using Union

```py
set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)
```

Output:

```
set(['a', 1, 'c', 'b', 3, 2])
```

#### Join Sets using Update

```py
set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)
```

**Note:** Both `union()` and `update()` will exclude any duplicate items.

### Common item between sets

The `intersection_update()` method will keep only the items that are present in both sets.

```py
set1 = {"a","b","c","x"}
set2 = {"z","a","x","y"}
set1.intersection_update(set2)
print(set1)
```

Output:

```
set(['a', 'x'])
```

### Exclude common element between two sets

The `symmetric_difference_update()` method will keep only the element that are NOT present in both sets.

```py
set1 = {"a","b","c","x"}
set2 = {"z","a","x","y"}
set1.symmetric_difference_update(set2)
print(set1)
```

Output:

```
set(['y', 'c', 'b', 'z'])
```

### Set Methods

| Method                        | Description                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------ |
| add()                         | Adds an element to the set                                                     |
| clear()                       | Removes all the elements from the set                                          |
| copy()                        | Returns a copy of the set                                                      |
| difference()                  | Returns a set containing the difference between two or more sets               |
| difference_update()           | Removes the items in this set that are also included in another, specified set |
| discard()                     | Remove the specified item                                                      |
| intersection()                | Returns a set, that is the intersection of two other sets                      |
| intersection_update()         | Removes the items in this set that are not present in other, specified set(s)  |
| isdisjoint()                  | Returns whether two sets have a intersection or not                            |
| issubset()                    | Returns whether another set contains this set or not                           |
| issuperset()                  | Returns whether this set contains another set or not                           |
| pop()                         | Removes an element from the set                                                |
| remove()                      | Removes the specified element                                                  |
| symmetric_difference()        | Returns a set with the symmetric differences of two sets                       |
| symmetric_difference_update() | inserts the symmetric differences from this set and another                    |
| union()                       | Return a set containing the union of sets                                      |
| update()                      | Update the set with the union of this set and others                           |

## Python Dictionary

Dictionary are used to store data values in key:value pairs.

A dictionary is a collection which is **ordered**, changeable and do not allow duplicates.

Example:

```py
student = {
    "name":"Avinash",
    "roll":1,
    "dob":2000
}
print(student)
```

Output:

```
{'dob': 2000, 'name': 'Avinash', 'roll': 1}
```

### Dictionary Items

Dict items are presented in key:value pairs, and can be referred to by using the key name.

```py
student = {
    "name":"Avinash",
    "roll":1,
    "dob":2000
}
print(student["name"])
```

### Dictionary length

To determine how many items a dictionary has, use the `len()` function.

```py
student = {
    "name":"Avinash",
    "roll":1,
    "dob":2000
}
print(len(student)) #3
```

### Get Keys

The `keys()` method will return a list of all the keys in the dictionary.

```py
student = {
    "name":"Avinash",
    "roll":1,
    "dob":2000
}
keys = student.keys()
```

Output:

```
['dob', 'name', 'roll']
```

### Get Values

The `values()` method will return a list of all the values in the dictionary.

```py
student = {
    "name":"Avinash",
    "roll":1,
    "dob":2000
}
values = student.values()
print(values)
```

Output:

```
[2000, 'Avinash', 1]
```

### Change the values of key

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
values = student.values()
print(values)
student["name"] = "Ravi"
values = student.values()
print(values)
```

Output:

```
[2000, 'Avinash', 1]
[2000, 'Ravi', 1]
```

### Get Items

The `items()` method will return each item in a dictionary, as tuples in a list.

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
items = student.items()
```

Output:

```
[('dob', 2000), ('name', 'Avinash'), ('roll', 1)]
```

### Check if key exist in dict

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
if "name" in student:
    print("key is present")
elif "roll" in student:
    print("roll is in student")
else:
    print("key not found")
```

### Change Dict Items

You can change The value of specific item by referring to its key name.

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
# change name
student["name"] = "Ravi"
```

### Update Dict

The `update()` method will update the dictionary with items from the given arguments.

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
student.update({"name":"Ravi","roll":3})
print(student)
```

Output:

```
{'dob': 2000, 'name': 'Ravi', 'roll': 3}
```

### Remove Dict Item

#### pop() method

pop() method removes the item with the specific key name.

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
student.pop("name")
print(student)
```

Output:

```
{'dob': 2000, 'roll': 1}
```

#### popitem() method

popitem() method removes the last inserted item.

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
student.popitem()
print(student)
```

Output:

```
{'name': 'Avinash', 'roll': 1}
```

#### del Keyword

The del keyword removes the item with the specific key name.

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
del student["name"]
print(Student)
```

- del keyword is also used to delete the dictionary completely.

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
del student
print(student) # this will through an error because student is no more in the program
```

#### clear() method

The clear() method empties the dictionary.

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
student.clear()
print(student)#{}
```

### Loop Through Dictionary

#### Print keys

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
for c in  student:
    print(x)
```

#### Print Values

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
for c in  student:
    print(student[x])
```

#### using values() method

It will return values

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
for c in  student.values():
    print(x)
```

#### using keys() method

It will return keys of dict

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
for c in  student.keys():
    print(x)
```

#### using items() method

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
for c in  student.items():
    print(x)
```

### Copy dictionary

Like set we can not directly write dict1 = dict2, because: dit2 will only be a reference to dict1, and any change in dic2 will reflect in dict2.

#### Copy() method

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
newStudent = student.copy()
print(newStudent)
```

Output:

```
{'dob': 2000, 'name': 'Avinash', 'roll': 1}
```

#### using dict() constructor

```py
student = {
    "name": "Avinash",
    "roll": 1,
    "dob": 2000
}
newStudent = dict(student)
print(newStudent)
```

### Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries.

Example1:

```py
myClass = {
    "student1":{
        "name":"Avinash",
        "roll":1,
        "passing":2022
    },
    "student2":{
        "name":"Sam",
        "roll":2,
        "passing":2022
    },
    "student3":{
        "name":"Ravi",
        "roll":3,
        "passing":2022
    }
}
```

Example2:

```py
student1 = {
    "name":"Avinash",
    "roll":1,
    "passing":2022
}
student2={
    "name":"Sam",
    "roll":2,
    "passing":2022
}
student3={
    "name":"Ravi",
    "roll":3,
    "passing":2022
}
# combine all 3 student to a class
myClass = {
    "student1":student1,
    "student2":student2,
    "student3":student3
}
```
