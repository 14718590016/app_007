# 读取yaml文件数据，返回的是字典
# yaml.safe_load(f)  需先打开文件并赋值对象给f

import yaml

with open("./data2.yml", "r", encoding="utf-8") as f:
    # 使用yaml加载数据
    data = yaml.safe_load(f)    # 返回字典
    print("返回字典数据： ", data)
    print("返回的数据类型： ", type(data.get("address")))