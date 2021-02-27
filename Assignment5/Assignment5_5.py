# accept number and return its factorial 

fact = 1 
def factorial(num) :
    global fact
    if num == 1 : 
        return 1 
    else :
        fact *= num 
        factorial(num-1)
        return fact    



def main() :
    num = int(input("Enter any number   :   "))
    factnumber = factorial(num) 
    print("factorial of digit {} is {} ".format(num,factnumber))



if __name__ == "__main__" : 
    main() 