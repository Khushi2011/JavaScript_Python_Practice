# f.tell() returns an integer giving the file pointer current position in the file represented as a number of bytes.
# File Pointer/File Handler is like a cursor, which defines from where the data has to be read or written in the file.

# Syntax:  file_pointer .seek(offset, whence).
# Offset:   In seek() function, offset is required. Offset is the position of the read/write pointer within the file.
# Whence: This is optional. It defines the point of reference. The default is 0, which means absolute file positioning.

f=open("demo.txt","rt")

print(f.tell())
print(f.readline())

f.seek(20)
print(f.readline())
f.close()

# f=open("26_IO_Basics.txt","a")
# text=input("Enter string:-")
# f.write(text)
# f.close()
#
# f=open("26_IO_Basics.txt","r")
# print(f.readlines())
# f.close()

