import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt  

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签  

# 假设你的数据集名称为 employee_data.csv，包含离职时间字段 '离职时间' 和入职时间字段 '入职时间'
# 如果数据集是以其他格式或者存储在数据库中，你需要根据实际情况进行适当的读取操作
employee_data = pd.read_csv('D:/sj/employee_data.csv')

# 将 '离职时间' 字段和 '入职时间' 字段转换为日期时间类型
employee_data['离职时间'] = pd.to_datetime(employee_data['离职时间'])
employee_data['入职时间'] = pd.to_datetime(employee_data['入职时间'])

# 根据月份统计离职员工数量和入职员工数量
monthly_departures = employee_data['离职时间'].dt.to_period('M').value_counts().sort_index()
monthly_hires = employee_data['入职时间'].dt.to_period('M').value_counts().sort_index()

# 计算每个月的净员工数量变化
monthly_net_employees = monthly_hires - monthly_departures

# 计算净员工数量变化的绝对值
absolute_net_employees = monthly_net_employees.abs()

# 计算人力波动幅度
hr_fluctuation = absolute_net_employees.mean()  # 这里以平均值作为波动幅度，你可以根据需求选择其他指标

# 绘制人员波动曲线和离职员工数量曲线
plt.figure(figsize=(10, 6))
plt.plot(monthly_departures.index.to_timestamp(), monthly_departures.values, color='r', marker='o', label='离职')
plt.plot(monthly_hires.index.to_timestamp(), monthly_hires.values, color='g', marker='o', label='入职')
plt.xlabel('月份')
plt.ylabel('员工数量')
plt.title('每月员工数量变化')
plt.grid(True)
plt.legend()
plt.tight_layout()

# 保存第一个图到相对路径下
image_path_1 = 'image'
if not os.path.exists(image_path_1):
    os.makedirs(image_path_1)
plt.savefig(os.path.join(image_path_1, 'ren2.png'))

plt.show()

# 绘制净员工数量变化的绝对值随时间变化的曲线图
plt.figure(figsize=(10, 6))
plt.plot(absolute_net_employees.index.to_timestamp(), absolute_net_employees.values, color='b', marker='o')
plt.xlabel('月份')
plt.ylabel('员工净变化绝对值')
plt.title('每月员工净变化绝对值')
plt.axhline(y=hr_fluctuation, color='r', linestyle='--', label='平均变化')
plt.grid(True)
plt.tight_layout()

# 保存第二个图到相对路径下
image_path_2 = 'image'
if not os.path.exists(image_path_2):
    os.makedirs(image_path_2)
plt.savefig(os.path.join(image_path_2, 'ren1.png'))

plt.show()

print("企业内部人力波动幅度 (平均值):", hr_fluctuation)



# 读取公司订单数据和公司财报数据
order_data = pd.read_csv('D:/sj/公司订单数据.csv')
financial_data = pd.read_csv('D:/sj/企业财报.csv', encoding='gbk')

# 将订单日期列转换为日期时间类型
order_data['订单日期'] = pd.to_datetime(order_data['订单日期'])
# 将财报日期列转换为日期时间类型
financial_data['日期'] = pd.to_datetime(financial_data['日期'])

# 按照日期合并订单和财报数据
merged_data = pd.merge(order_data, financial_data, left_on='订单日期', right_on='日期', how='inner')

# 计算每月的净收入（收入减支出）
merged_data['净收入'] = merged_data['收入'] - merged_data['支出']

# 按日期分组，并计算每月的净收入
monthly_net_income = merged_data.groupby(merged_data['订单日期'].dt.to_period('M'))['净收入'].sum()

# 绘制行业内部效益输出曲线
plt.figure(figsize=(10, 6))
plt.plot(monthly_net_income.index.to_timestamp(), monthly_net_income.values, marker='o', color='b')
plt.xlabel('日期')
plt.ylabel('净收入')
plt.title('企业净收入产出曲线')
plt.grid(True)

image_path_3 = 'image'
if not os.path.exists(image_path_3):
    os.makedirs(image_path_3)
plt.savefig(os.path.join(image_path_3, 'nihe2.png'))
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt  

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签 

# 读取数据集
data = pd.read_csv('D:/sj/employee.csv', encoding='gbk')

# 将类别特征转换为数值特征
data['是否离职'] = data['是否离职'].map({'是': 1, '否': 0})
data['性别'] = data['性别'].map({'男': 0, '女': 1})

# 使用独热编码转换分类变量
data = pd.get_dummies(data, columns=['学历', '职位等级'])

# 分割特征和标签
X = data.drop(['是否离职', '离职时间', '入职时间'], axis=1)
y = data['是否离职']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建逻辑回归模型
model = LogisticRegression()

# 训练模型
model.fit(X_train, y_train)

# 在测试集上做预测
probabilities = model.predict_proba(X_test)[:, 1]  # 获取离职的概率

# 绘制密度图
sns.histplot(probabilities, kde=True)
plt.xlabel('离职概率')
plt.ylabel('频数')
plt.title('员工离职概率分布')

image_path_4 = 'image'
if not os.path.exists(image_path_4):
    os.makedirs(image_path_4)
plt.savefig(os.path.join(image_path_4, '3a.png'))

plt.show()

# 获取特征对应的系数
coefficients = model.coef_[0]

# 获取特征名称
feature_names = X.columns

# 将特征名称和系数对应起来，并按绝对值大小排序
feature_coefficients = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})
feature_coefficients['Absolute Coefficient'] = abs(feature_coefficients['Coefficient'])
feature_coefficients = feature_coefficients.sort_values(by='Absolute Coefficient', ascending=False)

# 输出前几个对离职概率影响最大的特征
print("Top features affecting turnover probability:")
print(feature_coefficients.head(10))


# 从CSV文件中加载财务数据
df = pd.read_csv('D:/sj/行业财务数据.csv', encoding='gbk')


# 计算行业整体平均利润
industry_avg_profit = df['月利润'].mean()

# 将纵坐标单位改为万
df['月利润（万）'] = df['月利润'] / 10000

# 绘制行业内部效益输出曲线
plt.figure(figsize=(10, 6))
plt.plot(df['公司名称'], df['月利润（万）'], marker='o', label='月公司利润（万）')
plt.axhline(industry_avg_profit/10000, color='red', linestyle='--', label='行业平均月利润（万）：{}'.format(abs(industry_avg_profit/10000)))
plt.xlabel('公司')
plt.ylabel('月利润（万）')
plt.title('行业内部效益输出曲线')
plt.xticks(rotation=45)
plt.legend()

# 自定义纵坐标标签的格式，确保负数前显示负号
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in plt.gca().get_yticks()])

plt.grid(True)
plt.tight_layout()

image_path_5 = 'image'
if not os.path.exists(image_path_5):
    os.makedirs(image_path_5)
plt.savefig(os.path.join(image_path_5, 'nihe1.png'))

plt.show()
plt.show()