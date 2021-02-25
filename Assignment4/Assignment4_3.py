# use of map filter reduce on list 

requiredNum = lambda num : num>=70 and num<=90
increment = lambda num : num+10 

import functools 
prod = lambda num1,num2 : num1*num2


def main() :
    size = int(input("Enter size of list    :   "))
    
    List = [] 
    for i in range(0,size) : 
        List.append(int(input("Enter value at   {}    : ".format(i))))

    print("Entered list is                  :   {}".format(List))

    newList = list(filter(requiredNum,List))
    print("newList after modification  is   :   {}".format(newList))

    resultList = list(map(increment,newList))
    print("resultList after increment  is   :   {}".format(resultList))

    product = functools.reduce(prod,resultList)
    print("result after product  is   :   {}".format(product))



if __name__ == "__main__" : 
    main() 