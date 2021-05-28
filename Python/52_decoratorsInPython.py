# def function1():
#     print("Subscribe now")
#
# func2 = function1
# del function1
# func2()#even if we delete original function it will not delete it's copy
#

#decorators
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def what_is_sum():
    print("Sum is:-",76+24)

khushi=what_is_sum()