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

amos_gimpo = amos_all[amos_all['지점명'] == '김포공항'] # 김포공항 데이터만 추출
amos_gimpo = amos_gimpo.drop(['지점'], axis=1) # 불필요한 지점 컬럼 제거
amos_gimpo.sort_values(by='일시', inplace=True) # 측정 일시에 따라 정렬
amos_gimpo.loc[amos_gimpo['강수량(mm)'].isnull(), '강수량(mm)'] = 0 # 강수량의 결측치를 0으로 대체

def knot_to_ms(knot):
    return knot * 0.514444

amos_gimpo['풍속(m/s)'] = knot_to_ms(amos_gimpo['풍속(KT)'])


# 측정 시간에 따른 풍속 변화 확인
plt.figure(figsize=(15, 5))
plt.plot(amos_gimpo['일시'], amos_gimpo['풍속(m/s)'])



# 측정 시간에 따른 기온 변화 확인 (전체 지점)
# 일반 plot과 이동 평균을 같이 확인
plt.figure(figsize=(15, 5))
window_size = 120 # 5일 치 데이터를 이용하여 이동 평균 계산

plt.plot(amos_gimpo['일시'], amos_gimpo['풍속(m/s)'], alpha=0.5)
plt.plot(amos_gimpo['일시'], amos_gimpo['풍속(m/s)'].rolling(window=window_size).mean())



# 측정 시간에 따른 기온 변화 확인
plt.figure(figsize=(15, 5))
plt.plot(amos_gimpo['일시'], amos_gimpo['기온(°C)'])

plt.figure(figsize=(15, 5))

plt.plot(amos_gimpo['일시'], amos_gimpo['기온(°C)'])
plt.plot(amos_gimpo['일시'], amos_gimpo['이슬점온도(°C)'])
