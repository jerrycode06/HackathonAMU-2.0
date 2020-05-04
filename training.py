import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Imoprting dataset
df =  pd.read_csv('data.csv')

# Splitting into Dependent and Independent variables
X = df.iloc[:,:-1].values
Y = df.iloc[:,-1].values

# Splitting the dataset for training and testing
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
# Feature Scaling
'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''

# Training Model
model = RandomForestClassifier(n_estimators=300)
model.fit(X,Y)

# pred = model.predict_proba([[104,1,61,1,1]])

# Open a file, where you want to store the data
file = open('model.pkl', 'wb')
# a=[model, sc_X] when feature scaling is in effect dump this list in pickle
# Dump information to that file
pickle.dump(model, file)
file.close()