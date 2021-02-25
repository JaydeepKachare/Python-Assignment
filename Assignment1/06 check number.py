# accept number from user check status of that number 

def checkNum (num) :
    if num < 0 : 
        print("{} is Less than zero ".format(num))
    elif num > 0 : 
        print("{} is greater than zero ".format(num))
    else :
        print("{} is zero ".format(num))
        


def main() :
    num = int(input("Enter any number : "))
    checkNum(num)



if __name__ == "__main__" :
    main() 