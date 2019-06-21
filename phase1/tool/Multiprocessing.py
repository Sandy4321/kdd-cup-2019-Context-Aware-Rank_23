
#pandas��û��ֱ�Ӷ���̵ķ����������ǽ�  ԭʼapply�ĳ� group ֮��ķ�ʽʵ�֣���������ȡ��������ʱ�䡣   ���Է�����Ҫ�Ƕ��������������
'''

��Ӧ����ʽ��ԭʼ����ʽΪ��
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

def add_labels(filenam,df):
	list_name = list(df['name'])
	if filename in list_name:
		i = list_name.index(filename)
		return df['�Ƿ���][i]
	else:
		return 'Nan'

df1['�Ƿ���'] = df1['name'].apply(add_labels, args=(df2,))
'''
import pandas as pd
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

from joblib import Parallel, delayed
def add_labels(filename, df):
    list_name = list(df['name'])
    if filename in list_name:
        i = list_name.index(filename)
        return df['�Ƿ���'][i]
    else:
        return 'Nan'


def tmp_func(df1):
    df1['�Ƿ���'] = df1['name'].apply(add_labels, args=(df2,))
    return df1


def apply_parallel(df_grouped, func):
    results = Parallel(n_jobs=10)(delayed(func)(group) for name, group in df_grouped)
    return pd.concat(results)


df_grouped = df1.groupby(df1.index)
df1 = apply_parallel(df_grouped, tmp_func)
