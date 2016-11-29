import mods
import random

# InsideBet: Contains everything for inside bets
# outsideBet: Contains everything for outside bet
# selectingANumber: produces a random number for the table

def insideBet(player,num,betCount):
    # If no cash, cant bet
    if player[num][1] == 0:
        print('Insufficient funds')
        return
    
    selection = mods.valueChecker('\n\nWhat kind of inside be would you like to place?', 1, 5, 'i')
    
    if selection == 1:
        
        numberSelect = mods.valueChecker('What number would you like to bet on?', 0, 36, 'i')
        
        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')
        
        
        
        return {betCount: [numberSelect ,bet,35]}
    
    elif selection == 2:
        
        number1 = mods.valueChecker('Whats the first number you would like to bet on?', 1, 36, 'i')
        
        while True:
            number2 = mods.valueChecker('Whats the second number you would like to bet on?', 1, 36, 'i')
            
            # This checks to make sure number2 is next to number1 on the table
            if number2 == number1 - 1 or number2 == number1 + 1 or number2 == number1 + 3 or number2 == number1 - 3:
                break
            
            # If the second number is not next to the firsrt number, it will print this before looping again.
            print("Select another number. The second number is not next to the first number!")
        # This will make it so numberSelect which is returned is a list of the numbers the player selected to bet with
        numberSelect  = []
        numberSelect.append(number1)
        numberSelect.append(number2)
        
        # Asks for the bet
        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')
        
        
        
        return {betCount: [numberSelect ,bet,17]}
        
    elif selection == 3:
        # Initial location selection
        number1 = mods.valueChecker('Whats the first number you would like to bet on?', 1, 36, 'i')
        
        # number2 represents the number that encloses the second number
        while True:
            
            number2 = mods.valueChecker('Whats the second number you would like to bet on?', 1, 36, 'i')
            
            # based on what number2 equals, develop the inbetween value
            if number2 == number1 - 2:
                number3 = number1 - 1
                print('\nThe inbetween number is:',number3)
                break
            elif number2 == number1 + 2:
                number3 = number1 + 1
                print('\nThe inbetween number is:',number3)
                break
            elif number2 == number1 + 6:
                number3 = number1 + 3
                print('\nThe inbetween number is:',number3)
                break
            elif number2 == number1 - 6:
                number3 = number1 - 3
                print('\nThe inbetween number is:',number3)
                break
            

        
        
               
            # If the second number is not next to the firsrt number, it will print this before looping again.
            print("Select another number. The second number given does not close the street")
        # This will make it so numberSelect which is returned is a list of the numbers the player selected to bet with
        numberSelect  = []
        numberSelect.append(number1)
        numberSelect.append(number2)
        numberSelect.append(number3)
        
        # Asks for the bet
        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')
        
        
        
        return {betCount: [numberSelect ,bet,11]}



    elif selection == 4:
    
        while True:
            number1 = mods.valueChecker('Whats the bottom left corner you would like to bet on of the square?', 1, 32, 'i')
            if not number1%3 == 0:
                break
            else:
                print('That is an unacceptable position')
            
        number2 = number1 + 1
        number3 = number1 + 3
        number4 = number1 + 4
            
            
        numberSelect  = []
        numberSelect.append(number1)
        numberSelect.append(number2)
        numberSelect.append(number3)
        numberSelect.append(number4)
    
        # Asks for the bet
        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')
        
        
        
        return {betCount: [numberSelect ,bet,8]}
    
    elif selection == 5:
    
        while True:
            number1 = mods.valueChecker('Whats the bottom left corner you would like to bet on of the double street?', 1, 29, 'i')
            if not number1%3 == 0:
                break
            else:
                print('That is an unacceptable position')
            
        number2 = number1 + 1
        number3 = number1 + 3
        number4 = number1 + 4
        number5 = number1 + 6
        number6 = number1 + 7
            
            
        numberSelect  = []
        numberSelect.append(number1)
        numberSelect.append(number2)
        numberSelect.append(number3)
        numberSelect.append(number4)
        numberSelect.append(number5)
        numberSelect.append(number6)
    
        # Asks for the bet
        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')
        
        
        
        return {betCount: [numberSelect ,bet,5]}

