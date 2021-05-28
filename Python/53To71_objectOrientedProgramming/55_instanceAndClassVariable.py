# The __dict__ attribute
# Every object in Python has an attribute which is denoted by __dict__, it maps the attribute name to its value.
# This dictionary is used to stores all the attributes defined for the object itself.
#
# Following is the syntax of using __dict__:
# object.__dict__

# Instance, variables are createdonly for a specific object.The object can change, create, or update only its
# instance variables.While in the case of class variables, the variables and values we create or define are set
# as default for all the objects.The objects cannot change the value or variable in the class by just updating
# it using object_name.class_name.However, it can change the values of their particular instance variables.
# Making use of class and instance variables can ensure that our code adheres to the DRY (don't repeat yourself)
# principle to reduce repetition within code.


class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print("Employee.no_of_leaves:-",Employee.no_of_leaves)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print("Employee.no_of_leaves:-",Employee.no_of_leaves)

harry.no_of_leaves=10
print("harry.no_of_leaves:-",harry.no_of_leaves)
print("Employee.no_of_leaves:-",Employee.no_of_leaves)
print("rohan.no_of_leaves:-",rohan.no_of_leaves)
print(rohan.__dict__)
print(harry.__dict__)


