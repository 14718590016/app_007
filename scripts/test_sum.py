# 计算判断两数和,通过调用封装的数据驱动的方式,与sum,yaml配合

import pytest

from Base.getData import GetData


def sum_data():
    liebiao = []
    # with open("./Data/sum.yaml", "r", encoding="utf-8") as f:
    #     # 使用yaml加载数据
    #     data = yaml.safe_load(f)  # 返回字典
    data = GetData.get_yaml_data("sum.yaml")     # 通过调用封装的打开加载yaml数据的方法
    for i in data.values():  # 遍历字典并取所有values值
        print("i: ", i)
        liebiao.append((i.get("a"), i.get("b"), i.get("c")))
    print(liebiao)
    return liebiao


class TestSum:
    # @pytest.mark.parametrize("a,b,c", [(1, 2, 3), (3, 4, 5), (4, 5, 9)])
    @pytest.mark.parametrize("a,b,c", sum_data())
    def test_sum(self, a, b, c):
        # 判断两数和等于第三数
        print("\n{}+{}={}".format(a, b, c))
        assert a + b == c
