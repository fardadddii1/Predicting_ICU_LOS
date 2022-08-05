import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import sklearn
from sklearn.preprocessing import OneHotEncoder

def encode_many(dataframe,feat):
    
    ohe = OneHotEncoder(handle_unknown='ignore')
    gf = (ohe.fit_transform(dataframe[[feat]]))
    gf = gf.toarray()

    temp = []
    for yt in range(1,len(pd.unique(dataframe[feat]))+1):
        col_name = (feat.lower()).capitalize()
        col_name = col_name+str(yt)
        temp.append(col_name)
    
    temp_df = DataFrame(gf, columns = temp)
    
    return temp_df