from selenium.webdriver.common.by import By

from TestData.sunxing_ny_app.page.config_page import Config_page
import time
"""
点击浮点后的创建线索和创建工单
"""

class FuDian_Home(Config_page):
    # 联系人
    _name=(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
    # 联系电话
    _iphone=(By.XPATH,"//*[@resource-id='android:id/content']/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.EditText[2]")
    # 店铺名称
    _store_name=(By.XPATH,"//*[@text='店铺名称 请输入店铺名称']")
    # 店铺区域
    _store_region=(By.XPATH,"//*[@text='店铺区域 请选择店铺区域']")
    # 店铺地址
    _store_address=(By.XPATH,"//*[@text='店铺地址 请输入店铺地址']")
    # 客户来源
    _store_source=(By.XPATH,"//*[@text='客户来源 请选择客户来源']")
    # 下啦菜单的确定
    _yes=(By.XPATH,"//*[@text='确定']")
    # 下拉菜单的取消
    _no=(By.XPATH,"//*[@text='取消']")

    def found_xiansuo(self):
        self.find_element_and_sendkeys(self._name,sendkeys="光头强")
        time.sleep(3)
        self.find_element_and_sendkeys(self._iphone,"15000000000")
        self.find_element_and_sendkeys(self._store_name,"熊大熊二烧烤")
        # 点击店铺区域  并选择区域
        self.find_element_and_click(self._store_region)
        self.find_element_and_click(self._yes)
        # 点击店铺地址  进入高德
        # self.find_element(self._store_address).click()
        # 客户来源
        self.find_element_and_click(self._store_source)
        self.find_element_and_click(self._yes)







    def found_task(self):
        time.sleep(3)


