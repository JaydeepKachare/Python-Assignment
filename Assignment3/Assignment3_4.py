
def findFreq (List , num) :
    freq = 0
    for i in range(0,len(List)) :
        if List[i] == num :
            freq += 1 
    return freq 


def main() :
    List = [] 

    size = int(input("Enter Length of List  :   "))

    for i in range(0,size) :
        List.append(int(input("Enter num at position {} :   ".format(i))))

    print("Entered List is  {}  ".format(List))
    num = int(input("Enetr num to search frequency  :   "))
    result = findFreq(List,num) 
    print("Frequency of  {}  from List is    :   {}" .format(num , result))


if __name__ == "__main__" : 
    main() 