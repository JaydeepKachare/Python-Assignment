# display even odd numbers through thread

import threading 
import time 

def isEven(num) : 
    return num%2 == 0 

def EvenFactorSum (lock) :
    lock.acquire() 
    num = int(input("Enter any number : "))
    sum = 0 
    for i in range (1,num) : 
        if num%i == 0 :
            if isEven(i) == True : 
                sum += i
    print(f"sum of even factors of {num} is {sum} ")
    lock.release() 
    

def OddFactorSum (lock) : 
    lock.acquire() 
    num = int(input("Enter any number : "))
    sum = 0 
    for i in range (1,num) : 
        if num%i == 0 :
            if isEven(i) == False : 
                sum += i
    print(f"sum of odd factors of {num} is {sum} ")
    lock.release() 




def main() :
    print("Start of main")

    lock = threading.Lock() 
    
    Th1 = threading.Thread(target=EvenFactorSum, args=(lock,))
    Th2 = threading.Thread(target=OddFactorSum, args=(lock,) )
    
    Th1.start() 
    Th2.start() 

    Th1.join() 
    Th2.join() 

    print("End of main")





if __name__ == "__main__" : 
    main() 