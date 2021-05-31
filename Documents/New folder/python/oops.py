class Employee:
    classVaribale=9
    def __init__(self,name,salary) :
        self.name=name
        self.salary=salary
    def printdetails(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

prince=Employee("prince",39000)
# prince.name="Prince"
print(prince.printdetails())
# print(prince.classVaribale)
# print(prince.__dict__)
# prince.classVaribale=8  #instance cannot change class variable it will create own instance variable and change we can change using class for class variable
# print(prince.__dict__)
# print(prince.classVaribale)
# print(Employee.classVaribale)