# accept number from user and check for divisibility f 5 

def checDivisibilty ( num ) : 
    if num%5 == 0 : 
        return True 
    else :
        return False 



def main() :
    num = int(input("Enter any number : "))
    
    if checDivisibilty(num) == True :
        print("{} is divisible by 5".format(num)) 
    else :
        print("{} is not divisible by five".format(num))


if __name__ == "__main__" :
    main()