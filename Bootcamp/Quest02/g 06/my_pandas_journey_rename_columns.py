import numpy as np 
import pandas as pd 
def my_pandas_journey_rename_columns(param_1, param_2, param_3):
    df = pd.DataFrame(param_1)
    return df.rename(columns={param_2:param_3})