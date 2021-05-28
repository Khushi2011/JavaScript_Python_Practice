# The self keyword is used in the method to refer to the instance of the current class we are using.
# The self keyword is passed as a parameter explicitly every time we define a method.
# def read_number(self):
#         print(self.num)

# __init__ method:-
# "__init__" is also called as a constructor in object-oriented terminology. Whereas a constructor is defined as:
# "Constructor in Python is used to assign values to the variables or data members of a class when an
# object is created."

class person:
    def print_details(self):
        return f"Name is {self.name} and Age is {self.age}"
    pass


khushi = person()
khushi.name = "Khushi Doshi"
khushi.age = 20

tithi = person()
tithi.name = "Tithi Shah"
tithi.age = 21

print(khushi.print_details())
print(tithi.print_details())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
p2 = Person("Khushi", 20)
p3 = Person("Tithi", "21")
print(p1.name)
print(p2.age)
