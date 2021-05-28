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
        return cls(*string.split("-"))

    @staticmethod
    def print_statement(str):
        print(f"Hello!!!You are done.{str}")
        return "Over"


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
# we can use anything in place of -(dash)
karan = Employee.from_dash("Karan-480-Student")
print(karan.no_of_leaves)
karan.print_statement(karan.name)  # we can call it using object instance
Employee.print_statement("khushi")  # we can also call it using classname

# print_statement  is returning over so it will print over
print(karan.print_statement("karan"))
