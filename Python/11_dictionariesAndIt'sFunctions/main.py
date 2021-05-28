# It is unordered (no sequence is required - data or entries have no order)
# It is mutable (values can be changed even after its formation or new data/information can be added
        #     to the already existing dictionary, we can also pop/remove an entry completely)
# It is indexed (Dictionary contains key-value pairs and indexing is done with keys.
        #       Also after the Python 3.7th update the compiler stores the entries in the order they are created)
# No duplication of data (each key is unique; no two keys can have the same name so there is no chance
        #       for a data being overriden)

# its syntax comprises of key and values separated by colons in curly brackets,
# where the key is used as a keyword

# We can store heterogeneous data into our dictionary i.e. numbers, strings, tuples, and the other
# objects can be stored in the same dictionary.
# Different data types can be used in a single list, which can be made the value of some keys in the dictionary. etc.

dict1={'khushi':'doshi','tithi':'shah','birva':'babaria','yukta':'desai'}
print(dict1)
print(dict1['khushi'])#for accessing particular key-element.

# to change value of anykey
dict1['khushi']='patel'
print(dict1)

dict1['khushi']='doshi'
#to add any key value pair
dict1['prince']='vanani'
dict1.update({'aneri':'dhola'})
print(dict1)

#to copy aa dictionary
dict2=dict1
print(dict2)

#another functions
print(dict1.keys())
print(dict1.values())
print(dict1.items())

#we can make dictionary within dictionary
dict3={'khushi':'happiness','rapidly':'speedily','sad':'unhappy','pents':{'khushi':'doshi','yukta':'desai'}}
print(dict3)

dict3={'khushi':'happiness','rapidly':'speedily','sad':'unhappy','pents':'jagins'}
to_find=input("Enter the word to find it's meaning in dictionary")
print('the meaning is:',dict3[to_find])


