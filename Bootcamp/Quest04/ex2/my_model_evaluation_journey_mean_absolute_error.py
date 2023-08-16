import pandas as pd 
import numpy as np
from sklearn.metrics import mean_absolute_error
def my_model_evaluation_journey_mean_absolute_error(param_1, param_2):
    df1 = pd.read_csv(param_1)
    df2 = pd.read_csv(param_2)
    return mean_absolute_error(df1.iloc[:, 1:], df2.iloc[0:len(df1), 1:])