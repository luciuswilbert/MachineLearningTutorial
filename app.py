import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

numerical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='median')),
                              ('scaler', StandardScaler()),
                              ])
categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')),
                              ('one_hot', OneHotEncoder()),
                              ])