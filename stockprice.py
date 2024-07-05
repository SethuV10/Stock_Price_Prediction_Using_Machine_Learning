import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 
  
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression 
from sklearn.svm import SVC 
from xgboost import XGBClassifier 
from sklearn import metrics 
  
import warnings 
warnings.filterwarnings('ignore')

pip install matplotlib

import os
import pandas as pd 
abs_path = os.path.dirname('TSLA.csv')
print( 'path is',os.path )
df = pd.read_csv('C:\\Users\\alagu\\Downloads\\TSLA.csv')

df.shape

df.describe()

df.info()

import matplotlib.pyplot as plt
import pandas as pd 
plt.figure(figsize=(15,5)) 
df = pd.read_csv('C:\\Users\\alagu\\Downloads\\TSLA.csv')
plt.plot(df['Close']) 
plt.title('Tesla Close price.', fontsize=15) 
plt.ylabel('Price in dollars.') 
plt.show()

import pandas as pd 
df = pd.read_csv('C:\\Users\\alagu\\Downloads\\TSLA.csv')
df.head()

import pandas as pd 
df = pd.read_csv('C:\\Users\\alagu\\Downloads\\TSLA.csv')
df = df.drop(['Adj Close'], axis=1)
df.isnull().sum()
