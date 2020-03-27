from selenium.webdriver.common.by import By

from TestData.sunxing_ny_app.page.config_page import Config_page
from TestData.sunxing_ny_app.page.fudian import FuDian

"""

鲶鱼 工作台页面
"""


class Work_Bench(Config_page):
    _fu_diian=(By.CLASS_NAME,"android.widget.Button")

    # 工作台
    def bench(self):
        pass



    # 看台
    def stand(self):
        pass



    # 我的
    def man(self):
        pass


    # 浮点
    def dian(self):
        self.find_element_and_click(self._fu_diian)
        return FuDian(self.driver)






