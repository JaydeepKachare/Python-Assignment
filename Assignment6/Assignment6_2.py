# class for circle 


class Circle : 
    PI = 3.14               # class varibale 

    def __init__(self):
        print("Inside constructor of Circle ")
        self.Radius = 0 
        self.Area = 0 
        self.Circumference = 0 

    def Accept(self) :
        print("Enter value of radius    :   ",end=" ")
        self.Radius = float(input()) 


    def CalculateArea(self) :
        self.Area = Circle.PI * self.Radius * self.Radius 
        print("Area calculated and stored ....          ;)")

    def CalculateCircumference(self) :
        self.Circumference = 2 * Circle.PI * self.Radius 
        print("Circumference calculated and stored .... ;)")


    def Display(self) : 
        print("Radius           :   {} ".format(self.Radius))
        print("Area             :   {} ".format(self.Area))
        print("Circumference    :   {} ".format(self.Circumference))



def main() :
    print("Create object  of class circle ") 
    obj  = Circle() 
    obj.Accept() 
    obj.CalculateArea() 
    obj.CalculateCircumference() 
    obj.Display() 



if __name__ == "__main__" : 
    main() 