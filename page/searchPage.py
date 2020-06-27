# 搜索页面类(调用元素定位页面获取信息来去base操作页面进行操作)

from Base.base import Base
from page.pageElements import PageElements


class SearchPage(Base):

    def __init__(self):
        super().__init__()    # 使用继承Base,然后重写父类初始化




    def search_test(self, text):
        # 搜索内容的方法，text搜索内容由013测试页传入过来
        self.send_ele(PageElements.search_input_id, text)

    def get_search_result(self):
        # 获取搜索结果方法
        # 定位搜索结果并返回搜索结果的文本
        results = self.search_eles(PageElements.search_result_ids)
        return [i.text for i in results]
