import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dataframe_to_list(dataframe):
    "DataFrame转换为list类型"
    return np.array(dataframe)

def date_and_frequency(data_l):
    "返回x,y值"
    frequency_ = []
    date_ = []
    for date in data_l:
        date_.append(date[0])
        frequency_.append(int(date[-1]))
    return date_, frequency_

file_path = "file_path"

dataframe = pd.read_excel(file_path, sheetname='sheetname')
data_l = dataframe_to_list(dataframe)
frequency_ = date_and_frequency(data_l)[-1]

plt.plot(range(len(data_l)), frequency_)
# plt.scatter(range(len(data_l)), frequency_)
plt.show()
plt.close()
