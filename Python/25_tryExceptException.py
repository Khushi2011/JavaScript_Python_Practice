num1=input("Enter a value:-")
num2=input("Enter a value:-")
try:
    print("Sum is:-",int(num1)+int(num2))
    print("division is:-",int(num1)/int(num2))
except Exception as e:
    print("Exception is:-",e)