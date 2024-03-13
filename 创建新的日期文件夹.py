import os
from datetime import datetime

# 获取当前日期
now = datetime.now()

# 格式化日期为"年"、"年-月"和"年-月-日"格式
year_folder = now.strftime('%Y')
month_folder = now.strftime('%Y-%m')
day_folder = now.strftime('%Y-%m-%d')

# 拼接完整的路径（这里假设是在当前目录下创建）
year_path = os.path.join(os.getcwd(), year_folder)
month_path = os.path.join(year_path, month_folder)
day_path = os.path.join(month_path, day_folder)

# 分别检查并创建年、月、日文件夹
if not os.path.exists(year_path):
    os.makedirs(year_path)

if not os.path.exists(month_path):
    os.makedirs(month_path)

if not os.path.exists(day_path):
    os.makedirs(day_path)
