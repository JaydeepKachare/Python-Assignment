
def main() :
    num = int(input("Enter number : ")) 

    for i in range(0,num) :
        for j in range(0,num) :
            print(" {} ".format(j+1),end=" ") 
        print()    



if __name__ == "__main__" : 
    main() 