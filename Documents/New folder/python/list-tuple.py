l1=[1,"prince",True,3+1j] #mixed list
l2=[1,2,5,43,6,9,5,5]
# l2.sort()  #sort list into increasing order
# l2.reverse() #reverse list
# print(l2.count(5))
# l2.extend(3)
print(len(l2))
# l2[2]=3 #list is mutable 
print(l2.index(5))
print(l2)
#list using constructor
constructorList=list(("a","b","c"))
print(constructorList)
# del l2
# print(l2)
# tuple is immutable property same as list
l1=(1,2,3,"prince")
l1=(1,1,2,3,4,2)
# l1=(1,) #type is tuple
# l1=(1) #type is int not tuple
print(l1.index(2))
print(l1.count(2))
# l1.append(6) #tuple not contain method append
print(l1)
#tuple creation using constructor
constructorTuple=tuple(("a","b","c","d"))
print(constructorTuple)
#if we want update or change tuple we can change convert into list then change it after convert into tuple
