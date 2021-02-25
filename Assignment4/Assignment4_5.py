# map filter reduce for prime no on list of accepted users 

def isPrime (num) :
    for i in range(2,num) : 
        if (num%i) == 0 :
            return False 
    return True 

multiply = lambda num : num*2 

def findMax (List) : 
    max = 0 
    for i in range(0,len(List)) :
        if List[i] > List[max] : 
            max = i 
    return List[max]
        

def main() :
    size = int(input("Enter size of List    :   "))
    List = [] 
    for i in range(0,size) : 
        List.append(int(input("Enter num at position  {}    :   ".format(i))))
    
    print("Entered List is              :   {}".format(List))

    newList = list(filter(isPrime,List))
    print("List of prime num is         :   {}".format(newList))

    resultList = list(map(multiply,newList)) 
    print("resultList is                :   {}".format(resultList))

    maxNum = findMax(resultList) 
    print("Final Max number is          :   {}".format(maxNum))
        

if __name__ == "__main__" :
    main() 