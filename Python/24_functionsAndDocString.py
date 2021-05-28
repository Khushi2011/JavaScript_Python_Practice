def ave(a,b):
    '''This function is doing average of 2 numbers'''
    ans=(a+b)/2
    return ans
num1=int(input("Enter 1st number:-"))
num2=int(input("Enter 2nd number:-"))
ans=ave(num1,num2)
print("Average is:-",ans)
print("discription is:-",ave.__doc__)