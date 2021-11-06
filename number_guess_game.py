#Build a number guessing game
#import random to specify the range of INTEGERS for the game
#the user will have to specify the number range for the game, using two numbers
#the system will take a random number from the range specified by the user, and the user will have to guessing
#the user will get a limited number of guesses to perform

import random

def menu(): # this will run the program
    print("Welcome to the number guessing game!\n") #introduction
    ans=str(input("Hit 'Y' to start or 'N' to exit: ")) #lets user make a choice if they want to play
    ans=ans.upper() #ensures the answer goes through the loop
    while(ans != 'N'):
        result=play()
        print(f"Solution: {result}") #informs the user how well they did in the game
        ans=str(input("Want to keep playing? Hit 'Y' or 'N': ")).upper() #will change this to a uppercase letter after input
        #ans allows the loop to continue or exit depending on the user's reply


def user_choice(): #the user will enter a number for the range
    num1=int(input("Enter a number for the starting range: "))
    num2=int(input("Enter a number for the end range: "))
    print(f"You entered {num1} as start and {num2} as end")
    return specify_range(num1, num2+1) #this will return the selected value the system picks

def specify_range(start, end): #this program will run on the start and end values for the range
    selected=random.randint(start, end) #the system randomly selects a random number
    return selected

def play():
    sysnum=user_choice() #this uses the value from specify_range function that the player will guesses
    #print("System num is: ",sysnum)
    guessNum=3 #the player will get three chances to guessNum
    points=0
    #we will use a while loop
    while(guessNum > 0):
        choice=int(input("\nGuess a number: "))
        if(choice==sysnum):
            print("You got it correct!\n")
            points+=1
            sysnum=user_choice() #will pick a new number
        elif(choice > sysnum):
            print("Try again! You guessed too high!")
        elif(choice < sysnum):
            print("Try again! You guessed too low!")
        guessNum-=1 #will subtract 1 each time regardless of correct or incorrect
    if(guessNum < 3):
        guessNum=3 #reset it
    if(points > 0 and points < guessNum):
        return "You got some correct"
    elif(points ):
        return "You got everything correct"
    elif(points==0):
        return "You didn't get anything correct."

