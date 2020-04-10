from selenium.webdriver.common.by import By

from TestData.sunxing_ny_app.page.Contract_Singning_Home import Contract_Singning_Home
from TestData.sunxing_ny_app.page.config_page import Config_page
"""

工作台的附属页面：签约合同，回款，异常合同
"""


class Bench_Home(Config_page):
    _contract_signing=(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]")
    # 签约合同
    def contract_signing(self):
        self.find_element_and_click(self._contract_signing)
        return Contract_Singning_Home(self.driver)


