import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

sample_data = pd.read_csv('sample.csv')
sample_data = sample_data.dropna(axis=0, subset=['CostPerUnit'], inplace=True)
print(sample_data)
