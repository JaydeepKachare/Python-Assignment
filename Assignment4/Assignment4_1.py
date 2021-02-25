# lambda function for returning power of two 

ppowerOf2 = lambda num : pow(2,num) 


def main() :
    num = int(input("Enter any number   :   "))
    result = ppowerOf2(num)
    print("2^{} = {}".format(num,result))


if __name__ == "__main__" :
    main() 