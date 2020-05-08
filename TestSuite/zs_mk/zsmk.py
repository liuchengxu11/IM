import allure
import pytest
import pymysql
from Config.Config import sx_zs_api,SX_PC_IM_headers
import json
from Utils.common import Common


class Test_case():
    @allure.epic("招商模块分析")
    @allure.feature("招商数据概括接口")
    @pytest.mark.parametrize("isCumulative,signBrandCode,unit,case",aaa)
    def mk_merchantsStatistics_merchantsContractStatics(self,isCumulative,signBrandCode,unit,case):
        """
        招商数据概括接口
        :return:
        """
        uri="/api/v1/merchantsStatistics/merchantsContractStatics"
        allure.attach(
            sx_zs_api +
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
            "isCumulative": isCumulative, # 布尔  必须  是否累计
            "signBrandCode": signBrandCode,  # string 非必须  品牌code
            "unit": unit,  # number 必须  单位 (0,上周,1本周,2上个月,本月)

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
                "---------/api/v1/merchantsStatistics/merchantsContractStatics接口调用成功")
        else:
            print(
                "---------/api/v1/merchantsStatistics/merchantsContractStatics接口调用失败")


    @allure.epic("招商模块分析")
    @allure.feature("招商人数")
    @pytest.mark.parametrize("unit,case", aaa)
    def mk_merchantsStatistics_merchantsEfficiency(self, unit, case):
        """
        招商人数
        :return:
        """
        uri = "/api/v1/merchantsStatistics/merchantsEfficiency"
        allure.attach(
            sx_zs_api +
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
            "unit": unit,  # number 必须  单位 (0,上周,1本周,2上个月,本月)
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
                "---------/api/v1/merchantsStatistics/merchantsEfficiency接口调用成功")
        else:
            print(
                "---------/api/v1/merchantsStatistics/merchantsEfficiency接口调用失败")

    @allure.epic("招商模块分析")
    @allure.feature("招商人数")
    @pytest.mark.parametrize("unit,signBrandCode,signBrandCodeName,case", aaa)
    def mk_merchantsStatistics_merchantsContractRatio(self, unit,signBrandCode,signBrandCodeName,case):
        """
        招商人数
        :return:
        """
        uri = "/api/v1/merchantsStatistics/merchantsContractRatio"
        allure.attach(
            sx_zs_api +
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
            "unit": unit,  # number 必须  单位 (0,上周,1本周,2上个月,本月)
            "signBrandCode": signBrandCode, # string  非必须  品牌code
            "signBrandCodeName": signBrandCodeName, # string 非必须  品牌名称
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
                "---------/api/v1/merchantsStatistics/merchantsContractRatio接口调用成功")
        else:
            print(
                "---------/api/v1/merchantsStatistics/merchantsContractRatio接口调用失败")




