import random

Number_attamp = 5 




def gamefun():
    global Number_attamp


    print("\nWELCOM TO GUESS GAME IN PYTHON \nGuess 1 to 10 Any Number\n")
    user_input = int(input("Enter Guess Number..... "))
    AI_number = random.randint(1,10)

    if(user_input == AI_number):
         print("\nYOU WIN THIS GAME!")
         
    elif user_input >10:
        print("\nplese input right number\n you have only ",Number_attamp," attempts ")
        if(Number_attamp > 0 ):
            Number_attamp -=1
            gamefun()
        else:
            a = input("\nif you play agen pre (y/n)")
            life_timeadd(a.lower())
    else:
        print("\nYOU LOSS THE GAME! \n you have only ",Number_attamp," attempts ")
        if Number_attamp > 0:
            Number_attamp -=1
            gamefun()
        else:
            a = input("\nif you play agen pre (y/n)")
            life_timeadd(a.lower())
    
def life_timeadd(answer):
    global Number_attamp
    if(answer == "y"):
        Number_attamp = 5
        gamefun()
    else:
        print("\nthanks for playering...\n")    


gamefun()