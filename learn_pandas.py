import pandas as pd

sample_data = pd.read_csv('sample.csv')
# print(sample_data.Region.value_counts())
# print(sample_data.groupby('Region').Region.count())
# print(sample_data.sort_values(by='len', ascending = False))
print(sample_data.dtypes)
print(sample_data.UnitsSold.dtype)