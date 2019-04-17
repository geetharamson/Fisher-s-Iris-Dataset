    
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

Loading the Iris dataset from Scikit-learn

Data as table :
A basic table is a two-dimensional grid of data, 
in which the rows represent individual elements of the dataset, 
and the columns represent quantities related to each of these elements
Features matrix :
    This table layout makes clear that the information
can be thought of as a two-dimensional numerical array or matrix, called the
features matrix with shape.
$ python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> digits = datasets.load_digits()
