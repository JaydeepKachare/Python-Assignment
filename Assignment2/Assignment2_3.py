

def main() :
    num = int(input("Enter number : "))
    n = num 
    fact = 1 
    while num > 0 :
        fact = fact * num 
        num = num -1 

    print("{}! = {}".format(n,fact))


if __name__ == "__main__" : 
    main() 