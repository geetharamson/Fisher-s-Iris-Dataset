    
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

#Data as table :#
   #A basic table is a two-dimensional grid of data, 
#in which the rows represent individual elements of the dataset, 
#and the columns represent quantities related to each of these elements.

##Features matrix :##
    #This table layout makes clear that the information
#can be thought of as a two-dimensional numerical array or matrix, called the
#features matrix with shape.


### Sklearn ###  
#Initialise ipython
 # from sklearn import datasets
 from sklearn import datasets
    
 # From the dataset load iris 
 iris = datasets.load_iris()
 #print iris
 print (iris)
    
    
 # How to plot as Graph  
import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
g = sns.PairGrid(iris)
g.map(plt.scatter);  
Adapted from http://seaborn.pydata.org/tutorial/axis_grids.html?highlight=iris%20dataset
# Adapted from  https://stackoverflow.com/a/38105540   
#https://scikit-learn.org/stable/tutorial/basic/tutorial.html#machine-learning-the-problem-setting

    
    
    
