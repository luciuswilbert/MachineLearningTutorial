import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

my_pipeline = Pipeline(steps=[('imputer', SimpleImputer(strategy='median')),
                              ('scaler', StandardScaler())
                              ])