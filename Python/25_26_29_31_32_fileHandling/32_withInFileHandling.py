with open("demo.txt") as f:
    print(f.readlines())

f=open("demo.txt","r")
print(f.readline())
f.close()