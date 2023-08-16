import pandas as pd 
import numpy as np
from sklearn.metrics import accuracy_score
def my_model_evaluation_journey_accuracy_score(param_1, param_2):
    df1 = np.array(param_1)
    df2 = np.array(param_2)
    return accuracy_score(df1, df2)