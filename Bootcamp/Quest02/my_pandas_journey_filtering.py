import numpy as np 
import pandas as pd
def my_pandas_journey_filtering(param_1, param_2):
        df = pd.DataFrame(param_1)
        return df.filter(regex=param_1,param_2, axis=1)