# take input from user and print * that many times 

def printStar(num) :
    if num == 0 :
        print()
        return 
    else :
        print("*  ",end=" ")
        printStar(num-1)


def main() :
    num = int(input("Enter any number   :   "))
    printStar(num)



if __name__ == "__main__" : 
    main() 