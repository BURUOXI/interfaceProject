# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 12:34
# @Author  : felix
# @Email   : 876569085@qq.com
# @File    : handlerequest.py
# @Software: PyCharm
import requests


class SendRequest(object):
    """cookie+session鉴权的请求类封装"""

    def __init__(self):
        self.session = requests.session()

    def send(self, url, method, headers=None, params=None, data=None, json=None, files=None):
        method = method.lower()
        if method == "get":
            response = self.session.get(url=url, params=params, headers=headers)
        elif method == "post":
            response = self.session.post(url=url, json=json, data=data, files=files, headers=headers)
        elif method == "patch":
            response = self.session.patch(url=url, json=json, data=data, files=files, headers=headers)

        return response
