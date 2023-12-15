#James Rebholz Final 
#Random Number Guesser 
#This Program will generate a random number, from here then it will prompt the user to guess the number 
#My goal for this program is to get it so that the user has different options to play this game 

#The Program was built from the bottom up
#starting from Hard mode and then adding more on to build both Easy and Medium Mode


#Importing The Random Module
import random
import math

#Variable Declaration
menue = str() #Used to Select the Mode the User wants to play
randomNumber = int() #Will be the number trying to be guessed
roundedRandom = int() #This is the rounded version of the random number, to the nearest tenth
UsersNumber = int() #This is the number that is inputted from the user
UsersNumberSTR = str() #The inputted number convered into a string
WhileCounter = int() #This will keep track of how many guesses the user is on
NumberChecker = bool() #True / False to see if it is a number or not 





#Defining the Random Number
randomNumber = random.randint(1,100)

#Shows the random number -- Commented out 
#print(randomNumber)

#Welcome Screen
print("Please pick a Selection on how you want to play the number game:")
print("1. Easy Mode: Unlimited Guesses with 3 Extra Hints")
print("2. Medium Mode: Unlimited Guesses with NO EXTRA HINTS") 
print("3. Hard Mode: Only Five Guesses with NO EXTRA HINTS")
menue  = input ("Selection: ")
print("----------------")

#***Majority of the comments are in easy mode since it has the most code***
#Easy Mode will give three hints to the user and unlimited guesses
if menue == "1":
    
    #The WhileCounter keeps track of how many times the person has gone through the loop 
         #In the hard mode option it will also limit them on the amount of tries they have
    WhileCounter = 1

    print("Easy Mode")
    while WhileCounter >= 1:

            #Using the WhileCounter it will give the user three hints based off of which one they are on
            if WhileCounter == 1:

                #This First hint will tell the user if the number is Greater or Lesser then 50 
                if randomNumber > 50:
                    print("HINT 1:")
                    print("The Number you are trying to guess is Greater then 50")
                elif randomNumber < 50:
                    print("HINT 1:")
                    print("The Number you are trying to guess is Less then 50")
                elif randomNumber == 50:
                    print("HINT 1:")
                    print("The Number you are trying to guess is DEFINATLY NOT 50 ;)")

            if WhileCounter == 2:

                #The second hint will mod (%) the random number to see if it is equal to 0 if it is then it is an even number
                #This will tell the user if the number they are trying to guess is even or odd
                if ((randomNumber % 2) == 0):
                    print("HINT 2:")
                    print("The Number you are trying to guess is an EVEN Number")
                else:
                    print("The Number you are trying to guess is an ODD Number")

            if WhileCounter == 3:

                #The Third hint will take the number and round it down to the nearest 10 
                #Then it will add 10 that rounded number and give a range that the user can guess between 
                roundedRandom = math.floor(randomNumber/10)*10
                print ("The range of the number you are trying to guess is between: " + str(roundedRandom) + " and " + str(roundedRandom + 10))
           
            if WhileCounter == 100:

                #Pretty self explanatory
                print("You have tried every number and still ccouldn't get it, you lose")
                break

            #This just showed the number of guesses the user has tried based off of the WhileCounter
            print("This Guess #" + str(WhileCounter))

            #Takes the input of the number that the user is trying to guess
            UsersNumber  = int(input("Enter Your Number You Would Like to Guess: "))

            #UserNumberSTR is a place holder to test to see if it's a valid number 
            UsersNumberSTR = UsersNumber

            #By using the .isnumeric you can test strs to see if they are numeric 
            #By using the place holder you can then keep the number inputted an int without having to redefine it later
            NumberChecker = str(UsersNumberSTR).isnumeric()
            
            #If the NumberChecker is returned False from the .isnumeric test it will then promt the user to try again
            #If it returns True then it will move onto the next step which will test to see if it is between 1 and 100
            #If that returns true then it will end with the else statement that will move onto the next part of the code
            #Which is testing to see if the guessed number is the secret number

            if (NumberChecker == False):
                print("Please Enter a Number, Do Not Enter Any Letters, This Includes Negatives")
            elif (int(UsersNumberSTR) <= 0 or int(UsersNumberSTR) >= 101):
                print("Please Enter a Number Between 1 and 100, No Negative Numbers")
            else:

                #If the Users guessed number is equal to the secret number then they found it and they win
                if (UsersNumber == randomNumber):
                    print("CONGRADULATIONS YOU GUESS THE SECRET NUMBER!!!")
                    print("THE SECRET NUMBER WAS: " + str(randomNumber))
                    break

                #If the Users guessed number is smaller then the secret number then, it will tell then user so
                elif (UsersNumber < randomNumber):
                    print("The Number you guess is SMALLER then the secret number")
                    print("Try Again")

                #If the Users guessed number is larger then the secret number then, it will tell then user so
                elif (UsersNumber > randomNumber):
                    print("The Number you guess is LARGER then the secret number")
                    print("Try Again")

            print("----------------")
            WhileCounter += 1

