# from list get sum of all prime numbers 

# check for prime number and add it to sum 
import checkPrime  as checkPrime
def sumList (arr) : 
    sum = 0 
    for i in range(0,len(arr)) : 
        if checkPrime.isPrime(arr[i]) == True :
            sum += arr[i]
    
    return sum 



def main() :
    arr = [] 
    size = int(input("Enter size of list    :    "))
    
    for i in range(0,size) : 
        arr.append(int(input("Enter element at position  {}     :   ".format(i))))
    
    print("Entered data is  {}".format(arr))
    result = sumList(arr) 
    print("Sum of prime number from list is {}".format(result))


if __name__ == "__main__" : 
    main() 