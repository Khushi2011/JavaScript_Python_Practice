#Docstring means multiline comment into function
def function1(p):
    return f"Hello, Good morning {p}"
def function2(a):
    a=2
    return a
# def function2(a,b):
#     """This is Doc string of Average function """
#     return (a+b)/2
if __name__=='__main__':
    a=5
    # print(function2(5,7))
    # print(a)
    print(function2(a))
    print(a)
# print(function1.__doc__)

#variable length function
# def printNumber(arg1,*vartuple):
#     """This function is used for varibale length arguments"""
#     print(arg1)
#     for var in vartuple:
#         print(var)
# printNumber(1)
# printNumber(1,2,3,4)

#anonymous function 
# lambda function equal
# for example
# def sum(a,b):
#     return a+b
# sum=lambda arg1,arg2: arg1+arg2
# print(sum(2,3))

# a=[[3,8],[1,6],[2,9]]
# a.sort(key=lambda x : x[1])
# a=[3,2,1]
# a.sort()
# print(a)
