import pandas as pd 
def my_pandas_journey_return_n_rows(param_1, param_2):
    data = pd.DataFrame(param_1)
    return data.iloc[:param_2]