def outsideBet(player,num,betCount):
    
    # Outcomes necessary for defining what are the outside bets
    numberValues = {0: None, 1: 'r', 2: 'b', 3: 'r', 4: 'b', 5: 'r', 6: 'b', 7: 'r', 8: 'b', 9: 'r', 10: 'b', 11: 'b' , 12: 'r', 13: 'b', 14: 'r', 15: 'b', 16: 'r', 17: 'b', 18: 'r', 19: 'r', 20: 'b', 21: 'r', 22: 'b', 23: 'r', 24: 'b',  25: 'r', 26: 'b', 27: 'r', 28: 'b', 29: 'b', 30: 'r', 31: 'b', 32: 'r', 33: 'b', 34: 'r', 35: 'b', 36: 'r'}
    
    # If no cash, can't bet
    if player[num][1] == '0':
        print('Insufficient funds')
        return
    
    
    selection = mods.valueChecker('\n\nWhat kind of outside bet would you like to place?', 1, 5, 'i')
    
    if selection == 1:
        
        select = mods.valueChecker('Would you like to bet on red or black? (1 - Black, 2 - Red)', 1, 2, 'i')
        numberSelect = []
        
        if select == 1:
            for key in numberValues:
                if numberValues[key] == 'b':
                    numberSelect.append(key)
        elif select == 2:
            for key in numberValues:
                if numberValues[key] == 'r':
                    numberSelect.append(key)
                    
        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')

        return {betCount: [numberSelect ,bet,1]}

    elif selection == 2:
        select = mods.valueChecker('Would you like to bet on which dozen? (1st Dozen - 1, 2nd Dozen - 2, 3rd Dozen - 3)', 1, 3, 'i')
        numberSelect = []
        
        if select == 1:
            for nu in range(1,13):
                numberSelect.append(nu)
        elif select == 2:
            for nu in range(13,25):
                numberSelect.append(nu)
        elif select == 3:
            for nu in range(25,37):
                numberSelect.append(nu)
                    
        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')

        return {betCount: [numberSelect ,bet,1]}
    
    elif selection == 3:
        select = mods.valueChecker('Would you like to bet low (1 - 18 = 1) or high (19 - 36 = 2)', 1, 2, 'i')
        numberSelect = []
        
        if select == 1:
            for nu in range(1,19):
                numberSelect.append(nu)
        elif select == 2:
            for nu in range(19,37):
                numberSelect.append(nu)

        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')

        return {betCount: [numberSelect ,bet,1]}
    
    elif selection == 4:
        
        select = mods.valueChecker('Would you like to bet odd or even (1,2)', 1, 2, 'i')
        numberSelect = []
        
        if select == 1:
            for nu in numberValues:
                if nu == 0:
                    continue
                
                if not nu%2 == 0:
                    numberSelect.append(nu)
        elif select == 2:
            for nu in numberValues:
                if nu == 0:
                    continue
                
                if nu%2 == 0:
                    numberSelect.append(nu)

        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')

        return {betCount: [numberSelect ,bet,1]}
    
    elif selection == 5:
        select = mods.valueChecker('Would you like to bet on which column? (First Column:1, Second Column:2, Third Column:3)', 1, 3, 'i')
        numberSelect = []
        
        if select == 1:
            for nu in range(1,37,3):
                numberSelect.append(nu)
        elif select == 2:
            for nu in range(2,37,3):
                numberSelect.append(nu)
        elif select == 3:
            for nu in range(3,37,3):
                numberSelect.append(nu)
                    
        bet = mods.valueChecker('How much would you like to bet?', 0.01, player[num][1], 'f')

        return {betCount: [numberSelect ,bet,2]}
    
def selectingANumber():
    
    theNumber = random.randint(0,37)
    
    return theNumber
