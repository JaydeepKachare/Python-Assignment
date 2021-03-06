# BankAccount class 

class BankAccount :
    # class variable 
    ROI = 10.5  
    def __init__(self,Name,Amount):
        self.Name = Name 
        self.Amount = Amount 

    def Deposite(self,Amount) : 
        self.Amount += Amount 
    
    def Withdraw(self,Amount) : 
        self.Amount -= Amount 
    
    def CalculateIntrest(self) : 
        interest = self.Amount * BankAccount.ROI / 100 
        return interest

    def Display(self) : 
        print("Name : {} Amount : {} Interest : {} ".format(self.Name,self.Amount,self.CalculateIntrest()))

def main() :
    obj = BankAccount("Jaydeep",10000) 
    obj.Withdraw(5000)
    obj.Deposite(15000)
    obj.Display() 


if __name__ == "__main__" : 
    main() 


