# Import Libraries
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# For these examples, sklearn is featured
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB 
    


# Read data and check for null values
forest_raw = pd.read_csv('/Users/meganporter/OwnJupyterNotebooks/covtype.csv')
forest_raw = forest_raw.dropna(axis = 0, how ='any')



# Consolidate actions
def stack_ml_algs(data):
    
    # DECISION TREE CLASSIFIER
    print('Decision Tree Classifier')
    X = data[data.columns[:-1]]
    y = data[data.columns[-1]]
    # Divide X and y into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    # Train a DescisionTreeClassifier 
    decision_tree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train) 
    decision_tree_predictions = decision_tree_model.predict(X_test)
    decision_tree_predictions
    # Get a measure of accuracy
    global accuracy_score
    accuracy = accuracy_score(y_test, decision_tree_predictions)
    print('The accuracy of the Decision Tree Classifier on this data set is:', accuracy)
    # SKLEARN classification report
    report = classification_report(y_test, decision_tree_predictions)
    print(report)
    print()


    # KNN
    print('K Nearest Neighbors')
    # X is the classification predictor characteristics, y is the target label
    X = data[data.columns[:-1]]
    y = data[data.columns[-1]]
    # Divide X, y into train and test data, input and output variables 
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    # Train the KNN classifier 
    knn = KNeighborsClassifier(n_neighbors = 7).fit(X_train, y_train)
    # Accuracy on X_test 
    accuracy_score = knn.score(X_test, y_test) 
    print('The accuracy of KNN on this data set is:', accuracy_score) 
    # Create a confusion matrix/contingency table for visualization of accuracy 
    knn_predictions = knn.predict(X_test)  
    cm = confusion_matrix(y_test, knn_predictions)
    print('The confusion matrix', cm)
    print()


    # NAIVE BAYES
    print('Naive Bayes')
    # X is the classification predictor characteristics, y is the target label
    X = data[data.columns[:-1]]
    y = data[data.columns[-1]]
    # Divide X, y into train and test data, inputs and outputs 
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    # Train the Naive Bayes classifier  
    gaussian_nbayes = GaussianNB().fit(X_train, y_train) 
    gaussian_nbayes_predictions = gaussian_nbayes.predict(X_test)
    # Accuracy for the X_test 
    accuracy_score = gaussian_nbayes.score(X_test, y_test) 
    print('The accuracy of Naive Bayes on this data set is:', accuracy_score)

stack_ml_algs(forest_raw)    




