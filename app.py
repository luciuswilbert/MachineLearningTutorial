from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

import pandas as pd

def get_mae(max_leaf_nodes, train_x, val_x, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state = 1)
    model.fit(train_x, train_y)
    prediction = model.predict(val_x)
    mae = mean_absolute_error(val_y, prediction)
    return mae

melbourne_data = pd.read_csv("melb_data.csv")

melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = melbourne_data[melbourne_features]

# Splitting
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state = 42)

# for max_leaf_nodes in [5, 50, 500, 5000]:
#     my_mae = get_mae(max_leaf_nodes, train_x, val_x, train_y, val_y)
#     print(f"Max leaf nodes: {max_leaf_nodes} \nMean Absolute Error: {my_mae}")

forest_model = RandomForestRegressor(random_state = 1)
forest_model.fit(train_x, train_y)
predictions = forest_model.predict(val_x)
print(mean_absolute_error(val_y, predictions))