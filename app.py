import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

my_pipeline = Pipeline(steps=[('imputer', SimpleImputer(strategy='median')),
                              ('scaler', StandardScaler()),
                              ('model', RandomForestRegressor(n_estimators=50, random_state=42))
                              ])