# create class accept value from user and store it in object 

class Demo : 
    
    def __init__(self,num1,num2):
        print("Inside constructor")
        self.no1 = num1 
        self.no2 = num2 

    def Fun(self) :
        print("no1 : {}         for {} ".format(self.no1 , type(self)))


    def Gun(self) :
        print("no2 : {}         for {} ".format(self.no2 , type(self)))


def main() :
    num1 = int(input("Enter value for no1   :   "))
    num2 = int(input("Enter value for no2   :   "))
    
    Obj1 = Demo(num1,num2)


    num1 = int(input("Enter value for no1   :   "))
    num2 = int(input("Enter value for no2   :   "))
    
    Obj2 = Demo(num1,num2)


    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun() 


if __name__ == "__main__" : 
    main() 



