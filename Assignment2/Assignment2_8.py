
def main() :
    num = int(input("Enter number : ")) 

    for i in range(0,num+1) :
        for j in range(0,num+1  ) :
            if j<i :
                print(" {} ".format(j+1),end=" ") 
        print()    



if __name__ == "__main__" : 
    main() 