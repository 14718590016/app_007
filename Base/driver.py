# app驱动对象，供其他文件调用
from appium import webdriver


class Driver:
    # 声明web或者app的驱动对象
    # 定义要测app的驱动对象
    app_driver = None

    @classmethod   # 类方法，不需要实例化类Driver()来进行调用，可以直接Driver.函数
    def get_app_driver(cls):
        """声明手机驱动对象, 以供调用"""
        if not cls.app_driver:    # 防止每次调用都打开一次app，加判断条件，为空时声明驱动对象
            # server 启动参数
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }

            # 声明我们的driver对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            # 返回驱动对象
            return cls.app_driver
        else:   #  app_driver已经声明过了，返回已打开的驱动对象
            return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出手机驱动对象"""
        if cls.app_driver:    # 有值
            cls.app_driver.quit()

            # 重新将app_driver置为None
            cls.app_driver = None