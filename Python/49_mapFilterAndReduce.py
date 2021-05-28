# map():
# "A map function executes certain instructions or functionality provided to it on every item of an iterable."

# SYNTAX:
# map(function, iterable)
numbers = ["3", "34", "64"]

#using simple for loop
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers[2] = numbers[2] + 1
print(numbers[2])

#using map
numbers = list(map(int, numbers))
def sq(a):
    return a*a
num = [2,3,5,6,76,3,3,2]
square = list(map(sq, num))
print(square)

#using lambda function
num = [2,3,5,6,76,3,3,2]
square = list(map(lambda x: x*x, num))
print(square)

def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
num = [2,3,5,6,76,3,3,2]
for i in range(8):
    val = list(map(lambda x:x(i), func))
    print(val)

# filter():-
# "A filter function in Python tests a specific user-defined condition for a function and returns an iterable "
# "for the elements and values that satisfy the condition or, in other words, return true."
# --------------------------FILTER------------------------------
list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)

a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c= list(filter(lambda x: x in a, b))
print(c)

# reduce():
# "Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant".
from functools import reduce

list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x+y, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)