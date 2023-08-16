import pandas as pd 
def my_pandas_journey_return_n_columns(param_1, param_2):
    data = pd.DataFrame(param_1)
    return data.get(data.columns[:param_2])