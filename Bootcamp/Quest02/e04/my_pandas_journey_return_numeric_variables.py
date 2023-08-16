import pandas as pd 
import numpy as np
def my_pandas_journey_return_numeric_variables(param_1):
    data = pd.DataFrame(param_1)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    return data.select_dtypes(include=numerics)