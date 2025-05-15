import random
from random import randint


#cau 1:
for i in range(1,11):
    print(i)
    
#cau 2:
def sum(n):
    sumN = 0
    for i in range(1,n+1):
        sumN += i
    return sumN

#cau 3:
def sum(n):
    sumN = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            sumN += i
    return sumN

#cau 4:
def vowels(string):
    vowelsL = ["u","e","o","a","i"]
    count = 0
    for i in string:
        if i in vowelsL:
            count += 1
    
    return count

#cau 5:
def count_words(string):
    listW = string.split()
    
    return len(listW)

#cau 6:
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
    print("\t che do 1 (easy): ban co 6 luot doan.")
    print("\t che do 2 (medium): ban co 4 luot doan.")
    print("\t che do 3 (hard): ban co 2 luot doan.")
    
    limit = True
    while limit:
        level = int(input("chon che do ban muon choi (1->3): "))
        if level >= 1 and level <= 3:
           return 6 if level == 1 else 4 if level == 2 else 4
        
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