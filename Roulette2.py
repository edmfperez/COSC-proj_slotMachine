    # Feras AlSaffar
    # 11/10/2015
  
def roul():  
    while True:
        # import modules dictionary
        import mods
        import RouletteMods
        import time
        
        # import saved file information
        diction = mods.openSaveFile()
        
        # players is a dictionary in the form:
        #     Player [num]: [0] player name [1] amount of money
        players = mods.playerSelect(diction)
        
        
        # This will print the table and all other necessary information
        print("""
        This game is roulette. You may select to place a bet anywhere on the table. To select a certain region, input a value in the menu:
        
        
            |---------------------------------|------|
            |3|6|9|12|15|18|21|24|27|30|33|36||2 to 1|
        ----|---------------------------------|------|
          0 |2|5|8|11|14|17|20|23|26|29|32|35||2 to 1|
        ----|---------------------------------|------|
            |1|4|7|10|13|16|19|22|25|28|31|34||2 to 1|
            |---------------------------------|------|--|
            |    1st 12    |    2nd 12    |    3rd 12   |
            |-------------------------------------------|
            |1 to 18| EVEN | RED | BLACK | ODD |19 to 26|
            |-------------------------------------------|
        
        
        
        
        1. Place a bet on a specific number(s) [Inside Bet]
        2. Place a bet on a non-specific value but a group of numbers [Outside Bet]
        
        Inside Bets:
        
        1.Betting on 1 number (Straight): 35:1 Payout
        2.Betting on 2 numbers (Split): 17-1 Payout
        3.Betting on 3 numbers (Street): 11-1 Payout
        4.Betting on 4 numbers (Square): 8-1 Payout
        5.Betting on 6 numbers (Six Line): 5-1 Payout
        
        Outside Bets:
        
        1.Betting on either Red or Black: 1-1 Payout
        2.Betting on any dozen: 1-1 Payout
        3.Betting on 1 to 18 [Low] or 19 to 36 [High]: 1-1 Payout
        4.Betting on Odd or Even: 1-1 Payout
        5.Betting on 2 to 1 [Columns]: 2-1 Payout
        """)
        
        
        # Loop this to go through each player. Necessary to call specific key in players dictionary
        num = 1
        bettings = {}
        
        while num <= len(players):
        
            # This is to loop through the two dictionaries NUMBER and BETS to keep track of bets and how much was bet
            betCount = 1
            bets = {}
            print("\n\nFor --",players[num][0],'-- :')
            
            # if selection is 1, go to insideBet function
            while True:
                
                if players[num][1] == 0:
                    print('Cannot place anymore bets')
                    break
                
                selection = mods.valueChecker("Would you like to place an inside or outside bet?:(3 is for no more bets) ", 1, 3, 'i')
        
                
                if selection == 1:
                    
                    while True:
                        # This will go through ask what kind of inside bet
                        # Then, it will return a dictionary
                        # Bets take the form bets[numberOfBet] = [0] betted number [1] amount
                        try:
                            bets.update(RouletteMods.insideBet(players,num,betCount))
                        except:
                            print('You have no more moola so you can\'t place anymore bets.')
                            break
                        players[num][1] -= bets[betCount][1]
                        betCount+= 1
                
                        
                        again = mods.valueChecker('\nAnother inside bet? (1 - Yes, 2 - No)', 1, 2, 'i')
                        if again == 2:
                            break
                        
                elif selection == 2:
                    
                                
                    while True:
                        # This will go through ask what kind of inside bet
                        # Then, it will return a dictionary
                        # Bets take the form bets[numberOfBet] = [0] betted number [1] amount
        
                        try:
                            bets.update(RouletteMods.outsideBet(players,num,betCount))
                        except:
                            print('You have no more moola so you can\'t place anymore bets.')
                            break
                        players[num][1] -= bets[betCount][1]
                        betCount+= 1
                
                        
                        again = mods.valueChecker('\nAnother outside bet? (1 - Yes, 2 - No)', 1, 2, 'i')
                        if again == 2:
                            break
                elif selection == 3:
                    break
            # to save the bets of player num to a dictionary so bets can be reset
            
            
            bettings[num] = bets
            
            # To the next player
            num += 1
            
            
            
            
            
            
        # This will return a random number
        RESULT = RouletteMods.selectingANumber()
        print("\nThe ball is now spinning")
        time.sleep(2)
        print('\nIt is still spinning')
        time.sleep(3)
        print('\nIT STOPPED!')
        time.sleep(1)
        print("And.....")
        time.sleep(2)
        
        print("""
        
        The RESULT IS""", RESULT,"\n\n")
        
        for playerNum in bettings:
            
            bets = bettings[playerNum]
        
            lose = 0
            
            for bet in bets:
                
                numbers = bets[bet][0]
                
                try:
                    if RESULT in numbers:
                         
                        players[playerNum][1] += bets[bet][1] + (bets[bet][1] * bets[bet][2])
                        lose -= bets[bet][1] * bets[bet][2]
                    else:
                        lose += bets[bet][1]
                    
                except:
                    if RESULT == numbers:
                        
                        players[playerNum][1] += bets[bet][1] + (bets[bet][1] * bets[bet][2])
                        lose -= bets[bet][1] * bets[bet][2]
                    else:
                        lose += bets[bet][1]
            
            # Prints lose or gains
            if lose > 0:
                print("I am sorry", players[playerNum][0],", you lost $",lose)
            elif lose < 0:
                print("Congrats",players[playerNum][0],", you won $",-1*lose)
            else:
                print("You did not gain anything, or lose anything", players[playerNum][0])
                
        # This will rewrite the saves.file with the new values of money
        mods.writeToSave(players, diction)
        
        selection = mods.valueChecker('Would you like to play roulette again?(1 is Yes, 2 is No)', 1, 2, 'i')
        
        if selection == 2:
            break
        
    return
