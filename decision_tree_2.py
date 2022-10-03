#-------------------------------------------------------------------------
# AUTHOR: Leonardo Langgeng
# FILENAME: decision_tree_2.py
# SPECIFICATION: compare the number of training instances with model performance
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the
    #4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =

    age = []
    spectacle = []
    astigmatism = []
    tear = []
    recommended = []

    for data in dbTraining:
        #print(data)

        current_data = []
        if data[0] == 'Young':
            current_data.append (0)
        elif data[0] == 'Presbyopic':
            current_data.append (1)
        elif data[0] == 'Prepresbyopic':
            current_data.append (2)

        if data[1] == 'Myope':
            current_data.append(0)
        elif data[1] == 'Hypermetrope':
            current_data.append(1)

        if data[2] == 'No':
            current_data.append(0)
        elif data[2] == 'Yes':
            current_data.append(1)

        if data[3] == 'Normal':
            current_data.append(0)
        elif data[3] == 'Reduced':
            current_data.append(1)

        if data[4] == 'No':
            recommended.append(0)
        elif data[4] == 'Yes':
            recommended.append(1)

        X.append(current_data)


    #print("XXXXXX")
    #print(X)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> addd your Python code here
    # Y =

    Y = recommended

    #print("YYYYYYYYYYYYYY")
    #print(Y)

    #loop your training and test tasks 10 times here
    accuracy = []
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

       #tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
       #plt.show()



       #read the test data and add this data to dbTest
       #--> add your Python code here
       # dbTest =

        dbTest = []

        with open('contact_lens_test.csv', 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTest.append (row)

        #print('dbTest')
        #print(dbTest)

        class_true = 0
        class_false = 0

        for data in dbTest:

            #print("data")
            #print(data)
            #transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here

            current_data = []
            if data[0] == 'Young':
                current_data.append (0)
            elif data[0] == 'Presbyopic':
                current_data.append (1)
            elif data[0] == 'Prepresbyopic':
                current_data.append (2)

            if data[1] == 'Myope':
                current_data.append(0)
            elif data[1] == 'Hypermetrope':
                current_data.append(1)

            if data[2] == 'No':
                current_data.append(0)
            elif data[2] == 'Yes':
                current_data.append(1)

            if data[3] == 'Normal':
                current_data.append(0)
            elif data[3] == 'Reduced':
                current_data.append(1)

            if data[4] == 'No':
                current_data.append(0)
            elif data[4] == 'Yes':
                current_data.append(1)


            #print('predicting')
            class_predicted = clf.predict([[current_data[0], current_data[1], current_data[2], current_data[3]]])
            #print(class_predicted)


    


           

            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            if current_data[4] == class_predicted[0]:
                class_true = class_true + 1
            else:
                class_false = class_false + 1

        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here
        accuracy.append(float(class_true)/ (class_true + class_false))
        #print('accuracy this run:' , (float(class_true)/ (class_true + class_false)))

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
   
    print('10x accuracy training', ds, accuracy)
    print('minimum acc ', ds , min(accuracy))

