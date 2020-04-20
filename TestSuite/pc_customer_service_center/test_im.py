import pytest
import allure
from Utils.common import Common
from Config.Config import SX_PC_kf_IM_API, SX_PC_IM_headers,SX_PC_kf_API
import json
from Config.excel_config.sheet_excel import Sheet

"""
客服中心-即时通讯系列的相关接口
"""
init = Sheet().kf_sheet(row_id=2, column_id=3)
init_disconnect = Sheet().kf_sheet(row_id=3, column_id=3)
updateCustomerServiceStatus = Sheet().kf_sheet(row_id=4, column_id=3)
dingding_sendMessage=Sheet().kf_sheet(row_id=5, column_id=3)


class Test_case():
    # @allure.epic("即时通讯")
    # @allure.feature("初始化登陆")
    # @pytest.mark.parametrize(
    #     "accountName,name,userType,phone,email,loginType,case", init)
    # def test_im_init(
    #         self,
    #         accountName,
    #         name,
    #         userType,
    #         phone,
    #         email,
    #         loginType,
    #         case):
    #     """
    #     初始化登陆接口
    #     :return:
    #     """
    #     uri = "/sunxing-customer-service/api/v1/im/init"
    #     allure.attach(SX_PC_kf_API + uri,
    #         "地址",
    #         allure.attachment_type.TEXT)
    #     headers = SX_PC_IM_headers
    #     allure.attach(
    #         json.dumps(
    #             headers,
    #             ensure_ascii=False,
    #             indent=4),
    #         "请求头",
    #         allure.attachment_type.TEXT)
    #     common = Common()
    #     data = {
    #         "accountName": accountName,  # 登录账号  必传
    #         "name": name,  # 用户昵称  必传
    #         "userType": userType,  # 用户身份 0 客服 1 客户  必传
    #         "phone": phone,  # 联系方式
    #         "email": email,  # 邮箱
    #         "loginType": loginType   # 登录类型 传值 web app
    #     }
    #     allure.attach(
    #         json.dumps(
    #             data,
    #             ensure_ascii=False,
    #             indent=4),
    #         "body",
    #         allure.attachment_type.TEXT)
    #     response = common.post(uri, data=data, headers=headers)
    #     allure.attach(json.dumps(response.json(), ensure_ascii=False,
    #                              indent=4), "响应", allure.attachment_type.TEXT)
    #     code = int(response.status_code)
    #     code1 = json.loads(response.text)["code"]
    #
    #     if code == 200 and str(code1 == 200):
    #         print("---------/sunxing-customer-service/api/v1/im/init接口调用成功")
    #     else:
    #         print("---------/sunxing-customer-service/api/v1/im/init接口调用失败")
    #
    # @allure.epic("即时通讯")
    # @allure.feature("结束会话")
    # @pytest.mark.parametrize("fromAccount,to,userType,case", init_disconnect)
    # def test_im_init_disconnect(self, fromAccount,to, userType, case):
    #     """
    #     结束会话
    #     :return:
    #     """
    #     uri = "/sunxing-customer-service/api/v1/im/disconnect"
    #     allure.attach(
    #         SX_PC_kf_API +
    #         uri,
    #         "地址",
    #         allure.attachment_type.TEXT)
    #     headers = SX_PC_IM_headers
    #     allure.attach(
    #         json.dumps(
    #             headers,
    #             ensure_ascii=False,
    #             indent=4),
    #         "请求头",
    #         allure.attachment_type.TEXT)
    #     common = Common()
    #     data = {
    #         "fromAccount": fromAccount,  # 发送者账户
    #         "to": to,  # 接收者账户
    #         "userType": userType,  # 结束会话用户类型 0 客服 1 客户
    #     }
    #     allure.attach(
    #         json.dumps(
    #             data,
    #             ensure_ascii=False,
    #             indent=4),
    #         "body",
    #         allure.attachment_type.TEXT)
    #     response = common.post(uri, data=data, headers=headers)
    #     allure.attach(json.dumps(response.json(), ensure_ascii=False,
    #                              indent=4), "响应", allure.attachment_type.TEXT)
    #     code = int(response.status_code)
    #     code1 = json.loads(response.text)["code"]
    #
    #     if code == 200 and str(code1 == 200):
    #         print("---------/sunxing-customer-service/api/v1/im/disconnect接口调用成功")
    #     else:
    #         print("---------/sunxing-customer-service/api/v1/im/disconnect接口调用失败")
    #
    # @allure.epic("即时通讯")
    # @allure.feature("更新客服状态")
    # @pytest.mark.parametrize("account,status,case", updateCustomerServiceStatus)
    # def test_im_updateCustomerServiceStatus(self, account, status, case):
    #     """
    #     更新客服状态
    #     :return:
    #     """
    #     uri = "/sunxing-customer-service/api/v1/im/updateCustomerServiceStatus"
    #     allure.attach(
    #         SX_PC_kf_API +
    #         uri,
    #         "地址",
    #         allure.attachment_type.TEXT)
    #     headers = SX_PC_IM_headers
    #     allure.attach(
    #         json.dumps(
    #             headers,
    #             ensure_ascii=False,
    #             indent=4),
    #         "请求头",
    #         allure.attachment_type.TEXT)
    #     common = Common()
    #     data = {
    #         "account": account,  # 客服账号
    #         "status": status,  # 客服状态 0 在线 1 离线 2 忙碌
    #     }
    #     allure.attach(
    #         json.dumps(
    #             data,
    #             ensure_ascii=False,
    #             indent=4),
    #         "body",
    #         allure.attachment_type.TEXT)
    #     response = common.post(uri, data=data, headers=headers)
    #     allure.attach(json.dumps(response.json(), ensure_ascii=False,
    #                              indent=4), "响应", allure.attachment_type.TEXT)
    #     code = int(response.status_code)
    #     code1 = json.loads(response.text)["code"]
    #
    #     if code == 200 and str(code1 == 200):
    #         print(
    #             "---------/sunxing-customer-service/api/v1/im/updateCustomerServiceStatus接口调用成功")
    #     else:
    #         print(
    #             "---------/sunxing-customer-service/api/v1/im/updateCustomerServiceStatus接口调用失败")

    @allure.epic("IM消息推送")
    @allure.feature("钉钉机器人群消息推送")
    @pytest.mark.parametrize("msgType,businessSystem,dingWebHookUrl,atMobiles,isAtAll,title,content,messageUrl,picUrl,case", dingding_sendMessage)
    def test_dingding_news_sendMessage(self,msgType,businessSystem,dingWebHookUrl,atMobiles,isAtAll,title,content,messageUrl,picUrl, case):
        """
        钉钉机器人群消息推送
        :return:
        """
        uri = "/api/dingding/news/sendMessage"
        allure.attach(
            SX_PC_kf_IM_API +
            uri,
            "地址",
            allure.attachment_type.TEXT)
        headers = SX_PC_IM_headers
        allure.attach(
            json.dumps(
                headers,
                ensure_ascii=False,
                indent=4),
            "请求头",
            allure.attachment_type.TEXT)
        common = Common()
        data = {
            "msgType":msgType,
            # 消息类型（1.text 消息类型为text类型 content 参数 businessSystem 参数 dingWebHookUrl 参数 必转
            #  ,2.link 消息类型为link类型 content 参数 title 参数 messageUrl 参数 businessSystem 参数 dingWebHookUrl 参数 必转, 3.markdown 消息类型为 markdown类型 content 参数 businessSystem 参数 dingWebHookUrl 参数 必转）
            "businessSystem": businessSystem,  # 业务系统-消息来自哪里（NY_PC:鲶鱼PC,  NY_APP:鲶鱼APP,DataGroup:数据组,FinanceGroup:财务组)
            "dingWebHookUrl": dingWebHookUrl,  # 机器人roup:数据组，FinanceGroup:财务组)
            "atMobiles": atMobiles,     # 被@人的手机号(在text内容里要有@手机号)
            "isAtAll": isAtAll,   # @所有人地址标识(DataG时：true，否则为：false
            "title": title,   # 标题
            "content": content,  # 消息内容
            "messageUrl":messageUrl, # 消息跳转的url
            "picUrl":picUrl, # 图片url
        }
        allure.attach(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=4),
            "body",
            allure.attachment_type.TEXT)
        response = common.post(uri, data=data, headers=headers)
        allure.attach(json.dumps(response.json(), ensure_ascii=False,
                                 indent=4), "响应", allure.attachment_type.TEXT)
        code = int(response.status_code)
        code1 = json.loads(response.text)["code"]

        if code == 200 and str(code1 == 200):
            print(
                "---------/api/dingding/news/sendMessage接口调用成功")
        else:
            print(
                "---------/api/dingding/news/sendMessage接口调用失败")
