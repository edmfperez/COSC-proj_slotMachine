
# Functions that are used globally and are not specific to a game
import mods
import Roulette2


# Welcome the user
print('''
\tWelcome to the Casino!
\n\tYou will be able to choose \n\tfrom three games and save \n\tyour winnings (if you win, \n\tthat is) as you play along.
''')
# Loops through the entire program
select = True
while select:
    print('''\nHere are your options:

    1 - Play Roulette
    2 - Play Slots
    3 - Check all Scores
    4 - Create new login
    5 - Quit

    ''')
    # What does the user want to do
    select = mods.valueChecker('What would you like to play', 1, 6, 'i')
    
    # If 1 go to Roulette2 and run roul
    if select == 1:
        
        Roulette2.roul()
    
    # If 2 run the lsots machine program
    elif select == 2:
                
        import random
        import time
        import mods
        
        # imports
        diction = mods.openSaveFile()
        players = mods.playerSelectOne(diction)
        
        # shows user what each slot combination pays out
        print('''Welcome to the Slot Machine 
        You'll start with the money with the user. You'll be asked if you want to play.
        Answer with yes/no. you can also use y/n
        There is no case sensitivity, type it however you like!
        To win you must get one of the following combinations:
        BAR\tBAR\tBAR\t\tpays\t$250
        BELL\tBELL\tBELL/BAR\tpays\t$20
        PLUM\tPLUM\tPLUM/BAR\tpays\t$14
        ORANGE\tORANGE\tORANGE/BAR\tpays\t$10
        CHERRY\tCHERRY\tCHERRY\t\tpays\t$7
        CHERRY\tCHERRY\t  -\t\tpays\t$5
        CHERRY\t  -\t  -\t\tpays\t$2
        7\t  7\t  7\t\tpays\t The Jackpot!
        
        
        ''')
        time.sleep(10)
        #Constants:
        initialState = players[1][1]
        initialBalance = mods.jackpotOpen()
        items = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR", "7"]
        
        # constants for the slots
        firstWheel = None
        secondWheel = None
        lastWheel = None
        stake = initialState
        balance = initialBalance
        
        # logic for the slot mechanism
        def play():
            # calls on global variables of stake and the three wheels
            global stake, firstWheel, secondWheel, lastWheel
            playQuestion = askPlayer()
            # loops through the spinning of the wheels
            while(stake != 0 and playQuestion == True):
                firstWheel = spinWheel()
                secondWheel = spinWheel()
                lastWheel = spinWheel()
                # prints the score based on the combination
                printScore()
                # asks the player if they want to play again
                playQuestion = askPlayer()
        
        def askPlayer():
            '''
            Asks the player if he wants to play again.
            expecting from the user to answer with yes, y, no or n
            No case sensitivity in the answer. yes, YeS, y, y, nO . . . all works
            '''
            # calls on each variable from outside the function
            global stake
            global balance
            while(True):
            
                # resets the jackpot once all the money has been won
                if (balance <=1):
                    print ("Machine balance reset. The jackpot is gone")
                    balance = balance
                
                # tells the user what the current jackpot is; asks the user what they would like to do
                print ("The Jackpot is currently: $" + str(balance) + ".")
                answer = input("Would you like to play? Or check your money?: ")
                answer = answer.lower()
                
                # makes user input really simple
                if(answer == "yes" or answer == "y" or answer == 'play' or answer == 'PLAY' or answer == 'Play'):
                    return True
                elif(answer == "no" or answer == "n"):
                    print("You ended the game with $" + str(stake) + " in your hand. Great job!")
                    mods.jackpotClose(balance)
                    
                    players[1][1] = stake
                    
                    mods.writeToSave(players, diction)
                    
                    time.sleep(5)
                    return False
                # lets user check their current balance
                elif(answer == "check" or answer == "CHECK"):
                    print ("You currently have $" + str(stake) + ".")
                else:
                    print("Whoops! Didn't get that...")
        
        # logic for wheel spin
        def spinWheel():
            '''
            returns a random item from the wheel
            '''
            randomNumber = random.randint(0, 5)
            return items[randomNumber]
        
        # it looks complex, but really they're all a bunch of if-conds that appropriate scores based on combinations; pretty self-explanatory
        def printScore():
            '''
            prints the current score
            '''
            global stake, firstWheel, secondWheel, lastWheel, balance
            if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
                win = 2
                balance = balance - 2
            elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (lastWheel != "CHERRY")):
                win = 5
                balance = balance - 5
            elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (lastWheel == "CHERRY")):
                win = 7
                balance = balance - 7
            elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((lastWheel == "ORANGE") or (lastWheel == "BAR"))):
                win = 10
                balance = balance - 10
            elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((lastWheel == "PLUM") or (lastWheel == "BAR"))):
                win = 14
                balance = balance - 14
            elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((lastWheel == "BELL") or (lastWheel == "BAR"))):
                win = 20
                balance = balance - 20
            elif((firstWheel == "BAR") and (secondWheel == "BAR") and (lastWheel == "BAR")):
                win = 250
                balance = balance - 250
            elif((firstWheel == "7") and (secondWheel == "7") and (lastWheel == "7")):
                win = balance
                balance = balance - win
            else:
                win = -1
                balance = balance + 1
        
            # controls what happens when the user wins the jackpot
            stake += win
            if win == balance:
                print ("You won the JACKPOT!!")
            if(win > 0):
                print(firstWheel + '\t' + secondWheel + '\t' + lastWheel + ' -- You win $' + str(win))
                time.sleep(3)
        
            else:
                print(firstWheel + '\t' + secondWheel + '\t' + lastWheel + ' -- You lose')
                time.sleep(2)
            # NOTE: for all the time.sleeps, pausees the game on purpose to let the user read
        
        play()
    
    # If three run the check score function
    elif select == 3:
        mods.checkScores()
    # If 4 run the addNewUser def
    elif select == 4:
        mods.addNewUser()
    # If 5 exit
    elif select == 5:
        print('Thanks for playing!')
        exit()
    # No comprhende 
    else:
        print('I didn\'t get that...')