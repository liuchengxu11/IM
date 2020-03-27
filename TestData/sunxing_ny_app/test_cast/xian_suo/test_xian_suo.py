
from TestData.sunxing_ny_app.page.app import App

"""

工作台首页——创建线索
"""


class Test_XianSuo:

    def setup(self):# 完成app的初始化并点击首页的浮点
        self.search_page=App.app().dian()

    def test_xiansuo_pj(self):# 点击线索并进行进入创建线索页面设置线索
        self.found=self.search_page.xiansuo()
        self.found.found_xiansuo()

    def teardown(self):
        App.quit()