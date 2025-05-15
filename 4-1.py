from random import randint
import random

def guess_game(turns):
    number = random.randint(1,100)
    
    win = False
  
    count = 0
    
    for i in range(turns):
        numberGuess = int(input("nhap so ban doan: "))
        count += 1
        if numberGuess == number:
            print(f"ban doan dung sau {i+1} lan")
            win = True
            break
        else:
            if numberGuess < number:
                print("so ban doan nho hon")
            else:
                print("so ban doan lon hon ")
                

    print(f"so dung la: {number}")
    print(f"so ban doan la: {numberGuess}")
    
    return win
        
        
            
def choose_level():
    print("\t che do 1 (easy): ban co 9 luot doan.")
    print("\t che do 2 (medium): ban co 6 luot doan.")
    print("\t che do 3 (hard): ban co 4 luot doan.")
    
    limit = True
    while limit:
        level = int(input("chon che do ban muon choi (1->3): "))
        if level >= 1 and level <= 3:
           return 9 if level == 1 else 6 if level == 2 else 4
        
def ex6():
    winCount = 0
    loseCount = 0
    while True:
        if guess_game(choose_level()):
            winCount += 1
        else:
            loseCount += 1
        
        player = input("ban co muon choi tiep khong (Y/N): ")
        if player.lower() == "n":
            break
        
    print(f"you played {winCount + loseCount} times")
    print(f"you winned {winCount} times")
    print(f"you losed {loseCount} times")
    
        
    
ex6()