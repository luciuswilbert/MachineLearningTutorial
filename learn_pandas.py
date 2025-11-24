import pandas as pd

# data_frame = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
# data_frame2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful'], 'Sue': ['Pretty good.', 'Bland']})
# data_frame3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful'], 'Sue': ['Pretty good.', 'Bland']}, index=['Product A', 'Product B'])

# series_1 = pd.Series([1, 2, 3, 4, 5])
# series_2 = pd.Series([1, 2, 3], index=['2015 Sales', '2020 Sales', '2025 Sales'], name='Product A')

# print(data_frame)
# print(data_frame2)
# print(data_frame3)

# print(series_1)
# print(series_2)

sample_data = pd.read_csv('sample.csv')
print(sample_data)
# print(sample_data.shape)
# print(sample_data.loc[:,'Region':'Revenue'])
# print(sample_data.loc[(sample_data.Region != 'East') & (sample_data.UnitsSold >= 100)]) 
# print(sample_data.loc[(sample_data.Region.isin(['East', 'West'])) & (sample_data.Revenue >= 100)])
# print(sample_data.loc[sample_data.CostPerUnit.notnull()])
# print(sample_data.loc[:,'ProductCategory':'UnitsSold'])
# print(sample_data.iloc[0])

# print(sample_data.Region.value_counts())

print(sample_data.Region.map(lambda x : x.lower()))