import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

amos_all = pd.read_csv("amos_rawdata.csv")

unique_time_list = sorted(list(set(amos_all['일시']))) # 측정 일시 종류 확인
print(unique_time_list) # AMOS 측정 일시 데이터 확인
print(len(set(amos_all['일시']))) # 측정 일시 종류 확인

print(sorted(list(set(amos_all['지점명'])))) # AMOS 측정 지점명 데이터 확인
print(len(set(amos_all['지점명']))) # 측정 지점명 종류 확인

##amos_all["지점명"].value_counts()
"""precipitation_mean = amos_all["강수량(mm)"].mean()
precipitation_std = amos_all["강수량(mm)"].std()"""

amos_all.describe()

