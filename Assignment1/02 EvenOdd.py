# check if number iseven or odd 

def isEven (num) : 
    if num%2 == 0 :
        return True
    else :
        return False 



def main() :
    num = int(input("Enter any number : "))

    if isEven(num) == True :
        print("{} is Even".format(num))
    else :
        print("{} is Odd".format(num))



if __name__ == "__main__" :
    main() 