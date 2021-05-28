# To declare a class as private, we use a double underscore “_­_” sign before the data members of the class.
class employee:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age  # private attribute

# To declare a class as protected, we use a single underscore “_” sign before the data members of the class.
class employee:
    def __init__(self, name, age):
        self._name = name  # protected attribute
        self._age = age  # protected attribute

#public modifier
class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Public -
# Protected -
# Private -

class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __pr = 98

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp = Employee("harry", 343, "Programmer")
# print(emp.__pr)#it will give error
print(emp._Employee__pr)#private variable access

print(emp._protec)#protected variable access

print(emp.var)#public variable access
