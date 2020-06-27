# 设置里搜索页面的测试文件
import pytest

from Base.driver import Driver
from Base.page import Page


class Test_Search:


    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()

    # # 因为只需要运行一次 并且是依赖方法，所以使用fixture工厂函数
    # @pytest.fixture(scope="class", autouse=True)
    # def click_search_btn(self):
    #     """点击搜索按钮 并且 点击一次"""
    #     self.base_obj.click_ele(self.search_btn_id)

    @pytest.mark.parametrize("search_data, exp_data", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search_text(self, search_data, exp_data):
        """
        搜索测试方法
        :param search_data: 输入内容
        :param exp_data: 预期结果
        :return:
        """
        # 点击搜索按钮
        Page.get_settingPage().click_sousuo_btn()
        # 输入框输入内容
        # self.base_obj.send_ele(self.search_input_id, search_data)
        Page.get_sousuoPage().search_test(search_data)
        # 获取结果
        # results = self.base_obj.search_eles(self.search_result_ids)
        sousuojg = Page.get_sousuoPage().get_search_result()
        # 断言
        assert exp_data in sousuojg
