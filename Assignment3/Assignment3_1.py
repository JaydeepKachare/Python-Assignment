
def addition (Lsit) :
    sum = 0 
    for i in range(0,len(Lsit)) :
        sum += Lsit[i]
    return sum 


def main() :
    List = [] 

    size = int(input("Enter Length of List  :   "))

    for i in range(0,size) :
        List.append(int(input("Enter num at position {} :   ".format(i))))
        size -= 1 

    print("Entered List is  {}  ".format(List))
    result = addition(List) 
    print("Summaion of all num is   :   {}" .format(result))


if __name__ == "__main__" : 
    main() 