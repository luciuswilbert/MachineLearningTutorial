import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fifa_data = pd.read_csv('fifa.csv', index_col='Date', parse_dates=True)
print(fifa_data.head())