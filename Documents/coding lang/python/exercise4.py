patternLine=int(input("Enter number of lines do you want print pattern:"))
typeOfPattern=int(input("Enter pattern type you want print True for upward and False for downward:"))
boolPattern=bool(typeOfPattern)
if(boolPattern==True):
    for i in range(patternLine):
        for j in range(patternLine):
            if(j<=i):
                print("*",end=" ")
        print()
else:
    for i in range(patternLine):
        for j in range(patternLine-i):
                print("*",end=" ")
        print()