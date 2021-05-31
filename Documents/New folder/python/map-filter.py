# 1. map
# l1=["1","2","3","4","5"]
# for i in range(len(l1)):
#     l1[i]=int(l1[i])
# l1[2]=l1[2]+10 
#instead of this we can use map for convert type or apply function to iterable return object map(function,iterable )
# number=list(map(int,l1))
# number[2]=number[2]+10
# print(number[2]) 
 
#another demo
# def sq(x):
#     return x*x

# l1=[1,2,3,4,5]
# l1=list(map(sq,l1))
# print(l1)
#instead of this we can use lamda function
# l1=[1,2,3,4,5]
# l1=list(map(lambda x:x*x,l1))
# print(l1)
#another example
# def square(x):
#     return x*x
# def cube(x):
#     return x*x*x
# func=[square,cube]
# n1=[1,2,3,4,5]
# for i in range(len(n1)):
#     val=list(map(lambda fun:fun(n1[i]),func))
#     print(val)

# 2.Filter
# def is_greater_5(num):
#     return num>5
# l1=[1,2,3,4,5,6,7,8,9]
# num=list(filter(is_greater_5,l1))
# print(num)

# 3.Reduce
from functools import reduce

l1=[1,2,3,4]
# sum=0
# for i in range(len(l1)):
#     sum +=l1[i]
# print(sum)

sum=reduce(lambda x,y:x+y,l1)
print(sum)