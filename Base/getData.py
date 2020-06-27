# 封装打开加载yaml数据的方法
import os

import yaml

class GetData:
    # 读取测试数据的方法
    @classmethod
    def get_yaml_data(cls, name):
        # 读取yaml数据
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
        # yaml读取文件
            return yaml.safe_load(f)