
class Student:
    def __init__(notSelf, name, age):
        notSelf.name = name
        notSelf.age = age

    def myFunc(itSelf):
        print("Hello is am itSelf but self and my name is "+itSelf.name)


# create an object
s1 = Student("Avinash", 21)
s1.name = "Arpita"
del s1
s1.myFunc()
