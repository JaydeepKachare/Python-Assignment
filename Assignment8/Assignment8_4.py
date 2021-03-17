# display even odd numbers through thread

import threading 
import time 
import os 

def small (str) : 
    count = 0 
    for char in str : 
        if char.islower() == True :
            count += 1 
    print("No of lower character in passed list ",count)
    print("Thread id : ",os.getpid()  )
    print("Name : ",threading.currentThread().name )


def capital (str) : 
    count = 0 
    for char in str : 
        if char.isupper() == True :
            count += 1 
    print("No of upper character in passed list ",count)
    print("Thread id : ",os.getpid()  )
    print("Name : ",threading.currentThread().name )



def digit (str) : 
    count = 0 
    for char in str : 
        if char.isnumeric() == True : 
            count += 1 
    print("No of numbers in passed list ",count)
    print("Thread id : ",os.getpid()  )
    print("Name : ",threading.currentThread().name )



def main() :
    print("Start of main")

    str = "abcdefghijklmnopqrstuvwxyz"
    Th1 = threading.Thread(target=small, args=(str,))
    Th1.start() 
    Th1.join() 

    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Th2 = threading.Thread(target=capital, args=(str,))
    Th2.start() 
    Th2.join() 

    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123454"
    Th3 = threading.Thread(target=digit, args=(str,))
    Th3.start() 
    Th3.join() 

    print("End of main")


if __name__ == "__main__" : 
    main() 