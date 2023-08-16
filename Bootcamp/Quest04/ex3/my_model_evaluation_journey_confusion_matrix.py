import pandas as pd 
import numpy as np
from sklearn.metrics import confusion_matrix
def my_model_evaluation_journey_confusion_matrix(param_1, param_2):
    df1 = np.array(param_1)
    df2 = np.array(param_2)
    return confusion_matrix(df1, df2)