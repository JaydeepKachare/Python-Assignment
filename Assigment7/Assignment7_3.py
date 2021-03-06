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
        pass


    def Factors(self) : 
        for i in range(0,self.Value) : 
            if self.Value%i == 0 : 
                print(i) 


    def SumFactors(self) : 
        pass




def main() :
    pass



if __name__ == "__main__" : 
    main() 

