# in we write multiple if  in code and if condition is true, it will check all if .

l1 = [1, 2, 3, 4, 5]
# print(15 not in l1)
# in and not in use for checking element is in or not

age = int(input("Enter your age: "))
if age > 0 and age < 100:
    if age > 18:
        print("your age is greater than 18 so you can drive")
    elif age == 18:
        print("your age is equal to 18 so we cannot decide you can drive or not")
    else:
        print("your age is lesser than 18 so you cannot drive")
else:
    print("enter valid Age!!")


#short hand if-else

# a=int(input("enter a:"))
# b=int(input("enter b:"))
# # if a>b : print("A is greater than B")
# print("A is less than B") if a<b else print("A is greater than B")