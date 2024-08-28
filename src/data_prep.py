import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def load_data(filePath: str)-> pd.DataFrame:
    try:
        return pd.read_csv(filePath)
    except Exception as e:
        raise Exception(f"Error loading data from {filePath} : {e}")

# train_data = pd.read_csv('./data/raw/train.csv')
# test_data = pd.read_csv('./data/raw/test.csv')

def fill_missing_with_median(data):
    for col in data.columns:
        if data[col].isnull().any():
            median_val = data[col].median()
            data[col].fillna(median_val, inplace=True)

    return data





def save_data(df: pd.DataFrame, filePath:str) -> None:
    try:
        return df.to_csv(filePath, index=False)
    except Exception as e:
        raise Exception(f"Error to save dataframe in {filePath} : {e}")
    

# processed_train.to_csv(os.path.join(data_path, 'processed_train.csv'), index=False)
# processed_test.to_csv(os.path.join(data_path, 'processed_test.csv'), index=False)

def main():
    try:
        raw_data_path = "./data/raw"
        processed_data_path = "./data/processed"

        train_data = load_data(os.path.join(raw_data_path, "train.csv"))
        test_data  = load_data(os.path.join(raw_data_path, "test.csv"))

        processed_train = fill_missing_with_median(train_data)
        processed_test  = fill_missing_with_median(test_data)

        os.makedirs(processed_data_path)

        save_data(processed_train, os.path.join(processed_data_path, "processed_train.csv"))
        save_data(processed_test, os.path.join(processed_data_path, "processed_test.csv"))
    
    except Exception as e:
        raise Exception(f"an error occured {e}")


if __name__ == "__main__":
    main()



















