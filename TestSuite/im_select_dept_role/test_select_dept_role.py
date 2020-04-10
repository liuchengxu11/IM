import pytest
import allure
from Config.Config import SX_IM_API, Login_Headers, DingDing_deptId, DingDing_roleId, DingDing_userid, DingDing_deptName,IM_json
from Utils.common import Common
import json
from Utils.db_tool.rides_db import Db_redis
from Config.excel_config.sheet_excel import Sheet



"""
查询部门，部门下用户，角色，角色下员工系列的接口

"""
ding_userid=Sheet().dingding_sheet(row_id=2,column_id=3)
ding_deptid=Sheet().dingding_sheet(row_id=3,column_id=3)
ding_roleid=Sheet().dingding_sheet(row_id=5,column_id=3)
ding_deptname=Sheet().dingding_sheet(row_id=10,column_id=3)
ding_IM=Sheet().dingding_sheet(row_id=13,column_id=3)
class Test_case():
    def setup_class(self):
        self.db = Db_redis()
    # @allure.epic("钉钉")
    # @allure.feature("获取部门列表")
    # def test_get_user_dingDingDept(self):
    #     """
    #     钉钉——获取部门列表
    #     :return:
    #     """
    #     uri = "/api/user/dingDingDept"
    #     allure.attach(SX_IM_API + uri, "地址", allure.attachment_type.TEXT)
    #     headers = Login_Headers
    #     allure.attach(json.dumps(
    #         headers,
    #         ensure_ascii=False,
    #         indent=4),
    #         '请求头', allure.attachment_type.TEXT)
    #     common = Common()
    #     response = common.get(uri, headers=headers)
    #     allure.attach(json.dumps(
    #         response.json(),
    #         ensure_ascii=False,
    #         indent=4), "响应", allure.attachment_type.TEXT)
    #     print(response.text)
    #     code = int(response.status_code)
    #     code1 = json.loads(response.text)["code"]
    #     code2 = json.loads(response.text)["desc"]
    #     if code == 200 and code1 == 0 and code2 == "ok":
    #         print("——————————/api/user/dingDingDept调用成功")
    #     else:
    #         print("——————————/api/user/dingDingDept调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取用户详情")
    @pytest.mark.parametrize("test1,test2,case", ding_userid)
    def test_get_user_dingDingUser(self, test1, test2, case):
        """
        钉钉——获取用户详情
        :return:
        """
        print(test1)
        print(test2)
        print(case)
        uri = "/api/user/dingDingUser"
        allure.attach(
            SX_IM_API +
            uri,
            "地址",
            allure.attachment_type.TEXT)
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
        code1 = int(json.loads(response.text)["code"])
        code2 = json.loads(response.text)["desc"]
        assert case == json.loads(response.text)["data"]['userName']

        # assert case==code3

        if code == 200 and code1 == 200 and code2 == "ok":
            print("---------/api/user/dingDingUser接口调用成功")
        else:
            print("---------/api/user/dingDingUser接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取部门详情")
    @pytest.mark.parametrize("test1,test2",ding_deptid)
    def test_get_user_dingDingDeptDetail(self, test1, test2):
        """
        钉钉-获取部门详情
        """
        uri = "/api/user/dingDingDeptDetail"
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
        code2 = json.loads(response.text)["desc"]
        if code == 200 and code1 == 0 and code2 == "ok":
            print("---------/api/user/dingDingDeptDetail接口调用成功")
        else:
            print("---------/api/user/dingDingDeptDetail接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取部门下用户列表")
    @pytest.mark.parametrize("test1,test2", ding_deptid)
    def test_get_user_dindDingDeptMember(self, test1, test2):
        """
        钉钉-获取部门下用户列表
        """
        uri = "/api/user/dingDingDeptMember"
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
        code2 = json.loads(response.text)["desc"]
        if code == 200 and code1 == 0 and code2 == "ok":
            print("---------/api/user/dingDingDeptMember接口调用成功")
        else:
            print("---------/api/user/dingDingDeptMember接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取角色下员工列表")
    @pytest.mark.parametrize("test1,test2", ding_roleid)
    def test_post_user_dingDingRoleStaffList(self, test1, test2):
        """
        钉钉-获取角色下员工列表
        """
        uri = "/api/user/dingDingRoleStaffList"
        allure.attach(SX_IM_API + uri, "地址", allure.attachment_type.TEXT)
        headers = Login_Headers
        allure.attach(json.dumps(
            headers,
            ensure_ascii=False,
            indent=4), "请求头", allure.attachment_type.TEXT)
        data={}
        common = Common()
        response = common.post(
            uri,
            data=data,
            params1=test1,
            params2=test2,
            headers=headers)
        allure.attach(json.dumps(response.json(), ensure_ascii=False,
                                 indent=4), "响应", allure.attachment_type.TEXT)
        code = int(response.status_code)
        code1 = json.loads(response.text)["code"]

        if code == 200 and code1 == 200:
            print("---------/api/user/dingDingRoleStaffList接口调用成功")
        else:
            print("---------/api/user/dingDingRoleStaffList接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取角色详情")
    @pytest.mark.parametrize("test1,test2", ding_roleid)
    def test_post_user_dingDingRoleDetail(self, test1, test2):
        """
        钉钉-获取角色详情
        """
        uri = "/api/user/dingDingRoleDetail"
        allure.attach(SX_IM_API + uri, "地址", allure.attachment_type.TEXT)
        headers = Login_Headers
        allure.attach(json.dumps(
            headers,
            ensure_ascii=False,
            indent=4), "请求头", allure.attachment_type.TEXT)
        data={}
        common = Common()
        response = common.post(
            uri,
            data=data,
            params1=test1,
            params2=test2,
            headers=headers)
        allure.attach(json.dumps(response.json(), ensure_ascii=False,
                                 indent=4), "响应", allure.attachment_type.TEXT)
        code = int(response.status_code)
        code1 = json.loads(response.text)["code"]

        if code == 200 and code1 == 0:
            print("---------/api/user/dingDingRoleDetail接口调用成功")
        else:
            print("---------/api/user/dingDingRoleDetail接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取角色列表")

    def test_post_user_dingDingRoleList(self):
        """
        钉钉-获取角色列表
        """
        uri = "/api/user/dingDingRoleList"
        allure.attach(SX_IM_API + uri, "地址", allure.attachment_type.TEXT)
        headers = Login_Headers
        allure.attach(json.dumps(
            headers,
            ensure_ascii=False,
            indent=4), "请求头", allure.attachment_type.TEXT)
        data={}
        common = Common()
        response = common.post(
            uri,
            data=data,
            headers=headers)
        allure.attach(json.dumps(response.json(), ensure_ascii=False,
                                 indent=4), "响应", allure.attachment_type.TEXT)
        code = int(response.status_code)
        code1 = json.loads(response.text)["code"]

        if code == 200 and code1 == 0:
            print("---------/api/user/dingDingRoleList接口调用成功")
        else:
            print("---------/api/user/dingDingRoleList接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取用户上级详情")
    @pytest.mark.parametrize("test1,test2,case", ding_userid)
    def test_get_user_dindDingGetUserLeader(self, test1, test2, case):
        """
        钉钉-获取用户上级详情
        """
        uri = "/api/user/dingDingGetUserLeader"
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
        if code == 200 and str(code1 == 0):
            print("---------/api/user/dingDingGetUserLeader接口调用成功")
        else:
            print("---------/api/user/dingDingGetUserLeader接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取当前用户下所有员工")
    @pytest.mark.parametrize("test1,test2,case", ding_userid)
    def test_get_user_dingDingUserList(self, test1, test2, case):
        """
        钉钉-获取当前用户下所有员工  做缓存
        """
        uri = "/api/user/dingDingUserList"
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

        if code == 200 and code1 == 200:
            print("---------/api/user//api/user/dingDingUserList接口调用成功")
        else:
            print("---------/api/user//api/user/dingDingUserList接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取部门下所有员工")
    @pytest.mark.parametrize("test1,test2", ding_deptname)
    def test_get_user_dingDingDeptUserList(self, test1, test2):
        """
        钉钉-获取部门下所有员工  做缓存
        """
        uri = "/api/user/dingDingDeptUserList"
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
        if code == 200 and str(code1 == 200):
            print("---------/api/user/dingDingDeptUserList接口调用成功")
        else:
            print("---------/api/user/dingDingDeptUserList接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取当前登录人部门列表")
    @pytest.mark.parametrize("test1,test2,case", ding_userid)
    def test_get_user_dingDingDeptList(self, test1, test2,case):
        """
        钉钉-获取当前登录人部门列表
        """
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

        if code == 200 and str(code1 == 200):
            print("---------/api/user/dingDingDeptList接口调用成功")
        else:
            print("---------/api/user/dingDingDeptList接口调用失败")

    @allure.epic("钉钉")
    @allure.feature("获取当前登录人树形菜单")
    @pytest.mark.parametrize("test1,test2,case", ding_userid)
    def test_get_user_dingDingUserTree(self, test1, test2, case):
        """
        钉钉-获取当前的登录人树形菜单  做缓存
        """
        uri = "/api/user/dingDingUserTree"
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



        if code == 200 and str(code1 == 200):
            print("---------/api/user/dingDingUserTree接口调用成功")
        else:
            print("---------/api/user/dingDingUserTree接口调用失败")

    # @allure.epic("IM消息中心")
    # @allure.feature("发送消息接口")
    # @pytest.mark.parametrize(
    #     "businessSystem,sendChannel,sendType,msgType,sendId,content,deptId,targetId,case",
    #     ding_IM)
    # def test_get_user_dingDingDeptUserList(
    #         self,
    #         businessSystem,
    #         sendChannel,
    #         sendType,
    #         msgType,
    #         sendId,
    #         content,
    #         deptId,
    #         targetId,
    #         case
    #         ):
    #     """
    #     IM消息中心-发送消息接口
    #     """
    #     uri = "/api/message/sendMessage"
    #     allure.attach(SX_IM_API + uri, "地址", allure.attachment_type.TEXT)
    #     headers = Login_Headers
    #     allure.attach(json.dumps(
    #         headers,
    #         ensure_ascii=False,
    #         indent=4), "请求头", allure.attachment_type.TEXT)
    #     data = {'businessSystem': businessSystem,  # 业务系统-消息来自哪里（鲶鱼PC：1 鲶鱼APP： 2)
    #             # 发送到的渠道（钉钉:1 鲶鱼PC:2 鲶鱼APP: 3 ），多个发送渠道用逗号隔开例如（1,2,3），暂时仅有钉钉
    #             'sendChannel': sendChannel,
    #             'sendType': sendType,  # 发送类型（1·工作通知 2·群消息 3·邮件 ），暂时仅支持发送工作通知
    #             'msgType': msgType,  # 消息类型（1·文本）
    #             'sendId': sendId,  # 发送人id（userid）
    #             'content': content,  # 发送内容
    #             'deptId': deptId,  # 要发送的部门id，如果是发送到指定人员，部门ID不需要填写
    #             'targetId': targetId,
    #             }  # 接收人id（userid），如果是发送到指定部门接收人ID不需要填写，如果有多个接收人，用逗号隔开例如（1231313，museri1212）
    #     common = Common()
    #     allure.attach(json.dumps(
    #         data,
    #         ensure_ascii=False,
    #         indent=4), "body", allure.attachment_type.TEXT)
    #     response = common.post(
    #         uri,
    #         data=data,
    #         headers=headers)
    #     allure.attach(json.dumps(response.json(), ensure_ascii=False,
    #                              indent=4), "响应", allure.attachment_type.TEXT)
    #     code = int(response.status_code)
    #     code1 = json.loads(response.text)["code"]
    #
    #     if code == 200 and str(code1 == 200):
    #         print("---------/api/message/sendMessage接口调用成功")
    #     else:
    #         print("---------//api/message/sendMessage接口调用失败")
