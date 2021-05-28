global_var=80 #global variable
def fun1():
    global_var=100 #global variable redefined
    print("1:-",global_var)#it will give output 100
fun1()

def fun2():
    #global_var+=1#here we have not redefined globar_var,so we can't increament it....this will give error
    print("2:-",global_var)#it will give output 80
fun2()

def fun3():
    global global_var
    global_var+=5#after declaring global keyword ,we can do this
    print("3:-",global_var)#it will give output 85
fun3()

x = 89 #if we don't define this then it will get create varible x of global scope with the value 88 here.
def khushi():
    x = 20
    def doshi():
        global x
        x = 88 #this will redefine global variable x to 88 from 89
    print("before calling doshi()", x)
    doshi()
    print("after calling doshi()", x)

khushi()
print(x)