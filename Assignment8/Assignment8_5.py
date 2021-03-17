
import threading 
import time 

def asc () : 
    for i in range (1,51,1) : 
        print("Ascending : ",i)


def desc () : 
    for i in range (50,0,-1) : 
        print("Descending : ",i)

def main() :
    print("Start of main")

    Th1 = threading.Thread(target=asc, args=())
    print("Thread execution completed ")
    Th2 = threading.Thread(target=desc, args=() )

    Th1.start() 
    Th2.start() 

    Th1.join() 
    Th2.join() 

    print("End of main")



if __name__ == "__main__" : 
    main() 