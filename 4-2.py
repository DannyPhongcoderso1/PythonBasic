import random


def game_engine(moneyInBank,betMoney):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    sumDice1Dice2 = dice1 + dice2
    win = False
    
    guessStatus = int(input("Ban chon tai (1) hay xiu (2) hay hoa (3): "))
    if sumDice1Dice2 > 5:
        if guessStatus == 1:
            print("ban da thang")
            moneyInBank = moneyInBank + betMoney * 2
            win = True
        else:
            print("ban da thua")
    elif sumDice1Dice2 < 5:
        if guessStatus == 2:
            print("ban da thang")
            moneyInBank = moneyInBank + betMoney * 2
            win = True
        else:
            print("ban da thua")
    elif sumDice1Dice2 == 5:
        print("ban da thang")
        if guessStatus == 3:
            print("ban da thang")
            moneyInBank = moneyInBank + betMoney * 3
            win = True
    return moneyInBank, win

def game():
    
    contPlay = True
    moneyInBank = 100000
    countWin = 0
    countLose = 0
    while contPlay:
        print("money in bank: ", moneyInBank)
        betMoney = int(input("nhap so tien ban muon cuoc: "))
        if moneyInBank - betMoney >= 0:
            moneyInBank = moneyInBank - betMoney
            moneyInBank, win = game_engine(moneyInBank, betMoney)
            if win:
                countWin += 1
            else:
                countLose += 1
        else:
            print("ban khong con tien de choi")
            break
        player = input("ban co muon tiep tuc choi khong (Y/N): ")
        if player.lower() == "n":
            contPlay = False
            print("cam on ban da choi")
            print("ban da thang ", countWin, " lan")
            print("ban da thua ", countLose, " lan")
            print("ban da choi ", countWin + countLose, " lan")
        else:
            contPlay = True
            print("ban da chon tiep tuc choi")
game()