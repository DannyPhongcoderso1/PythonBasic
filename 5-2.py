import random
import math

def menu():
    print("1.\t In ra danh sách vừa tạo.")
    print("2.\t In đảo ngược danh sách.")
    print("3.\t Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).")
    print("4.\t tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.")
    print("5.\t đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.")
    print("6.\t In ra vị trí các phần tử là số nguyên tố.")
    print("7.\t tìm các số duy nhất (không trùng lặp) trong danh sách.")
    print("8.\t liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.")
    print("9.\t In ra các đoạn con trong danh sách giảm liên tiếp.")
    print("10\t exit")
    
def create_list(n):
    list1 = []
    for i in range(n):
        num = random.randint(1,100)
        list1.append(num)
    return list1

def last_index_largest_number(list):
    sortedList = sorted(list)
    length = len(list)
    while length >= 0:
        length -= 1
        if list[length] == sortedList[-1]:
            print(f"Vị trí cuối cùng của phần tử lớn nhất là: {length}")
            break

def print_index_number(list, X):
    newList = []
    count = 0
    for i in range(len(list)):
        if list[i] == X:
            newList.append(i)
            count += 1
    print(newList)
    print(count)
            
def prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i ==0:
            return False
    return True
    
def find_unique(list):

#Trường hợp 1: Số xuất hiện 1 lần
    numDict = {}
    for key in list:
        if key not in numDict:
            numDict[key] = 1
        else:
            numDict[key] += 1
    newList =[]
    for key in numDict:
        if numDict[key] == 1:
            newList.append(key)
    print(f"số xuất hiện 1 lần: {newList}")
#Trường hợp 2: loại bỏ số bị trùng
    print(f"danh sach sau khi loại bỏ số bị trùng: {numDict}")
            
        
            
def exist_and_frequency(list):
    numDict = {}
    for key in list:
        if key not in numDict:
            numDict[key] = 1
        else:
            numDict[key] += 1
    print(numDict)

def descending_sublist(list):
    count = 0
    for i in range(len(list) - 1):
        if list[i] >list[i+1]:
            count += 1
        if list[i] < list[i+1]:
            if count > 1:
                print(list[i-count:i+1])
            count = 0
            
            

        

if __name__ == '__main__':
    menu()
    n = int(input("nhap so phan tu ban muon trong mang: "))   
    cList = create_list(n)
    while True:
        menu = input("Lua chon cua ban: ")
    
        if menu == '1':
            print(cList)
        elif menu == '2':
            print(cList[::-1])
        elif menu == '3':
            print(sorted(cList))
        elif menu == '4':
            last_index_largest_number(cList)
        elif menu == '5':
            num = int(input("nhap gia tri ban muon chon: "))
            print_index_number(cList,num)
        elif menu == '6':
            for i in range(len(cList)):
                if prime_number(cList[i]):
                    print(f"số nguyên tố: {cList[i]}, vị trí: {i}")
        elif menu == '7':
            find_unique(cList)
        elif menu == '8':
            exist_and_frequency(cList)
        elif menu == '9':
            descending_sublist(cList)
        elif menu == '10':
            break
        
    
    
    


    