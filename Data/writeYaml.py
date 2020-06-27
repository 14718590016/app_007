# 写入数据到yaml文件中  yaml.safe_dump((data,stream,encoding,allow_unicode))
# data: 要传输进去的文件数据   stream：打开待写⼊⽂件对象,
# encoding='utf-8'	#	设置写⼊编码格式    allow_unicode=True	#	是否允许unicode编码

import yaml

data = {'Search_Data': {'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
                        'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

# 在Data目录下新建abc.yml文件，并写入data字典数据
# 打开文件并进行a追加操作
with open("./abc.yml", 'a', encoding="utf-8") as f:
    # yaml写入数据
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)
