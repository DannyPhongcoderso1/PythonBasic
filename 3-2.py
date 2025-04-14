from random import random


#cau1
def eligible(age):
    if age < 18:
        return "not eligible"
    else:
        return "eligible"
    
#cau 2
def evenorodd(number):
    if number % 2 == 0:
        return "number is even"
    else:
        return "number is odd"
    
#cau 3
def divisedby7(number):
    if number % 7 == 0:
        return "number is divisible by 7"
    else:
        return " number is not divisible by 7"

#cau 4
def ex4(number):
    if number[len(number)-1] % 3 == 0:
        return "last digit is divisible by 3"
    else:
        return "last digit is not divisible by 3"

#cau 5
def guess_number():
    number = random(1,9)
    nums = int(input("chon so lan ban muon doan: "))
    
    for i in range(len(nums)):
        guessNumber = int(input("Nhap so ban doan"))
        if guessNumber == number:
            return True
        else:
            print("ban doan sai")
    
    return False

#cau 6
def weekly(number):
    week = {
        1: Sunday,
        2: Monday,
        3: Tuesday,
        4: Wednesday,
        5: Thursday,
        6: Friday,
        7: Saturday
    }

    return(week[number])
        
        