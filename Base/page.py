# 设置的统一入口-页面类(实例化设置及其下级选项以供调用)
from page.searchPage import SearchPage
from page.settingPage import SettingPage
from page.xianshiPage import XianShiPage


class Page:
    """返回所有页面实例化对象"""
    @classmethod     # 设置类方法，调用时直接Page.get_settingPage,不用a = Page(), a.get_settingPage
    def get_settingPage(cls):
        """返回设置页面类实例化对象"""
        return SettingPage()

    @classmethod
    def get_xianshiPage(cls):
        """返回显示页面类实例化对象"""
        return XianShiPage()

    @classmethod
    def get_sousuoPage(cls):
        """返回搜索页面类实例化对象"""
        return SearchPage()