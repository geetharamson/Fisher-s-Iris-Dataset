# Fisher's-Iris-Dataset
# GEETHA KARTHIKESAN , 2019
The Iris flower data set or
Fisher's Iris data set is a multivariate data set 
introduced by the British statistician and biologist Ronald Fisher in his 1936 paper.
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

# Requirements needed to work on the code oneself
  iPython and Python which has packages 
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

## Data sets using Sklearn ##  

Emphasis,* from sklearn import datasets  
 iris = datasets.load_iris() 
  print (iris) *
    
Adapted from [link](https://scikit-learn.org/stable/tutorial/basic/tutorial.html)
 Investigating the data
 
  
  iris_data = pd.read_csv('C:/Users/geeth/Desktop/problemset-pands/Iris.csv')
  iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']
  iris_data.head(10)
  iris_data.shape  
  ![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/data.JPG)
   
   iris_data.min()
   iris_data.max()
   iris_data.mean()
   iris_data.std()
   ![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/data1.JPG)
    iris_data.median()
    iris_data.head()
    iris_data.tail()
    iris_data.isnull()
   ![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/data2.JPG)
   
 ##  Data Visualize 

First with a boxplot which is going to be in the univariate form for each measurement. 
   ~box and whisker plots
   iris_data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
   plt.show()
   Adapted from  [link] https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
     ![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/data3.JPG)
     ![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/plot.JPG)
     
### Images ###
![alt text]( https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/iris%20array.jpg)
## Data Frame ## 
#####df = pd.read_csv('C:/Users/geeth/Desktop/problemset-pands/Iris.csv')
df
  Got the variable values for the Iris species of flowers and its sepal and petal specifications in a txt file format
  and saved as csv. In this dataframe we are asking pandas to read the file from my folder in my pc.
![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/df.JPG)

#####df.head()
  This dataframe command displays the top five contents in table.
![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/df1.JPG)

##### df.describe()
displays the row names -(Sepal_length,sepal_width,petal_length,petal_width,Species) and also count, mean,std,min,25%,50%,75%,max.
![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/df1.JPG)

##### df.info()
 This dataframe gives the information on class, range index,datacolumns, sepal and petal's width and length,species, datatypes and the memory usage.
![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/df2.JPG)

##### mad (Mean Absolute Deviation)
 This dataframe shows the mean absolute deviation .
 
 pd.DataFrame(df.mad() , columns = ["Mad"] ).T 
Adapted from ![alt text](https://stackoverflow.com/a/38546205)

![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/df4.JPG)

# To plot the graph 
import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
g = sns.PairGrid(iris)
g.map(plt.scatter);
Adapted from [ link](http://seaborn.pydata.org)
### Images
![alt text](https://github.com/geetharamson/Fisher-s-Iris-Dataset/blob/master/Iris%20graph1.PNG)



# Reference 
### https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics
### http://archive.ics.uci.edu/ml/datasets/Iris
### https://www.youtube.com/watch?v=hd1W4CyPX58
### https://gist.github.com/curran/a08a1080b88344b0c8a7
### https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
### https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
