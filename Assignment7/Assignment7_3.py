# Numbers class 

class Numbers : 
    pass

class Arithmetic : 
    def __init__(self,Value):
        self.Value = Value 
    

    def ChkPrime(self) : 
        for i in range(2,self.Value) : 
            if self.Value % i == 0  :
                return False 
        return True 


    def ChkPerfect(self) : 
        if self.Value == self.SumFactors() :
            return True
        else : 
            return False 


    def Factors(self) : 
        for i in range(1,self.Value) : 
            if self.Value%i == 0 : 
                print(i) 


    def SumFactors(self) : 
        sum = 0 
        for i in range(1,self.Value) : 
            if self.Value%i == 0 : 
                sum += i 
        return sum  





def main() :
    obj = Arithmetic(6)
    if obj.ChkPrime() == True : 
        print("Number is prime ") 
    else : 
        print("number is not prime ")

    print("Factors of given numbers : ",end=" ")
    obj.Factors() 

    
    if obj.ChkPerfect() == True : 
        print("Number is perfect")
    else : 
        print("number is not perfect ")

if __name__ == "__main__" : 
    main() 

