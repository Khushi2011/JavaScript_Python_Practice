list1=["khushi","manish","rita","shalin"]
count = 1
print("\n")
for name in list1:
    print(count,"name is:-",name)
    count=count+1


list1=[["khushi",20],["manish",54],["rita",50],["shalin",24]]
count = 1
print("\n")
for name,age in list1:
    print(count,"name is:-",name," age is:-",age)
    count=count+1

#to convert list into dictionary
dict1=dict(list1)
print(dict1)
count = 1
print("\n")
for name,age in dict1.items():
    print(count,"name is:-",name," age is:-",age)
    count=count+1
print("\n")
for name in dict1:
    print(name)

print("\n")
items = [int, float, "Khushi", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)