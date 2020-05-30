import random

def getBalance():
    balance = float(input("Balance: "))
    return balance

def getAmount(balance):
    while True:
        betAmount = float(input("Bet: "))
        if betAmount <= balance:
            return betAmount
        else:
            print("Cannot bet more than available balance.\n")

def getProbability():
    while True:
        pWin = float(input("Probability to win (decimal):"))
        if 0<=pWin<=1:
            return pWin
        else:
            print("Probability must be a number between 0 and 1.")
    
def getGoal():
    goal = float(input("Goal: "))
    return goal

def getResult(betAmount,p):
    if random.random() > p:
        print("#Loss#\n")
        return (-betAmount)
    else:
        print("#Win#\n")
        return (betAmount)

def getResultAuto(betAmount,p):
    betAmount = betAmount
    if random.random() > p:
        return (-betAmount)
    else:
        return (betAmount)
