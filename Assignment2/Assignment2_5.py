
def isPrime (num) :
    for i in range(2,num) : 
        if (num%i == 0) :
            return False 
        return True


def main() :
    num = int(input("Enter number : "))

    if isPrime(num) == True :
        print("{} is prime num ".format(num))
    else :
        print("{} is not prime number ".format(num))
    



if __name__ == "__main__" : 
    main() 