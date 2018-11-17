import pandas as pd
import matplotlib.pyplot as plt

housing = pd.read_csv("train.csv")
housing_info = housing.info()
corr_matrix = housing.corr()
housing_corr = corr_matrix.SalePrice.sort_values(ascending=False)
attrb = housing_corr.keys()[0:6]
print(attrb)

from pandas.plotting import scatter_matrix

scatter_matrix(housing[attrb], figsize=(12, 8))
plt.show()

# Experiment with some other attribute combinations