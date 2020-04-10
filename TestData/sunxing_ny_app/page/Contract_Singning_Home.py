from selenium.webdriver.common.by import By
import time
from TestData.sunxing_ny_app.page.config_page import Config_page
"""
合同签约页面
"""

class Contract_Singning_Home(Config_page):

    _element1=(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView")
    def contract_singning_home(self):
        self.find_element_and_sendkeys(self._element1,sendkeys="刘程旭好帅")
        time.sleep(3)

