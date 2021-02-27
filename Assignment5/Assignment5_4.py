# accept number and return summation ofdigits 

sum = 0 
def sumDigit(num) :
    global sum 
    if num == 0 :
        return 0 
    else : 
        sum += (num%10)
        sumDigit(int(num/10))
        return sum 
    



def main() :
    num = int(input("Enter any number   :   "))
    sumD = sumDigit(num) 
    print("Summation of digit of {} is {} ".format(num,sumD))



if __name__ == "__main__" : 
    main() 