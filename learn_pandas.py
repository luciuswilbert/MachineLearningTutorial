import pandas as pd

df1 = pd.DataFrame({'A': [1], 'B': [2]}, index=[0])
df2 = pd.DataFrame({'B': [3], 'C': [4]}, index=[1])

print(df1, df2)

vertical_stack = pd.concat([df1, df2])
print(vertical_stack)

horizontal_stack = pd.concat([df1, df2], axis = 1)
print(horizontal_stack)