from sklearn.datasets import load_iris
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

dataSet = load_iris()

features = dataSet.data
labels = dataSet.target
labelsNames = list(dataSet.target_names)
featureNames = dataSet.feature_names

featuresDF= pd.DataFrame(features)
featuresDF.columns = featureNames

clf = KNeighborsClassifier(n_neighbors=8)

X = features
y = labels

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

clf.fit(X_train, y_train)
accuracy = clf.score(X_train, y_train)
# print("accuracy on train data {:.2}%".format(accuracy))

accuracy = clf.score(X_test,y_test)
# print("accuracy on test data {:.2}%".format(accuracy))


from joblib import dump, load
filename="irisSavedModel.joblib"
dump(clf, filename)

clfUploaded = load(filename)

accuracy = clfUploaded.score(X_test,y_test)
# print("accuracy on test data {:.2}%".format(accuracy))