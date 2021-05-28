f=open("demo.txt","w")
f.write("Hello!!!Good morning.....")#this will create new file name demo.txt and write the print statement..
# if we run this statements for n times then it will rewrite this n times
f.close()

f = open("demo.txt" , "a")
f.write("Today is 16th May,2021")#if we run this statements for n times then it will append this n times
f.close()

# r+ mode is more of a combination of reading and append than read and write.
# By opening a file in this mode, we can print the existing content on to the screen by printing f.read() function
# and adding or appending text to it using f.write() function.
f = open("demo.txt", "r+")
print(f.read())
f.write(" thank you")
print(f.read())