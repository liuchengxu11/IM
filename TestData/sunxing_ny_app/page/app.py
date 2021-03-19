import os
import time

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from TestData.sunxing_ny_app.page.work_bench import Work_Bench

"""
查找app包的命令 adb shell dumpsys window windows | grep -E 'mCurrentFocus|FocusedApp'

adb shell dumpsys window w |grep \/ |grep name=

adb shell "dumpsys window w|grep \/|grep name=|sed 's/mSurface=Surface(name=//g'|sed 's/)//g'|sed 's/ //g'"

adb shell pm clear com.baidu.searchbox   包名  清理包的缓存数据  
"""


class App:
    driver :WebDriver =None

    @classmethod
    def app(cls):
        desired_caps = {}
        desired_caps["automationName"] = "UiAutomator2"
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['appPackage'] = 'com.tencent.mm'
        # desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['appPackage'] = 'com.sunxing.catfish'
        desired_caps['appActivity'] = 'com.sunxing.catfish.MainActivity'
        # appium提供的一种输入法，可以传中文。测试时直接用这个输入法
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"  # 程序结束时重置原来的输入法
        desired_caps["noReset"] = "True"  # 不初始化手机app信息（类似不清楚缓存）
        desired_caps['automationName'] = 'appium'
        desired_caps['deviceName'] = '12d63ed3'
        desired_caps['platformVersion'] = '9'
        desired_caps['autoGrantPermissions'] = 'True' # 这个是appium启动的时候处理各种权限弹窗  赋予全部权限
        udid = os.getenv("UDID", None)
        if udid != None:
            desired_caps["udid"] = udid
            print("udid={}".format(udid))
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # cls.driver = webdriver.Remote("http://192.168.100.165:4444/wd/hub", desired_caps)  # grid 的地址
        cls.driver.implicitly_wait(10)

        # 钉钉授权登录——确认登录
        cls.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.Button").click()
        time.sleep(2)

        # 授权app 点击授权
        cls.driver.find_element_by_xpath("//android.webkit.WebView/android.view.View[4]").click()
        time.sleep(2)
        return Work_Bench(cls.driver)   # 启动app之后页面进入 鲶鱼工作台页面


    @classmethod
    def quit(cls):
        cls.driver.quit()