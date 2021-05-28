# i=1
# while(i<=20):
#     print(i,end=" ")
#     i=i+1

#exercise:3
num=20
i=10

while(i<11 and i>=1):
    guess=int(input("Input a number of your guess:-"))
    i=i-1
    if (i == 0):
        print("Game is over!!!,You have 0 guess left!!!")
        exit()
    if guess<20:
        print("Please choose a bigger number than ",guess)
        print("You have ",i,"guesses left")
    elif guess>20:
        print("Please choose a smaller number than ", guess)
        print("You have ", i, "guesses left")
    else:
        print("You guess the correct number")
        exit()
