# display even odd numbers through thread

import threading 
import time 

def Even () : 
    print("Priting Even Numbers : ")
    count = 0 
    for i in range(0,20,2) : 
        count += 1
        print(f"Even # {count} = {i} ")


def Odd () : 
    print("Priting Odd Numbers : ")
    count = 0 
    for i in range(1,20,2) : 
        count += 1
        print(f"Odd # {count} = {i} ")



def main() :
    print("Start of main")

    Th1 = threading.Thread(target=Even, args=())
    Th2 = threading.Thread(target=Odd, args=() )

    Th1.start() 
    Th2.start() 

    Th1.join() 
    Th2.join() 

    print("End of main")



if __name__ == "__main__" : 
    main() 