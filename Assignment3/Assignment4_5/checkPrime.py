# function to check whether number is prime or not 

def isPrime (num) : 
    for i in range(2,num) :
        if num%i == 0 : 
            return False 
    return True 