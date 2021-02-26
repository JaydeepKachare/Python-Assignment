
def findMin (List) :
    minNum = List[0]
    for i in range(0,len(List)) :
        if List[i] < minNum :
            minNum = List[i]
    return minNum 


def main() :
    List = [] 

    size = int(input("Enter Length of List  :   "))

    for i in range(0,size) :
        List.append(int(input("Enter num at position {} :   ".format(i))))

    print("Entered List is  {}  ".format(List))
    result = findMin(List) 
    print("Minimum num from List is    :   {}" .format(result))


if __name__ == "__main__" : 
    main() 