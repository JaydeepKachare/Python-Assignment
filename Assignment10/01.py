import pandas as pd 
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def marvellous(path) :
    # get data 
    data = pd.read_csv(path)
    print("Length of dataset : " , len(data))

    # prepare data 
    Features = ["Wether" , "Temperature"] 
    print("Feature names are : ",Features)

    Wether = data.Wether
    Temperature = data.Temperature
    Play = data.Play

    lobj = preprocessing.LabelEncoder() 

    WetherX = lobj.fit_transform(Wether)
    TemperatureX = lobj.fit_transform(Temperature)
    Label = lobj.fit_transform(Play)

    features = list(zip(WetherX,TemperatureX)) 

    obj = KNeighborsClassifier(n_neighbors=3)

    obj.fit(features,Label)

    output = obj.predict([[0,2]])

    if output == 1 : 
        print("You can play")
    else : 
        print("Don't Play")


def main() :
    print("___ marvellous ___") 
    print("Enter path of file : ", end = " ") 
    path = "play.csv"
    marvellous(path) 


if __name__ == "__main__" : 
    main() 

