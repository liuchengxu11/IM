from selenium.webdriver.common.by import By

from TestData.sunxing_ny_app.page.config_page import Config_page
from TestData.sunxing_ny_app.page.fudian_home import FuDian_Home

"""

点击工作台上的浮点  1线索  2任务
"""


class FuDian(Config_page):
    _xiansuo=(By.XPATH,"//*[@resource-id='android:id/content']/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]")
    _task=(By.XPATH,"//*[@resource-id='android:id/content']/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]")
    def xiansuo(self):
        self.find_element_and_click(self._xiansuo)
        return FuDian_Home(self.driver)



    def task(self):
        self.find_element_and_click(self._task)
        return FuDian_Home(self.driver)