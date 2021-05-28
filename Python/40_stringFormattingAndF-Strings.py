#1 String Formatting (% Operator)
name="Jack"
n="My name is %s"%name
print(n)

#2 Using Tuple ()
name="Jack"
cla=5
s="%s is in class %d"%(name,cla)
print(s)

#3  String Formatting (str.format)
# Syntax: {}.format(values)
str = "This article is written in {} "
print (str.format("Python"))

#4 Using f-Strings ( f ):
## declaring variables

str1="HOME!!!"
str2="Ratnakunj"
print(f"Welcome to our {str1} {str2} ")