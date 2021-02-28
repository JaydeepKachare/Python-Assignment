# Arithematic class 


class Arithematic : 
    def __init__(self,num1,num2):
        print("Inside construcotr ")
        self.num1 = num1 
        self.num2 = num2 

    def Addition(self) : 
        print("Performing Addition ...")
        return self.num1 + self.num2
    

    def Subtraction(self) : 
        print("Performing Subtraction ...") 
        return self.num1 - self.num2
    
    def Multiplication(self) : 
        print("Performing Multiplication ... ") 
        return self.num1 * self.num2
    
    def Division(self) : 
        print("Performing Division ... ") 
        return self.num1 / self.num2



def main() :
    print("Create Object of class Arithematic   ") 
    obj = Arithematic(20,10) 

    add = obj.Addition() 
    sub = obj.Subtraction() 
    mul = obj.Multiplication() 
    div = obj.Division() 

    print("Addition          :   {}".format(add))   
    print("Subtraction       :   {}".format(sub))   
    print("Multiplication    :   {}".format(mul))   
    print("Division          :   {}".format(div))   



if __name__ == "__main__" : 
    main() 