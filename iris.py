    
#GEETHA KARTHIKESAN - 2019
#Fisher Iris data set
#https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html

#Import the libraries needed to explore the data set
 import numpy as np
 import pandas as pd 

#data = ("iris.csv")
#names=['sepal-length' ,'sepal-width', 'petal-length','petal-width','species']


# read in Iris as data frame
df = pd.read_csv('/Iris.csv')

#as an array 
data=np.genfromtext()

# from the external repository:
import Iris 
iris = datasets.load_iris()
