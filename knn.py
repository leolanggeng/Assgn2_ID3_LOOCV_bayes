#-------------------------------------------------------------------------
# AUTHOR: Leonardo Langgeng
# FILENAME: knn.py
# SPECIFICATION: calculating the LOO-CV error rate
# FOR: CS 4210- Assignment #2
# TIME SPENT: 3 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
print('db', db)

class_true = 0
#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
    #For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages

    #transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
    #For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages

    #--> add your Python code here

    X = []
    Y = []
    
    print('LOO', i)
    
    for j, each in enumerate(db):   #adding all to X except i; skipping
        #print('each', each)
        #print('j', j)
        if i == j:
            #print('cont', float(instance[0]), float(instance[1]))
            continue
        else:
            #print('add', float(instance[0]), float(instance[1]))
            X.append((float(each[0]), float(each[1])))
            if each[2] == '-':
                Y.append(0)
            elif each[2] == '+':
                Y.append(1)

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y )

    print('testing', [db[i][0], db[i][1]])

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    
    class_predicted = clf.predict([[float(db[i][0]), float(db[i][1])]])
    print('predict', class_predicted)

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    
    if (class_predicted == 0) and (db[i][2] == '-'):
        class_true = class_true + 1
        print('true')
    elif  (class_predicted == 1) and (db[i][2] == '+'):
        class_true = class_true + 1
        print('true')
    else:
        print('fail')

#print the error rate
#--> add your Python code here

print('error rate', class_true / len(db))


