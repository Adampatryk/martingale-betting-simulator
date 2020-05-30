import betting as bet

def manualBetting():
    balance = bet.getBalance()
    pWin = bet.getProbability()
    betAmount = bet.getAmount(balance)
    betResult = bet.getResult(betAmount,pWin)
    balance += betResult
    
    print("Balance:",balance)

def betUntilGoal(balance,betAmount,goal,pWin):
    
    bets = 0
    goalReached = False
    lossStreak = 0
    currentBet = betAmount
    wins,losses = 0,0
    while balance > 0:

        currentBet = betAmount* (2**(lossStreak))
        
        result = bet.getResultAuto(currentBet,pWin)
        
        if result == -currentBet:
            lossStreak+=1
            losses+=1
        elif result == currentBet:
            lossStreak = 0
            wins+=1

        balance = balance+result
        
        if balance>=goal:
            goalReached = True
            break
        
        bets+=1
      
    #print("Bets:",bets)
    #print("Balance:",balance)
    #print("Wins:",wins)
    #print("Losses:",losses)
    #print()

    return [goalReached,bets]
        
def main():
    
    print("1 - Manual\n2 - Repeat")
    menuChoice = input()

    if menuChoice == "1":
        while True:
            manualBetting()
    elif menuChoice == "2":
        while True:
            balance = bet.getBalance()
            betAmount = bet.getAmount(balance)
            pWin = bet.getProbability()
            goal = bet.getGoal()
            print()

            repeats = int(input("Repeats:"))
            wins = 0
            bets = 0
            for i in range(0,repeats):
                result = betUntilGoal(balance,betAmount,goal,pWin)
                
                if result[0]:
                    wins+=1
                    
                bets += result[1]
                
            print("Average Bets:",bets/repeats)
            print("% Win:",wins/repeats*100)
            print()
        print()
            
    else:
        print("Invalid choice.")
        main()

main()
