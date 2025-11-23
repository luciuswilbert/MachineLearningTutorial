from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

import pandas as pd

def get_mae(max_leaf_nodes, train_x, val_x, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state = 1)
    model.fit(train_x, train_y)
    prediction = model.predict(val_y)


melbourne_data = pd.read_csv("melb_data.csv")

melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = melbourne_data[melbourne_features]

# Splitting
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state = 42)

melbourne_model = DecisionTreeRegressor(random_state=1)

melbourne_model.fit(train_x, train_y)

# print("Making predictions for the following 5 houses:")
# print(x.head())
# print("The predictions are")
# print(melbourne_model.predict(x.head()))

predicted_home_prices = melbourne_model.predict(val_x)
print("Mean Absolute Error: ", mean_absolute_error(val_y, predicted_home_prices))
