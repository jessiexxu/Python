#################
## 1. Naive Bayes
#################

## Naive Bayes methods are a set of supervised learning algorithms based on applying Bayes’ theorem with the “naive” assumption  
## of independence between every pair of features.
## Advantages: Great for text (i.e. email classification) -- it’s faster and generally gives better performance than an SVM
## Disadvantages: 1) Assume independence of the variables in the dataset
##                2) The degree of class overlapping is small (i.e. potential linear decision boundary)

def NBAccuracy(features_train, labels_train, features_test, labels_test):
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    ### use the trained classifier to predict labels for the test features
    t0 = time()
    pred = clf.predict(features_test)
    print "predicting time:", round(time()-t0, 3), "s"
    
    ### calculate and return the accuracy on the test data
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(labels_test, pred)
    print accuracy

##################################
## 2. Support Vector Machine (SVM)
##################################

## SVMs are a set of supervised learning methods used for classification, regression and outliers detection.
## Advantages: 1) Effective in high dimensional spaces
##             2) Uses a subset of training points in the decision function (called support vectors) - memory efficient
##             3) Versatility (i.e. Kernel functions - linear, rbf)
## Disadvantages: 1) Poor performances if # of features is much >> than # of samples
##                2) SVMs don't directly provide probability estimates - calculated using an expensive five-fold cross-validation

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

features_train, features_test, labels_train, labels_test = preprocess()

## OPTION I: Linear decision boundary

from sklearn.svm import SVC
clf = SVC(kernel="linear")

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print accuracy

## OPTION II: Non-linear decision boundary

# features_train = features_train[:len(features_train)/100] -- select a small set of data as training data to improve efficiency
# labels_train = labels_train[:len(labels_train)/100] -- trade-off for accuracy

from sklearn.svm import SVC
clf = SVC(kernel="rbf", C=10000) 
# rbf - radial basis function; C parameter trades off misclassification of training examples against
# simplicity of the decision surface. A low C makes the decision surface smooth, while a high C aims at classifying
# all training examples correctly by giving the model freedom to select more samples as support vectors.

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print accuracy

## Output selected predicted values
answer = [pred[i] for i in [10,26,50]]
print answer



#################
## 6. Regression
#################
def studentRegression(ages_train, net_worths_train):
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(ages_train, net_worths_train)
    return reg
    
print "net worth prediction:", reg.predict([27])
print "slope:", reg.coef_
print "intercept:", reg.intercept_

print "\n stats on test dataset \n"
print "r-squared score:", reg.score(ages_test, net_worths_test) ## r-squared on test data can assess overfitting

print "\n stats on training dataset \n"
print "r-squared score:", reg.score(ages_train, net_worths_train)

plt.scatter(ages, net_worths)
plt.plot(ages, reg.predict(ages), color='blue', linewidth=3)
plt.xlabel("ages")
plt.ylabel("net worths")
plt.show()
