# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "matches.csv"
names = ['championId_1', 'championId_2', 'championId_3', 'championId_4', 'championId_5', 'championId_6', 'championId_7', 'championId_8', 'championId_9', 'championId_10', 'class']
dataset = pandas.read_csv(url, names=names)

# shape
print(dataset.shape)
print(dataset.head(20))

# descriptions
# print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())


# scatter plot matrix
# scatter_matrix(dataset)
# plt.show()

array = dataset.values
print(array)