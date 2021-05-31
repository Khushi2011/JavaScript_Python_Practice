dictionary = {
    "mutable": "changed after creation",
    "immutable": "can not change after creation",
    "set": "set is collection of object",
    "dictionary": "it is key-value pair",
    "list": "list is mutable iterative collection object",
    "tuple": "tuple is immutable iterative collection object"
}
print("Please select keys from dictionary it is :", dictionary.keys())
inputKey = input("Please Enter key you want to know about it:")
if(inputKey in dictionary.keys()):
    print(dictionary[inputKey])
else:
    print("please select valid key!!")
