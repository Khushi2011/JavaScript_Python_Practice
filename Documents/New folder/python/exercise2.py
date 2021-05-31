operator=input("what operation you can perform :")
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

if operator=="*":
    if((num1==45 and num2==3) or(num1==3 and num2==45)):
        print(555)
    else:
        print(num1*num2)
elif operator=="+":
    if((num1==56 and num2==9) or(num1==9 and num2==56)):
        print(77)
    else:
        print(num1+num2)
elif operator=="/":
    if(num1==56 and num2==6):
        print(4)
    elif(num2!=0):
        print(num1/num2)
    else:
        print("Number2 is cannot zero in divison operation!!")
elif operator=="-":
    print(num1-num2)
else:
    print("please select valid operation !")