#!/usr/bin/env python
# coding: utf-8

# # Anomaly Detection In IoT Sensor Networks
#  

# In this project, we aim to identify anomalies in Industrial IoT Pump Sensor Networks.
# The network consists of various nodes that monitors the pressure values of valves at different locations of networks.
# In case some of these are blocked, a centralized controller is able to re-route through pre-defined routes.
# If such a re-routing is not possible and the system comes to a halt, the controller must recognize the anomaly.
# We aim to develop a solution that pin-points the source of error and allows us to fix any anomalies
# 

# # Load data

# In[1]:


# load the dataset 
import pandas as pd
import numpy as np

df = pd.read_csv('sensor.csv')
df.head()


# In[11]:


# convert time into index 
df['index'] = pd.to_datetime(df['timestamp'])
df.index = df['index']


# In[12]:


# delete the colunmns 
del df['index']
del df['timestamp']


# In[13]:


df.head(2)


# In[14]:


df['sensor_15'].nunique() # no unique - complete zero
# drop the column 
df.drop(['sensor_15'], axis=1, inplace = True)
df.shape


# In[15]:


df.info()


# In[16]:


# machine status - no null 
# we will drop na in whole dataframe 
df['sensor_00'].isna().sum()


# In[17]:


# machine status
df['machine_status'].unique()#'NORMAL', 'BROKEN', 'RECOVERING' 
df['machine_status'].value_counts()


# In[18]:


# draw a countplot for machine status 
import seaborn as sns
sns.countplot(y = df['machine_status'])


# 
# * it is highly imbalanced data
# * we will experiement with SMOTE or oversampling 

# In[19]:


# apply label encoder to encode the machine status
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['machine_status'] = le.fit_transform(df['machine_status'])
df['machine_status'].value_counts()

# 1 - normal 
# 2 - recovering 
# 0 - broken


# In[20]:


#  look on complete data frame when device is broken
df_broken = df[df.machine_status ==0]
df_broken


# In[21]:


import matplotlib.pyplot as plt 
plt.plot(df['sensor_02'])


# In[22]:


# imputation for null values 
df['sensor_04'].hist()
# data is skewwed so we need to use median value to fill the data


# In[25]:


# used ffill method to fill the missing values
df = df.fillna(method='ffill')


# In[26]:


X = df.drop(['machine_status'], axis=1)
Y = df['machine_status']


# # Models

# In[ ]:


from imblearn.over_sampling import SMOTE
oversample = SMOTE()
X, y = oversample.fit_resample(X, y)


# In[29]:


# apply the logitic regression 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.30, random_state = 42)


# In[ ]:


from sklearn.ensemble import RandomForestClassifier
rnd_clf = RandomForestClassifier(n_estimators = 100 , criterion = 'entropy',random_state = 0)
rnd_clf.fit(X,y)


# In[ ]:


from sklearn.ensemble import IsolationForest
imodel=IsolationForest(n_estimators=100,max_samples='auto',contamination=float(0.2),random_state=random_state)
imodel.fit(X)
print(model.get_params())


# In[30]:


from sklearn.linear_model import LogisticRegression
logit = LogisticRegression()
lmodel = logit.fit(X_train, y_train)


# # Testing

# In[31]:


# predict
y_pred = lmodel.predict(X_test)
y_pred2 = rnd_clf.predict(X_test)
y_pred3 = imodel.predic(X_test)


# In[32]:


# evaluate the model
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
cm = pd.crosstab(y_test,y_pred, rownames=['True'], colnames=['Predicted'], margins=True)
cm


# In[33]:


accuracy = accuracy_score(y_test, y_pred)
accuracy


# In[ ]:


print(roc_auc_score(y_test, y_pred))
print(roc_auc_score(y_test, y_pred1))
print(roc_auc_score(y_test, y_pred2))

