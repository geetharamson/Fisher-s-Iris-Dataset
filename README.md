# Fisher's-Iris-Dataset
# GEETHA KARTHIKESAN , 2019
The Iris flower data set or
Fisher's Iris data set is a multivariate data set 
introduced by the British statistician and biologist Ronald Fisher in his 1936 paper.
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

## Data as table  ##

   A basic table is a two-dimensional grid of data, 
in which the rows represent individual elements of the dataset,
and the columns represent quantities related to each of these elements.
The columns in this table are SepalLength, SepalWidth,PetalLength,PetalWidth and Species .
[link](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/iris.csv)


# Data set #
The Iris dataset was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.

It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.

The columns in this dataset are:
SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species

[link](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/iris%20series.JPG)

##Data sets using Sklearn ##  

 from sklearn import datasets  
 iris = datasets.load_iris()
 print (iris)
    
Adapted from [link](https://scikit-learn.org/stable/tutorial/basic/tutorial.html)
### Images ###
![alt text]( https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/iris%20array.jpg)
## Data Frame ## 
#####df = pd.read_csv('C:/Users/geeth/Desktop/problemset-pands/Iris.csv')
![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/df.JPG)

#####df.head()
  This dataframe command displays the top five contents in table.
![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/irisdf2.JPG)

#####df.describe()
displays the row names -(Sepal_length,sepal_width,petal_length,petal_width,Species) and also count, mean,std,min,25%,50%,75%,max.

![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/irisdf3.JPG)


# To plot the graph 
import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
g = sns.PairGrid(iris)
g.map(plt.scatter);
Adapted from 
[ link](http://seaborn.pydata.org)
### Images
![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/Iris%20graph1.PNG)



# Reference 
### https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics
### http://archive.ics.uci.edu/ml/datasets/Iris
### https://www.youtube.com/watch?v=hd1W4CyPX58
### https://gist.github.com/curran/a08a1080b88344b0c8a7
### https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
