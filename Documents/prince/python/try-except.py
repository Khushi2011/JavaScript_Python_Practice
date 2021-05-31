try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("Divison is :",num1/num2)
except Exception as e: #exception catch in this part if there is exception it will catch and after this all of statement work 
    print(e)
print("This part must  be executed")