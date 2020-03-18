import requests
import json
from Config.Config import SX_IM_API


class Common(object):

    def __init__(self):
        self.url = SX_IM_API

    def get(self, uri, params1="", params2="", headers=""):
        if params2 is not None:
            url = self.url + uri + "?" + str(params1) + str(params2)
            print(url)
            if params2 is None:
                url = self.url + uri + "?" + str(params1)
                print(url)
        else:
            url = self.url + uri
        res = requests.get(url, headers=headers)
        return res

    def post(self, uri, params1="", params2="", data="", headers=""):
        if params2 is not None:
            url = self.url + uri + "?" + str(params1) + str(params2)
            print(url)
            if params2 is None:
                url = self.url + uri + "?" + str(params1)
                print(url)
        else:
            url = self.url + uri
        if len(data) > 0:
            res = requests.post(url, data=json.dumps(data), headers=headers)
        else:
            res = requests.post(url, headers=headers)
        return res
