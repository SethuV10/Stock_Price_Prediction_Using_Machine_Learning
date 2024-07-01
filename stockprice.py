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
