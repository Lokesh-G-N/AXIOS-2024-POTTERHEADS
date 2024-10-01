import pandas as pd
import numpy as np

df1 = pd.read_csv('EmployeeData.csv')
df2 = pd.read_csv('DepartmentData.csv')
l1 = {}
for i in range(1,20):
  q = df2.loc[i-1, 'tax_rate']
  l = []
  for index, row in df1.iterrows():
    if row['department_id'] == i:
      y=row['base_salary']+row['bonus']
      y=y-(y*q)
      l.append(y)
  l1[i] = np.mean(l)
l2 =sorted(l1.items(), key=lambda kv: (kv[1], kv[0]))
for i in l2[::-1]:
  x=df2.loc[i[0]-1, 'department_name']
  print(x[0])
