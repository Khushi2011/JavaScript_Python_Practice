# They are very different from static methods as they are limited in their functionality to the class
# they are built-in.
# They can be called by using the class name and also can be accessed by using the object.

# cls. Class methods take cls parameter that points to the class and not the object instance
# when the method is called.
# Syntax:
# class myClass:
#     @classmethod
#     def myfunc (cls, arg1, arg2, ...):
#                           ....


class Employee:
    no_of_leaves = 8

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
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

print(karan.no_of_leaves)
rohan.change_leaves(34)
print(harry.no_of_leaves)
print(Employee.no_of_leaves)
