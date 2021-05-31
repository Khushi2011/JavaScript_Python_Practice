actualNumber =20
totalGuess=9
takenGuess=0
while(True): 
    guessNumber=int(input("Guess a Number :"))
    takenGuess=takenGuess+1
    if(totalGuess>takenGuess):
        if(actualNumber==guessNumber):
            print("You take number of guess is:",takenGuess)
            print("You successfully Guess Number!")
            break
        elif(actualNumber>guessNumber):
            print("Your guess number is smaller than actual number\n","No of guess left is :",totalGuess-takenGuess)
        elif(actualNumber<guessNumber):
            print("Your guess number is greater than actual number\n","No of guess left is :",totalGuess-takenGuess)
    elif (totalGuess==takenGuess):
        print("Sorry Your guess is over!!")
