mydict={
    "Fname":"prince",
    "Lname":"vanani",
    "branch":"CE",
    "sem":4,
    "sem":4,
}
set1={1,2,3,"prince"}
# print(len(set1)) #find length of set
# print(type(set1))
# print(set1)
# set.clear() #clear set not delete object
set2=set((1,2,3,4,5)) #creation of set using constructor
# print(set2)
# set1.remove(4) #if there is no matching element with argument in set and we remove it it wii give an error in this method
# set1.discard(4)  #if there is no matching element with argument in set and we remove it it wii  not give an error in this method
set1.add(5) #add an element into sets
set1.update(mydict) #update method take itreable object list,tuple,set,dictionary,etc
print(set1)