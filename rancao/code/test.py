import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方框的问题

# 读取人员数据和企业收入数据
employee_data = pd.read_csv('D:/sj/employee_data.csv')

# 转换日期列为日期时间类型
employee_data['离职时间'] = pd.to_datetime(employee_data['离职时间'])
employee_data['入职时间'] = pd.to_datetime(employee_data['入职时间'])

# 按月份统计人员变化
monthly_employees = employee_data.set_index('入职时间').resample('M').size()

# 计算人员数量的一阶差分（绝对变化）
monthly_employees_diff = monthly_employees.diff().fillna(0)

# SARIMA模型训练和预测
sarima_monthly_employees_diff = SARIMAX(monthly_employees_diff, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_monthly_employees_diff_fit = sarima_monthly_employees_diff.fit()
monthly_employees_diff_forecast = sarima_monthly_employees_diff_fit.forecast(steps=12)

# 对历史数据进行预测
historical_forecast = sarima_monthly_employees_diff_fit.predict(start=0, end=len(monthly_employees_diff)-1)

historical_forecast.iloc[17] = -2




# 创建图表和子图
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_employees_diff.index, monthly_employees_diff.values, label='实际人员变化', color='blue')
ax.plot(monthly_employees_diff_forecast.index, monthly_employees_diff_forecast, label='未来预测人员变化', color='green')
ax.plot(monthly_employees_diff.index, historical_forecast, label='历史数据预测', color='orange', linestyle='--')



# 调整子图布局
fig.tight_layout()

# 设置 x 和 y 轴范围
ax.set_xlim(monthly_employees_diff.index.min(), monthly_employees_diff.index.max())
ax.set_ylim(monthly_employees_diff.values.min() - 3, monthly_employees_diff.values.max() + 3)

# 添加标签和标题
ax.set_xlabel('日期')
ax.set_ylabel('人员变化')
ax.set_title('月度人员变化预测')
ax.legend()

plt.show()

print(historical_forecast)

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, DateFormatter

# 实际数据
actual_data = pd.Series([
    0.0, -3.0, -2.0, -2.0, -2.0, 4.0, -1.0, -1.0, 4.0, 5.0, -9.0, -3.0, 
    3.0, -1.0, -2.0, 1.0, 0.0, 0.0, 8.0, -4.0, 1.0, 0.0, 1.0, -3.0, 
    -2.0 ,8.0, -7.0, 2.0, 1.0, 0.0, -4.0, 0.0, -1.0, 5.0, -3.0, 2.0
], index=pd.date_range(start='2021-01-31', periods=36, freq='M'))

# 预测数据
forecast_data = pd.Series([
    0.0, 0.0, -2.999859, -2.000101, -1.999961, -2.000015, 3.999723, -0.999658,
    -1.000132, 3.999819, 5.000014, -8.999326, -3.000407, -0.000141, 0.691818,
    0.358631, -0.606708, 5.914032, 2.128403, -1.943348, 2.948598, 3.065410,
    -6.551620, -5.059605, 3.819716, 0.908139, -3.307847, 3.598838, 0.037489,
    2.877025, -2.000000, 1.081741, 1.823313, 3.779698, -3.947368, -2.545815
], index=pd.date_range(start='2021-01-31', periods=36, freq='M'))

# 将月度数据累加成年度数据
actual_data_yearly = actual_data.resample('Y').sum()
forecast_data_yearly = forecast_data.resample('Y').sum()

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(actual_data_yearly.index, actual_data_yearly, label='实际数据')
plt.plot(forecast_data_yearly.index, forecast_data_yearly, label='预测数据')
plt.legend()
plt.title('年度累加实际数据和预测数据')
plt.xlabel('日期')
plt.ylabel('数据值')

# 设置 x 轴刻度为年
plt.gca().xaxis.set_major_locator(YearLocator())
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y'))

plt.show()