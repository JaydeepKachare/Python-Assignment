# program for addition of two number 

def add (num1, num2) :
    answer = num1 + num2 
    return answer 



def main() :
    num1 = int(input("Enter num1    :   "))
    num2 = int(input("Enter num2    :   "))
    
    result = add(num1,num2) 

    print("addition of {} and {} is {} ".format(num1,num2,result))



if __name__ == "__main__" : 
    main() 