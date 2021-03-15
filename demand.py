# -- coding: utf-8 --
import json
import requests
import jsonpath

from interfaceProject.common.handleconfig import conf
from interfaceProject.common.handlerandom import random_pyint


class Getlist:


    def login(self):
        url = conf.get("URL", "urls") + "/api/auth/login"
        headers = {"content-type": "application/json; charset=utf-8", "x-client": "bc", "client": "backend",
                   "guard": "api", "x-client-version": "3.22"}
        body = {"account": "13385289600",
                "password": "123456Aa",
                "auto_login": "true"
                }
        res = requests.post(url=url, headers=headers, params=body).text
        re = json.loads(res)
        result = jsonpath.jsonpath(re, "$...access_token")
        token_li = result[0]
        token = "Bearer " + token_li
        return token

    def get_demandList(self):
        """ 需求发布"""
        token = Getlist.login(self)
        # 获取url
        url = conf.get("URL", "url") + "/api/prs/demands/store"
        # 请求头
        headers = {"content-type": "application/json; charset=utf-8", "x-client": "bc", "client": "backend", "guard": "api"}
        # 请求头加入token
        headers["Authorization"] = token
        # 读取config存的数据
        datas = conf.get("multiTender", "data")  # 改这里的等一个字段
        name = "测试-发布需求{}".format(random_pyint())



        data = json.loads(datas)  # json类型转换为字符串类型
        data["name"] = name
        print(data)
        # 发起请求
        res = requests.post(url=url, headers=headers, json=data).text
        # 解析返回值
        re = json.loads(res)
        self.demand_id = jsonpath.jsonpath(re, "$..demand_id")
        # print(re)
        print("需求发布成功，需求id{}".format(self.demand_id))
        whether_publish = int(input("收发布至场推：1：是        2：否   :"))
        if whether_publish == 1:
            A.demands_publish()
            print("发布成功")
        else:
            print("不发布到场推")
        return self.demand_id

    def demands_publish(self):        # 发布到场推

        token = A.login()       # 传入token
        url = conf.get("URL", "url") + "/api/prs/demands/publish"
        headers = {"content-type": "application/json; charset=utf-8", "x-client": "bc", "client": "backend","guard": "api"}
        # 请求头加入token
        headers["Authorization"] = token
        id = self.demand_id[0]
        data = {"id": id}
        # 发起请求
        res = requests.post(url=url, headers=headers, json=data).text
        # 解析返回值
        re = json.loads(res)
        print(re)


A = Getlist()
A.get_demandList()




