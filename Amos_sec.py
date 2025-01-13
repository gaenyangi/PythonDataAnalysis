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



diff_rain = asos_incheon['일강수량(mm)'] - asos_ulsan['일강수량(mm)']
abs_diff_rain = abs(diff_rain) 
most_diff_rain = abs_diff_rain[abs_diff_rain == abs_diff_rain.max()]
most_diff_precipitation_date = most_diff_rain.index[0]
print(most_diff_precipitation_date)


incheon_temp_slp_corr = asos_incheon['평균기온(°C)'].corr(asos_incheon['평균 해면기압(hPa)'])
print(incheon_temp_slp_corr)
ulsan_temp_slp_corr = asos_ulsan['평균기온(°C)'].corr(asos_ulsan['평균 해면기압(hPa)'])
print(ulsan_temp_slp_corr)

# 두 데이터를 같이 그래프로 그리기
plt.plot(asos_incheon['평균기온(°C)']) # 앞에서 '일시' 데이터를 index로 지정했으므로, '일시' 데이터를 x축으로 사용하지 않아도 됩니다.
plt.plot(asos_incheon['평균 해면기압(hPa)'])
plt.show() # 캔버스에 올라간 그림을 모두 보여줍니다.


# 산점도 그리기
plt.scatter(asos_incheon['평균기온(°C)'], asos_incheon['평균 해면기압(hPa)'])
plt.show()

q2_corr = asos_incheon['일강수량(mm)'].corr(asos_incheon['평균 해면기압(hPa)'])
print(q2_corr)


# pd.read_csv를 통하여 항공기상관측(AMOS) 기상청 데이터를 데이터프레임 형태로 읽어옵니다.
amos_all = pd.read_csv("dataset/amos_rawdata.csv")
amos_all['일시'] = pd.to_datetime(amos_all['일시'])
# AMOS 데이터의 칼럼명 중 '지점명' 을 '지점' 으로 변경
amos_all.rename(columns={'지점명':'지점'}, inplace=True)

amos_ulsan = amos_all[amos_all['지점'] == '울산공항']
amos_incheon = amos_all[amos_all['지점'] == '인천공항']

amos_ulsan.set_index('일시', inplace=True)
amos_incheon.set_index('일시', inplace=True)

plt.plot(amos_ulsan['최고기온(°C)']) # 원본 데이터에 평균 
plt.plot(amos_incheon['최고기온(°C)'])

plt.show()

# Hint. 공항기상관측['최고기온(°C)'] - 종관기상관측['최고기온(°C)'] >= 0인 데이터의 수를 구하면 됩니다.
# Hint2. 2.1챕터에서 데이터를 분리한 방법을 응용한 후, 그 분리된 데이터의 길이를 구할 수 있습니다.

incheon_amos_asos_temp_diff = amos_incheon['최고기온(°C)'] - asos_incheon['최고기온(°C)']
q3_higher_temp_count=len(incheon_amos_asos_temp_diff[incheon_amos_asos_temp_diff>=0])

print(q3_higher_temp_count)
