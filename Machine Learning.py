#################
## 1. Naive Bayes
#################
def NBAccuracy(features_train, labels_train, features_test, labels_test):
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    
    ### calculate and return the accuracy on the test data
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(labels_test, pred)
    return accuracy


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
