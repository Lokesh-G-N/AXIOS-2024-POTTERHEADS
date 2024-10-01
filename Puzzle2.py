import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('final_dataset.csv', skipfooter=438000)

plt.scatter(df['x'],df['y'])
plt.show()
