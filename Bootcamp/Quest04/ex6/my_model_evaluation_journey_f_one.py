import pandas as pd 
import numpy as np
from sklearn.metrics import f1_score
def my_model_evaluation_journey_f_one(param_1, param_2):
    df1 = np.array(param_1)
    df2 = np.array(param_2)
    return f1_score(df1, df2, average=None)