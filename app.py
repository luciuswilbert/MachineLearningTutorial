from sklearn.tree import DecisionTreeRegressor

import pandas as pd

melbourne_data = pd.read_csv("melb_data.csv")
print(melbourne_data.describe())
print(melbourne_data.columns)

melbourne_data = melbourne_data.dropna(axis=0)
print(melbourne_data.describe())

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = melbourne_data[melbourne_features]
print(x.describe())
print(x.head())

melbourne_model = DecisionTreeRegressor(random_state=1)

melbourne_model.fit(x, y)

print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(melbourne_model.predict(x.head()))