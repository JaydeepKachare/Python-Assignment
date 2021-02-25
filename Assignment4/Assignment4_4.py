# take input from user filter even find square and add

isEven = lambda num : num%2 == 0
square = lambda num : num*num
import functools 
summation = lambda num1,num2 : num1+num2 


def main() :
    size = int(input("Enter size of List    :   "))
    List = [] 
    for i in range(0,size) :
        List.append(int(input("Enter num at position    {}  : ".format(i))))

    print("Entered List is          : {}".format(List))

    newList = list(filter(isEven,List))
    print("newList of even num is   : {}".format(newList))

    resultList = list(map(square,newList))
    print("resultList of sqaure     : {} ".format(resultList))
    
    sum = functools.reduce(summation,resultList) 
    print("Final output is          : {} ".format(sum))


if __name__ == "__main__" : 
    main() 