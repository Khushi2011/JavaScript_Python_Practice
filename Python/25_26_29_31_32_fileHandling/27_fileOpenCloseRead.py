# reading from the file
f=open("26_IO_Basics.txt","rt")
text=f.read()
print(text)
print("\n")
f.close()

# for reading specific characters
print("-------------------------------------------------------")
f=open("26_IO_Basics.txt","rt")
print("for reading specific characters")
text=f.read(20)
text2=f.read(20)
print(text)
print(text2)
f.close()

# to get output line by line
print("-------------------------------------------------------")
f=open("26_IO_Basics.txt","rt")
for line in f:
    print(line,end="")
f.close()

# readline() function
print("\n-------------------------------------------------------")
f=open("26_IO_Basics.txt","rt")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print("\n-------------------------------------------------------")
print(f.readlines())#it will create a list
f.close()

