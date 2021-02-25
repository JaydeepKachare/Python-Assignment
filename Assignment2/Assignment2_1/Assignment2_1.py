

import Arithmetic


def main() :
    num1 = int(input("Enter num1    :   "))
    num2= int(input("Enter num2     :   "))

    print("{} + {} = {}".format(num1,num2,Arithmetic.Add(num1,num2)))
    print("{} - {} = {}".format(num1,num2,Arithmetic.Sub(num1,num2)))
    print("{} * {} = {}".format(num1,num2,Arithmetic.Mul(num1,num2)))
    print("{} / {} = {}".format(num1,num2,Arithmetic.Div(num1,num2)))



if __name__ == "__main__" : 
    main() 