#The only difference is that the Hints from Easy mode are removed but the user still have Unlimtied Guesses
elif menue == "2":

    WhileCounter = 1

    print("Medium Mode")
    while WhileCounter >= 1:

            print("This Guess #" + str(WhileCounter))
            UsersNumber  = int(input("Enter Your Number You Would Like to Guess: "))

            UsersNumberSTR = UsersNumber

            NumberChecker = str(UsersNumberSTR).isnumeric()
            

            if (NumberChecker == False):
                print("Please Enter a Number, Do Not Enter Any Letters, This Includes Negatives")
            elif (int(UsersNumberSTR) <= 0 or int(UsersNumberSTR) >= 101):
                print("Please Enter a Number Between 1 and 100, No Negative Numbers")
            else:
                if (UsersNumber == randomNumber):
                    print("CONGRADULATIONS YOU GUESS THE SECRET NUMBER!!!")
                    print("THE SECRET NUMBER WAS: " + str(randomNumber))
                    break
                elif (UsersNumber < randomNumber):
                    print("The Number you guess is SMALLER then the secret number")
                    print("Try Again")

                elif (UsersNumber > randomNumber):
                    print("The Number you guess is LARGER then the secret number")
                    print("Try Again")

            print("----------------")
            WhileCounter += 1

#The user is limited to 5 guesses by using the hile loop counter as a tracker
#When it gets to the IF Else statements for the Greater then and Less then Portion
    #If the while loop counter is equal to 5 it will then end the program and tell the user the number
elif menue == "3":

    WhileCounter = 1

    print("Hard Mode")
    while WhileCounter < 6:

        print("This Guess #" + str(WhileCounter))
        UsersNumber  = int(input("Enter Your Number You Would Like to Guess: "))

        UsersNumberSTR = UsersNumber

        NumberChecker = str(UsersNumberSTR).isnumeric()
        

        if (NumberChecker == False):
            print("Please Enter a Number, Do Not Enter Any Letters, This Includes Negatives")
        elif (int(UsersNumberSTR) <= 0 or int(UsersNumberSTR) >= 101):
            print("Please Enter a Number Between 1 and 100, No Negative Numbers")
        else:
            if (UsersNumber == randomNumber):
                print("CONGRADULATIONS YOU GUESS THE SECRET NUMBER!!!")
                print("THE SECRET NUMBER WAS: " + str(randomNumber))
                break
            elif (UsersNumber < randomNumber):
                print("The Number you guess is SMALLER then the secret number")

                if (WhileCounter == 5):
                    print("----------------")
                    print("You Lost the game!")
                    print("The Secret Number was: #" + str(randomNumber))
                    print("Maybe Try an Easier Mode")
                else:
                    print("Try Again")

            elif (UsersNumber > randomNumber):
                print("The Number you guess is LARGER then the secret number")

                if (WhileCounter == 5):
                    print("----------------")
                    print("You Lost the game!")
                    print("The Secret Number was: #" + str(randomNumber))
                    print("Maybe Try an Easier Mode")
            else:
                print("Try Again")

        print("----------------")
        WhileCounter += 1
else:
    print("Try Again: Please Select One of the privous options")
