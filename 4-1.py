import random

def money_enter():
    amountMoney = int(input("enter the amount of money you want to bet: "))
    return amountMoney

def game_engine(amountMoney):
    status = ""
    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    sumDices = dice1 + dice2
    if sumDices > 5:
        status = "tai"
    elif sumDices == 5:
        status = "hue"
    else:
        status = "xiu"
            
    guess = input("you guess (tai/xiu): ")
    
    if guess.lower() == status:
        if guess.lower() == "hue":
            print("excellent")
            return amountMoney * 3
        print("you are right")
        return amountMoney * 2
    return 0

def tai_xiu():
    moneyInBank = int(input("nhap tien ban co trong tai khoan: "))
    
    while moneyInBank > 0:
        print(f"you are having {moneyInBank} in account")
        moneyEnter = money_enter()
        if moneyEnter <= moneyInBank:
            moneyInBank -= moneyEnter
            moneyInBank += game_engine(moneyEnter)
            player = input("do you want to play again? (y/n) ")
            if player == "n":
                break
        else:
            print("not enough money")

tai_xiu()