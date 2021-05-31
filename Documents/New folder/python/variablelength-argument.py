def varargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{value} is:",key)
l1=["java","python","HTML","JavaScript","Php"] #if we add in list using variable length argument
d1={"Prince":"Coder","Keyur":"Doctor"} #if we add key-value pair in dictionary using variable length argument
varargs("Nothing",*l1,**d1)