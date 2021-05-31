# def function1():
#     print("my name is prince")
# fun2=function1
# del function1  # if we delete because it will create copy so it will give output if  we delete function1
# fun2()
# def function2(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a=function2(0)
# print(a)
# def executor(fun):
#     fun("Nothing")
# executor(print)
# simple decorators 
# def dec1(func1):
#     def nowexec():
#         print("Executing now")
#         func1()
#         print("Executed")
#     return nowexec
# @dec1
# def who_is_prince():
#     print("Prince is good person")
# # who_is_prince=dec1(who_is_prince) #instead of this we can use @decorator-name
# who_is_prince()

def dec1(func1):
    def nowexec1():
        print("Executing1 now")
        func1()
        print("Executed1")
    return nowexec1
def dec2(func2):
    def nowexec2():
        print("Executing2 now")
        func2()
        print("Executed2")
    return nowexec2
@dec1
@dec2
def who_is_prince():
    print("Prince is good person")
# who_is_prince=dec1(who_is_prince) 
who_is_prince()

