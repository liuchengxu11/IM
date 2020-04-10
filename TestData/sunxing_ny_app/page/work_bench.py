from selenium.webdriver.common.by import By

from TestData.sunxing_ny_app.page.Bench_Home import Bench_Home
from TestData.sunxing_ny_app.page.config_page import Config_page
from TestData.sunxing_ny_app.page.fudian import FuDian
from TestData.sunxing_ny_app.page.Contract_Singning_Home import Contract_Singning_Home

"""

鲶鱼 工作台页面
"""


class Work_Bench(Config_page):
    _fu_diian=(By.CLASS_NAME,"android.widget.Button")
    _bench=(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ImageView[1]")
    _contract_signing = (By.XPATH,"//*[@text='签约合同']")


    # 工作台
    def bench(self):

        self.find_element(self.bench).click()
        return Bench_Home(self.driver)



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

        # 签约合同
    def contract_signing(self):
        self.find_element_and_click(self._contract_signing)
        return Contract_Singning_Home(self.driver)






