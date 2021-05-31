patternLine=int(input("Enter number of lines do you want print pattern:"))
print("1")
for i in range(patternLine):
        for j in range(patternLine):
            if(j>=patternLine-i-1):
                print("*",end=" ")
        print()
print("2")
for i in range(patternLine):
        for j in range(patternLine):
            if(j<=i):
                print("*",end=" ")
        print()
print("3")

print("4")
for i in range(patternLine):
        for j in range(patternLine-i):
                print("*",end=" ")
        print()
