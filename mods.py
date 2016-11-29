
# PlayerSelect: Sifts through dictionary to give a dictionary with only certiain players
# valueChecker: Checks if a number value that is inputted is acceptable in a range and is a num
# openSaveFile: Checks a txt file and gets a dictionary of players and value from it
# writeToSave: writes the dictionary of altered data back to the txt file
# jackpotOpen: obtain jackpot amount
# jackpotClose: Save the jackpot amount to the file

# Asks for the number of players, and asks for the names producing a dictionary of the selected players
def playerSelect(diction):

    infLooper = 1
    
    while infLooper == 1:
        
        try:
            numberOfPlayers = int(input("Input the number of players: "))
        except:
            print("Invalid input")
            continue
        
        if numberOfPlayers < 0:
            print("Invalid number of players!")
            continue
        infLooper +=1 
        
    num = 1
    playerNum = 1
    players = {}
    
    while num <= numberOfPlayers:
        
        print("Input the name of player",num,":", end='')
        name = input('')
        
        if name in players:
            print("You have already selected that player!")
            continue
        
        
        try:
            
            players[playerNum]=[name,int(diction[name])]
            playerNum += 1
        except:
            print('The name is not in the save file!')
            continue
        
        num += 1
        
    return players

def playerSelectOne(diction):

    
    num = 1
    playerNum = 1
    numberOfPlayers = 1
    players = {}
    
    while num <= numberOfPlayers:
        
        print("Input the name of player",num,":", end='')
        name = input('')
        
        if name in players:
            print("You have already selected that player!")
            continue
        
        
        try:
            
            players[playerNum]=[name,int(diction[name])]
            playerNum += 1
        except:
            print('The name is not in the save file!')
            continue
        
        num += 1
        
    return players







# Give a message to the user, the lower and upper bound and type of value and it will make sure a valid value is given by the user
def valueChecker(message,lowerBound,upperBound,type):
    
    message = str(message) + ': '
    
    
    while True:
        inputValue = input(message)
        
        if type.lower() == 'f':
            try:
                inputValue = float(inputValue)
            except:
                print("Sorry. Invalid input")
                continue
            
        elif type.lower() == 'i':
            try:
                inputValue = int(inputValue)
            except:
                print("Sorry. Invalid input")
                continue
        
        if not lowerBound <= inputValue <= upperBound:
            print('Sorry. The value you input is out of range.')
            continue
        
        break
    return inputValue



# WIll obtain the saved file information of the players
def openSaveFile():
    
    file = open('Saves.txt','r')
    
    savedDictionary = {}
    
    info = file.readline()
    
    while len(info) > 0:
        
        for letter in range(0,len(info)):
            
            if info[letter] == ':':
                
                
                try:
                    if '\n' in info[letter+1:]:
                        
                        money = float(info[letter+1:len(info)-1])
                        
                    else:
                        money = float(info[letter+1:])
                except:
                    print("There is an error in the save file!")
                    return
                
                    
                savedDictionary[info[:letter]] = money
        
        info = file.readline()

        
    return savedDictionary

# Take the players dictionary and add it back to the original diction dictionary. Then print the diction to the file
def writeToSave(players,diction):
    
    if players != 'NONE':
    
        for playerNum in players:
            diction[players[playerNum][0]] = players[playerNum][1]     
                
    file = open('Saves.txt','w')
    
    for key in diction:
        
        toWrite = key+':'+str(diction[key])
        file.write(toWrite)
        file.write('\n')
        
    file.close()
    
    return

def jackpotOpen():
    
    file = open('Jackpot.txt','r')
    
    jackpot = file.readline()
    
    return int(jackpot)

def jackpotClose(value):
    
    file = open('Jackpot.txt','w')
    
    file.write(str(value))
    
    return

# Print the scores from the save file

def checkScores():
    saveFile = open('Saves.txt','r')
    
    with saveFile as file:
        print('\t\tCURRENT SCORES\n')
        for element in file:
            print('\t\t',element.replace(':',' '))
            
    return

# Adds a user to the save file
def addNewUser():
    'Allows for creation of new account'
    while True:
        name = input('Please enter your username: ')
        name.lower()
        diction = mods.openSaveFile()
        
        if name in diction:
            print('Sorry name is already in use\n\n')
            continue
        else:
            break
        
    amount = mods.valueChecker('Input an amount of money greater than 0 (Not greater than 1000)', 0, 1000, 'f')

    

    diction.update({name:amount})
    
    mods.writeToSave('NONE', diction)
        
    return