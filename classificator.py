import numpy as np
from load_df import load_cases
X,Y = load_cases()

X_per = len(X[0:int(len(X)*0.9)]) #Take the first 90% attributes to train
Y_per = len(Y[0:int(len(X)*0.9)]) #Take the first 90% results to train

print(X_per)
print(Y_per)

data_train = X[:X_per] #Take the first 90% attributes to train
results_train = Y[:Y_per] #Take the first 90% results to train

data_test = X[int(len(X)*0.9):]#take the last 10% to test the AI
results_test = Y[int(len(X)*0.9):]

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(data_train, results_train)#training with the first 90 data

result = model.predict(data_train)#The AI will try to predict the last 10% of cases

dif = result - results_test#Difference between the results and the test results
matchs = [d for d in dif if d == 0]#count of matchs
total_matchs = len(matchs)
total_elements = len(data_test)

match_percentage = 100.0 * total_matchs / total_elements

print(match_percentage)
print(total_elements)
