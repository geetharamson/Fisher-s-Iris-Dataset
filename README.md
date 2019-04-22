# Fisher's-Iris-Dataset
# GEETHA KARTHIKESAN , 2019
The Iris flower data set or
Fisher's Iris data set is a multivariate data set 
introduced by the British statistician and biologist Ronald Fisher in his 1936 paper.
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

## Data as table   (IRIS.CSV) ##

   A basic table is a two-dimensional grid of data, 
in which the rows represent individual elements of the dataset,
and the columns represent quantities related to each of these elements.
The columns in this table are SepalLength, SepalWidth,PetalLength,PetalWidth and Species .


# Data set #
The Iris dataset was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.

It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.

The columns in this dataset are:
SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
Species

### Sklearn ###  

 from sklearn import datasets  
 iris = datasets.load_iris()
 print (iris)
    
https://scikit-learn.org/stable/tutorial/basic/tutorial.html#machine-learning-the-problem-setting

## Data Frame ## 


# To plot the graph 
`import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
g = sns.PairGrid(iris)
g.map(plt.scatter);`
[ link](http://seaborn.pydata.org/tutorial/axis_grids.html?highlight=iris%20dataset)

## Images
![alt text] (https://1drv.ms/u/s!Ap9A9jW2Nm_mgkWp6HgKBRIoA0a0/.jpg)

Here's our logo (hover to see the title text):

Inline-style: 
![alt text]( "http://seaborn.pydata.org/_images/seaborn-PairGrid-1.png")
("http://seaborn.pydata.org/_images/seaborn-PairGrid-5.png")


# Reference 
### http://archive.ics.uci.edu/ml/datasets/Iris
### https://www.youtube.com/watch?v=hd1W4CyPX58
