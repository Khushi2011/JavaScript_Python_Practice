def argsuse (normal, *args,**kwargskhushi):#we can change name of args ......we can write khushi also in place of args
    print(type(args))#type of args will always tuple even if we pass list.....
    print(normal)
    for name in args:
        print(name)
    for key,value in kwargskhushi.items():
        print(f"name is {key} surname is {value}")

list1=["khushi","manish","rita","shalin"]
normal="hello"
kw={"khushi":"doshi","rita":"doshi","manish":"doshi","shalin":"shah"}
argsuse(normal,*list1,**kw)#first argument will normal argument then *args and then **kwargs argument