#Problem Statement:-
# Input Format:A single line containing the string  and integer value  separated by a space.

# Constraints:The string contains only UPPERCASE characters.

# Output Format:Print the different combinations of string  on separate lines.
# Sample Input:
# HACK 2
# Sample Output
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK
a=input("Enter a String:-")
b=int(input("Enter a number:-"))

if b>=0 and b<= len(a):
    count=1
    for i in range(0,b):
        if count==1:
            for k in range(0, b):
                print(a[k])
        for j in range(0,count+1):
            print(a[j],end="")
        print()
        count+=1