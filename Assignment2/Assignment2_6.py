
def main() :
    num = int(input("Enter number : ")) 

    for i in range(0,num) :
        for j in range(num,i,-1) :
            print("*  ",end=" ") 
        print()    



if __name__ == "__main__" : 
    main() 