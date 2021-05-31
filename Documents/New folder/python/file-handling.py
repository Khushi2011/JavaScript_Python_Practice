#open file
# f=open("prince.txt") #bydefault mode is "rt" in open file and open() return file pointer pointer cannot changed pointng location
# content=f.read()  #if we not give any argument in read() it will read all content of file
# print(content) #read content of file 
# print(len(content))
# content1=f.read(2)
# content1=f.readline() #if we use readline() and again use readline() it will go next line and print
# content1=f.readline()
# print(content1)
# content2=f.readlines()  # readlines() return  line in form of list
# print(content2)
# for line in f:
#     print(line)
# f.write("Hello Everyone,My name is Prince Vanani\ni'm study ddit,nadiad\ndegree is B.tech computer engineering sem 4")
# writeCharcter=f.write("Thank you")  #f.write() return number charcter it will written in file
# print(writeCharcter)
#f.seek(offSet) it will change file pointer pointing position 
#f.tell() it will tell file pointer current pointing position
# print(f.tell())
# print(f.readline())
# f.seek(10)
# print(f.tell())
# print(f.readline())

# f.close()

# file open and close using with
with open("prince.txt") as f:
    a=f.read(6)
    print(a)
f=open("prince.txt")
print(f.read())
f.close()
#if we read all line and again open file it will start from zero position