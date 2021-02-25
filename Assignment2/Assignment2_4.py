

def main() :
    num = int(input("Enter number : "))
    sum = 0 

    factor = 1 
    while factor < num : 
        if (num % factor == 0) :
            sum = sum + factor 
        factor = factor + 1 
    
    print("sum offactor of {} is {} ".format(num,sum))



if __name__ == "__main__" : 
    main() 