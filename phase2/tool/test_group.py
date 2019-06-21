# coding=gbk
import pandas as pd
import numpy as np

np.random.seed(1)

""" 1. groupby, �������, ����, ��� """
df = pd.DataFrame({
    "key1": ["a", "a", "b", "b", "a"],
    "key2": ["one", "two", "one", "two", "one"],
    "data1": [np.nan,2,3,4,5],
    "data2": [6,7,8,9,10]
})

# ��key1����, ����data1�е�ƽ��ֵ
key1 = df.groupby(df["key1"])['data1'].count()

print(df)
print(key1)
