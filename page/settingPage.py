# 这是设置类的操作页面(调用元素定位页面获取信息来去base操作页面进行操作)
from Base.base import Base
from page.pageElements import PageElements


class SettingPage(Base):

    def __init__(self):
        super().__init__()

    def click_xianshi_btn(self):
        # 点击显示按钮
        self.click_ele(PageElements.setting_xianshi_btn_xpath)

    def click_sousuo_btn(self):
        # 点击搜索按钮
        self.click_ele(PageElements.search_btn_id)
