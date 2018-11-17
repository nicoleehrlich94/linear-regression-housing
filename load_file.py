import pandas as pd


def load_csv(file_path):
   return pd.read_csv(file_path, index_col=None, low_memory=False)
print(load_csv("housing.csv"))
