import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

asos_all = pd.read_csv("dataset/asos_rawdata.csv")

asos_all["일시"]=pd.to_datetime(asos_all["일시"])

unique_time_list = sorted(list(set(asos_all['일시']))) # 측정 일시 종류 확인

print(unique_time_list) # AMOS 측정 일시 데이터 확인
print(len(set(asos_all['일시']))) # 측정 일시 종류 확인
print(sorted(list(set(asos_all['지점명'])))) # ASOS 측정 지점명 데이터 확인
print(len(set(asos_all['지점명']))) # 측정 지점명 종류 확인
asos_all.describe() # asos_all DataFrame 통계수치 확인
