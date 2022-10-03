#-------------------------------------------------------------------------
# AUTHOR: Leonardo Langgeng
# FILENAME: naive_bayes.py
# SPECIFICATION: predict whether or not to play tennis using naive bayes algo
# FOR: CS 4210- Assignment #2
# TIME SPENT: 4 hrs
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here
weather_training = []
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         weather_training.append (row)
print('weather_training', weather_training)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =

X = []
Y = []
for data in weather_training:
    print(data)

    current_data = []
    if data[1] == 'Sunny':
        current_data.append (1)
    elif data[1] == 'Overcast':
        current_data.append (2)
    elif data[1] == 'Rain':
        current_data.append (3)

    if data[2] == 'Hot':
        current_data.append(1)
    elif data[2] == 'Mild':
        current_data.append(2)
    elif data[2] == 'Cool':
        current_data.append(3)

    if data[3] == 'Normal':
        current_data.append(1)
    elif data[3] == 'High':
        current_data.append(2)

    if data[4] == 'Weak':
        current_data.append(1)
    elif data[4] == 'Strong':
        current_data.append(2)

    X.append(current_data)

    #transform the original training classes to numbers and add them to the vector Y.
    #For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =

    if data[5] == 'No':
        Y.append(1)
    elif data[5] == 'Yes':
        Y.append(2)


print('===========')
print('X',X)
print('-----')
print('Y', Y)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here

weather_test = []
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         weather_test.append (row)
         print(row)


Z = []
for data in weather_test:
    print(data)

    current_data = []
    if data[1] == 'Sunny':
        current_data.append (1)
    elif data[1] == 'Overcast':
        current_data.append (2)
    elif data[1] == 'Rain':
        current_data.append (3)

    if data[2] == 'Hot':
        current_data.append(1)
    elif data[2] == 'Mild':
        current_data.append(2)
    elif data[2] == 'Cool':
        current_data.append(3)

    if data[3] == 'Normal':
        current_data.append(1)
    elif data[3] == 'High':
        current_data.append(2)

    if data[4] == 'Weak':
        current_data.append(1)
    elif data[4] == 'Strong':
        current_data.append(2)

    Z.append(current_data)


#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))
print('======================================================================================================================')
#use your test samples to make probabilistic predictions. For : clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here

for i,each in enumerate(Z):
    pred = clf.predict_proba([[each[0], each[1], each[2], each[3]]])

    if pred[0][0] >= 0.75:
        print (str(weather_test[i][0]).ljust(15) + str(weather_test[i][1]).ljust(15) + str(weather_test[i][2]).ljust(15) + str(weather_test[i][3]).ljust(15) + str(weather_test[i][4]).ljust(15) + "NO".ljust(15) + str(pred[0][0]).ljust(15))
    elif pred[0][1] >= 0.75:
        print (str(weather_test[i][0]).ljust(15) + str(weather_test[i][1]).ljust(15) + str(weather_test[i][2]).ljust(15) + str(weather_test[i][3]).ljust(15) + str(weather_test[i][4]).ljust(15) + "YES".ljust(15) + str(pred[0][1]).ljust(15))
    



