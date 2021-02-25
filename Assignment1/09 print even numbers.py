# print first 10 even numbers 


def main() :
    counter = 0 
    num = 2 

    while counter < 10 : 
        if num%2 == 0 :
            print(num) 
            counter = counter + 1 
        num = num + 1 

    

if __name__ == "__main__" : 
    main() 