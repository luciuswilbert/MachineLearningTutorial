import pandas as pd
from sklearn.model_selection import train_test_split

sample_data = pd.read_csv('sample.csv')
# sample_data.dropna(axis=0, subset=['CostPerUnit'], inplace=True)
# print(sample_data)
sample_data = sample_data.select_dtypes(exclude=['object'])
print(sample_data)
sample_data = sample_data.isnull().sum()
print(sample_data[sample_data > 0])