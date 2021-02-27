# take input from user and print number recursivey 

def printStar(num) :
    if num == 0 :
        return 
    else :
        print("{}  ".format(num),end=" ")
        printStar(num-1)


def main() :
    num = int(input("Enter any number   :   "))
    printStar(num)



if __name__ == "__main__" : 
    main() 