import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('Hungry.csv')
for i in range(1,len(df)):
  if 'train' in df.loc[i]['id']:
    continue
  else:
    df1 = df[:i]
    df2 = df[i:]
    break
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression(random_state=16,max_iter=1000000)
feature_cols = ['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']
X_train = df1[feature_cols]
Y_train = df1['target_binary']
# fit the model with data
logreg.fit(X_train,Y_train)

y_pred = logreg.predict(df2[feature_cols])
print(y_pred)
y_pred=y_pred.tolist()
df2['target_binary']=y_pred
print(df2)
