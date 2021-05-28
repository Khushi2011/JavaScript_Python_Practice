no=int(input("Enter the number:-"))
bool_number=int(input("choose 0 or 1 for reverse and front printing respectively:-"))
bool_value=bool(bool_number)
# print(bool_value)

if bool_value==True:
    i=0
    while (i<no):
        j=0
        while j<i+1:
                f = open("demo.txt", "a")
                if i==0:
                    f.write("\n")
                f.write("*")
                j=j+1
        f.write("\n")
        i=i+1
        f.close()

    #using for loop
    # for i in range(0,no):
    #     for j in range(0,i+1):
    #         print("*",end="")
    #     print()

    #using while loop
    # while i<no:
    #     j=0
    #     while j<i+1:
    #         print("*",end="")
    #         j+=1
    #     print()
    #     i+=1

if bool_value == False:
    i = no
    while (i >=0 ):
        j = 0
        while j<=i-1:
            f1 = open("demo.txt", "a")
            f1.write("*")
            j = j + 1
        f1.write("\n")
        i = i - 1
    f1.close()
    #using while loop
    # while i>0:
    #     j=0
    #     while j<i-1:
    #         print("*",end="")
    #         j=j+1
    #     print()
    #     i=i-1
