# def function1():
#     # l=5
#     m=8
#     global l
#     l=l+50
#     print(l,m)
# l=10
# function1()
# print(l) 
# global keyword use for change value of global variable 

def function2():
    x=20
    def function3():
        global x   #global x it will check globally not locally if not present it will create that variable
        x=88
        print(x)
    print(x)
    function3()
    print(x)
function2()
print(x)