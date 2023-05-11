#!/usr/bin/env python
# coding: utf-8

# needs TF so: conda activate tensorflow
import keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


# Load the CSV file
df = pd.read_csv(r'data/data.csv')

df.head()


# We'll split the data into input features and the target variable, MMI:
data = df
X = data[['M', 'logR', 'PGA', 'Ia', 'CAV']]
y = data['MMI']

# Next, we generate training & testing sets:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# we generate the Deep-Learning model: we use fully-connected Convolutional NN with 1 hidden layer:
model = Sequential()
model.add(Dense(10, input_dim=5, activation='relu'))
model.add(Dense(1))

# Next, we'll compile the model and specify the loss function and optimizer:
model.compile(loss='mse', optimizer='adam')

# we train the model:
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# We evaluate the model against the testing set:
mse = model.evaluate(X_test, y_test)

# to get the error of the predicted, we use the MSE:
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)


# In[10]:


print(mse)


# In[ ]:


get_ipython().system('jupyter nbconvert --t')

