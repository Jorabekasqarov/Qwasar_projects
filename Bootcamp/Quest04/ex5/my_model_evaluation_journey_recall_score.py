import pandas as pd 
import numpy as np
from sklearn.metrics import recall_score
def my_model_evaluation_journey_recall_score(param_1, param_2):
    df1 = np.array(param_1)
    df2 = np.array(param_2)
    return recall_score(df1, df2, average=None)