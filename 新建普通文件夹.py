import os
import sys
from datetime import datetime

# base_dir = os.getcwd()  # 获取当前工作目录
# print(f"当前工作目录: {base_dir}")
base_dir = os.path.dirname(sys.argv[0])

# 获取当前日期并转换为字符串格式
date_str = datetime.now().strftime('%Y%m%d')

# 创建文件夹的路径
folder_path = os.path.join(base_dir, date_str)

try:
    # 尝试创建文件夹
    os.mkdir(folder_path)
except FileExistsError:
    # 如果文件夹已经存在，捕获异常并不做任何操作
    pass
