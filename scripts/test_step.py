# 可为测试报告添加步骤说明+生成附件内容和名字+定义bug严重级别
# @allure.step("一般描述该函数的步骤")   ---写在方法上，作⽤：	⽅便他⼈阅读测试业务执⾏顺序
# allure.attach('附件内容',	'附件名字')	   ---写在方法里面，作⽤：⽅便其他⼈阅读报告每个步骤中具体操作
# @allure.severity(allure.severity_level.严重级别) --写在方法上，方便优先修复严重级别bug
# 严重级别(BLOCKER,CRITICAL,NORMAL,MINOR,TRIVIAL)	逐级降低
import allure

class TestSerup:
    @allure.severity(allure.severity_level.BLOCKER)    # 阻断性bug
    @allure.step("测试登录第一步")
    def test_001(self):
        """添加测试步骤描述信息"""
        # 添加测试步骤描述
        allure.attach("账号是xxx", "登录测试点的内容")

    @allure.severity(allure.severity_level.CRITICAL)    # 比较重要bug
    def test_002(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)      # 正常bug
    def test_003(self):
        assert True

    @allure.severity(allure.severity_level.MINOR)  # 一般bug
    def test_004(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)  # 可忽略bug
    def test_005(self):
        assert True