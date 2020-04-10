
import pytest
import allure
from Utils.db_tool.rides_db import Db_redis
from Config.Config import SX_IM_API,Login_Headers
import json
from Utils.common import Common

"""
针对钉钉组织架构接口对返回的数据进行mongo和redis数据验证核实是否落库
"""

class TestClass():
    def setup_class(self):
        self.db = Db_redis()

    userid = [("userId=","102013620721191002")]
    @allure.epic("钉钉")
    @allure.feature("获取当前登录人部门列表_缓存验证")
    @pytest.mark.parametrize("test1,test2",userid)
    def test_dingDingDeptList(self,test1,test2):
        self.db.get(test2)
        uri = "/api/user/dingDingDeptList"
        allure.attach(SX_IM_API + uri, "地址", allure.attachment_type.TEXT)
        headers = Login_Headers
        allure.attach(json.dumps(
            headers,
            ensure_ascii=False,
            indent=4), "请求头", allure.attachment_type.TEXT)
        common = Common()
        response = common.get(
            uri,
            params1=test1,
            params2=test2,
            headers=headers)
        allure.attach(json.dumps(response.json(), ensure_ascii=False,
                                 indent=4), "响应", allure.attachment_type.TEXT)
        code = int(response.status_code)
        code1 = json.loads(response.text)["code"]
        deftid=json.loads(response.text)["data"][0]["deptId"]
        print(code1)
        print(deftid)
        print(self.db.get(test2))
        # assert self.db.get(test2)== deftid
        if code == 200 and str(code1 == 0):
            print("---------/api/user/dingDingGetUserLeader接口调用成功")
        else:
            print("---------/api/user/dingDingGetUserLeader接口调用失败")







