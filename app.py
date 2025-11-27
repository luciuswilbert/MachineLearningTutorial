import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

numerical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='median')),
                              ('scaler', StandardScaler()),
                              ])
categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')),
                              ('one_hot', OneHotEncoder()),
                              ])

preprocessor = ColumnTransformer(transformers=[('numerical', numerical_transformer, numerical_cols),
                                               ('categorical', categorical_transformer, categorical_cols),
                                               ])

final_pipeline = Pipeline(steps=[('preprocess', preprocessor),
                                 ('model', RandomForestRegressor(n_estimators=50, random_state=42))
                                 ])