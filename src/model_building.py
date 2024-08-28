import pandas as pd
import numpy as np
import os
import yaml
import pickle
from sklearn.ensemble import RandomForestClassifier

def load_data(filePath: str) -> pd.DataFrame:
    try:
        return pd.read_csv(filePath)
    except Exception as e:
        raise Exception("Error loading data from {filePath} : {e}")

# train_data = pd.read_csv('./data/processed/processed_train.csv')

def prepare_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    try:
        X = data.drop(columns=['Potability'], axis=1)
        y = data['Potability']
        return X,y
    except Exception as e:
        raise Exception(f"Error in data prepairing as {e}")
#  this is numpy array without having columns name
# X_train = train_data.iloc[:, 0:-1].values
# y_train = train_data.iloc[:, -1].values

def load_params(filePath: str) -> float:
    try:
        with open(filePath, "r") as file:
            params = yaml.safe_load(file)
        return params["model_building"]["n_estimators"]
    except Exception as e:
        raise Exception(f"Error loading parameters from {filePath} : {e}")

# this is pandas formate that already have columns name
# X_train = train_data.drop(columns=['Potability'], axis=1)
# y_train = train_data['Potability']

# n_est = yaml.safe_load(open("params.yaml", "r"))["model_building"]["n_estimators"]
# depth = yaml.safe_load(open("params.yaml", "r"))["model_building"]["max_depth"]

def train_model(X:pd.DataFrame, y:pd.Series, n_estimators: int)->RandomForestClassifier:
    try:
        clf = RandomForestClassifier(n_estimators=n_estimators)
        clf.fit(X, y)
        return clf
    except Exception as e:
        raise Exception(f"Error model training : {e}")

# clf = RandomForestClassifier(n_estimators = n_est)
# clf.fit(X_train, y_train)

def save_model(model:RandomForestClassifier, filePath: str) -> None:
    try:
        with open(filePath, 'wb') as f:
            pickle.dump(model, f)
    except Exception as e:
        raise Exception(f"Error save model : {e}")

# pickle.dump(clf, open("model.pkl",'wb'))

def main():
    

    try:
        data_path = './data/processed/processed_train.csv'
        params_path = "params.yaml"
        model_path = "model.pkl"
        train_data = load_data(data_path)
        n_est = load_params(params_path)
        X_train, y_train = prepare_data(train_data)
        model = train_model(X_train, y_train, n_est)
        save_model(model, model_path)
    except Exception as e:
        raise Exception(f"An error occured : {e}")

if __name__=="__main__":
    main()