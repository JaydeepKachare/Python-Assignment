# display even odd numbers through thread

import threading 
import time 

def isEven(num) : 
    return num%2 == 0 

def EvenList (lock,List) :
    lock.acquire() 
    sum = 0  
    for ele in List :
        if isEven(ele) == True : 
            sum += ele 
    print("sum of even element is ",sum)
    lock.release() 

def OddFactorSum (lock,List) : 
    lock.acquire() 
    sum = 0  
    for ele in List :
        if isEven(ele) == False : 
            sum += ele 
    print("sum of odd element is ",sum)
    lock.release() 



def main() :
    print("Start of main")

    lock = threading.Lock() 
    
    l1 = [11,12,13,14,15,16,17,18,19,20] 
    Th1 = threading.Thread(target=EvenList, args=(lock,l1))

    l2 = [11,12,13,14,15,16,17,18,19,20]
    Th2 = threading.Thread(target=OddFactorSum, args=(lock,l2) )
    
    Th1.start() 
    Th2.start() 

    Th1.join() 
    Th2.join() 

    print("End of main")





if __name__ == "__main__" : 
    main() 