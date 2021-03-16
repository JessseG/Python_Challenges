from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def main():

    # divides training datasets and test datasets into X,y
    X, y = datasets.load_iris( return_X_y = True) 

    # splits the X & y data into random training and testing subsets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    # instantiate the classifier with 20 trees
    clf = RandomForestClassifier(n_estimators = 20)

    # train the model
    clf.fit(X_train, y_train)

    # make predictions
    y_pred = clf.predict(X_test)

    # calculate accuracy with metrics module
    print("\nAccuracy: ", accuracy_score(y_test, y_pred))

    # calculate accuracy with metrics module
    print("Confusion Maxtrix: \n", confusion_matrix(y_test, y_pred))

    output = "Accuracy: " + str(accuracy_score(y_test, y_pred)) + "\n\nConfusion Maxtrix: \n" + str(confusion_matrix(y_test, y_pred))

    # write output to 'output.txt'
    outfile = open('output.txt', 'w')
    outfile.write(output)
    outfile.close()


if __name__ == "__main__":
    exit(main())