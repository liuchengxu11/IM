import pytest
import allure
from Config.Config import SX_PC_kf_API,Login_Headers
import json
from Utils.common import Common



"""
客服中心 公共分类相关接口
"""


class Test_case():
    @allure.epic("客服中心公共分类相关")
    @allure.feature("app在线客服主页回复")
    def test_pc_getHeplProblem(self):
        """
        app在线客服主页回复
        :return:
        """
        uri = "/getHeplProblem"
        allure.attach(SX_PC_kf_API + uri + "地址" + allure.attachment_type.TEXT)
        headers=Login_Headers
        allure.attach(json.dumps(
            headers,
            ensure_ascii=False,
            indent=4),
            '请求头', allure.attachment_type.TEXT)
        common = Common()
        response = common.get(uri, headers=headers)
        allure.attach(json.dumps(
            response.json(),
            ensure_ascii=False,
            indent=4), "响应", allure.attachment_type.TEXT)
        print(response.text)
        code = int(response.status_code)
        code1 = json.loads(response.text)["code"]
        code2 = json.loads(response.text)["desc"]
        if code == 200 and code1 == 0 and code2 == "ok":
            print("——————————/api/user/dingDingDept调用成功")
        else:
            print("——————————/api/user/dingDingDept调用失败")








