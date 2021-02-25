# lambda function for returning multiplication of two numbers 

multiplication = lambda num1,num2 : num1*num2 


def main() :
    num1 = int(input("Enter num1    :   "))
    num2 = int(input("Enter num2    :   "))
    result = multiplication(num1,num2)
    print("{} * {} = {}".format(num1,num2,result))


if __name__ == "__main__" :
    main() 