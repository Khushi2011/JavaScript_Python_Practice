# Sets are iterable(iterations can be performed using loops)
# They are mutable (can be updated by adding or removing entries)
# There is no duplication (two same entries do not occur)

# Structure:
# Elements of the sets are written in between two curly brackets and are separated with a comma, and in this simple way, we can create a set in Python.
# The other way of forming a set is by using a built-in set constructor function.

#limitations
# Once a set is created, you can not change any of its items, although you can add new items or remove
        # previous but updating an already existing item is not possible.
# There is no indexing in sets, so accessing an item in order or through a key is not possible,
        # although we can ask the program if the specific keyword we are looking for is present in the set
        # by using “in” keyword or by looping through the set by using a for loop.

#to create a set
Veggie_set = {"Drumstick","Cabbage","Cauliflower"}
print(type(Veggie_set))
print((Veggie_set),"\n")

#to add and remove element.
Veggie_set.add("Lady Finger")
print((Veggie_set),"\n")
Veggie_set.remove("Lady Finger")
print((Veggie_set),"\n")

#other methods
new_set = Veggie_set.copy()
print("Copy of set:-",new_set,"\n")

Veggie_set1 = {"Drumstick","Cabbage","Cauliflower"}
Veggie_set2 = {"Brocoli","Corn","Cabbage"}
New_set = Veggie_set1.difference(Veggie_set2)
print("Difference is:-",New_set)
New_set = Veggie_set2.difference(Veggie_set1)
print("Difference is:-",New_set,"\n")

Veggie_set1.discard("Cauliflower")
print("After discarding:-",Veggie_set1,"\n")

Veggie_set1 = {"Drumstick","Cabbage","Cauliflower"}
set_to_remove = {"Cauliflower","Cabbage"}
New_set = Veggie_set1.difference(set_to_remove)
print("Difference is:-",New_set,"\n")

Veggie_set1 = {"Drumstick","Cabbage","Cauliflower"}
print(Veggie_set1)
Veggie_set2 = {"Cauliflower","Cabbage","Lady-finger"}
print(Veggie_set2)
New_set = Veggie_set1.intersection(Veggie_set2)
print("Intersection is:-",New_set,"\n")

Veggie_set1 = {"Cabbage","Cauliflower"}
print(Veggie_set1)
Veggie_set2 = {"Cauliflower","Cabbage","Lady-finger"}
print(Veggie_set2)
Eval = Veggie_set1.issubset(Veggie_set2)
print("IS subset is:-",Eval,"\n")

Veggie_set1 = {"Cabbage","Cauliflower"}
print(Veggie_set1)
Veggie_set2 = {"Cauliflower","Cabbage","Lady-finger"}
print(Veggie_set2)
check1 = Veggie_set1.issuperset(Veggie_set2)
print(check1)
check2 = Veggie_set2.issuperset(Veggie_set1)
print(check2,"\n")

# Veggie_set.clear()
# print(Veggie_set)
