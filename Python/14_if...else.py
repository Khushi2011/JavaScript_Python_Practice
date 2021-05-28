num1=50
num2=int(input("Enter a number:-"))
if num1 == num2:
    print(num1,"is Equal to",num2)
elif num2 > num1:
    print(num2," is greater than",num1)
else:
    print(num1," is greater than",num2)

list1=[5,8,10,12,4,7]
if 5 in list1:
    print("5 exists in ",list1)
if 20 not in list1:
    print("20 does not exist in ",list1)

#Excersice 2-Faulty Calculator
num1=int(input("Enter a num1:-"))
num2=int(input("Enter a num2:-"))
oper=input("Enter an operator:-")
if oper=='+' and num1==56 and num2==9:
    print("Ans is: 70")
elif oper=='+':
    print("Ans is: ",num1+num2)
elif oper=='*' and num1==45 and num2==3:
    print("Ans is: 70")
elif oper == '*':
    print("Ans is: ", num1 * num2)
elif oper=='/' and num1==56 and num2==6:
    print("Ans is: 70")
elif oper=='/':
    print("Ans is: ",num1/num2)
