
def main() :
    num = int(input("Enter number : ")) 
    n = num 

    count = 0 
    while num != 0 :
        count = count + (num%10)
        num = int(num/10)       # mandaotory typecasting otherwise 
        # result get converted into double type


    
    print("no of digit of {} is {}".format(n,count))



if __name__ == "__main__" : 
    main() 