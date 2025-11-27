import pandas as pd
from sklearn.model_selection import train_test_split

sample_data = pd.read_csv('sample.csv')
print(sample_data.nunique())