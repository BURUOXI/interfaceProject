# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 12:34
# @Author  : felix
# @Email   : 876569085@qq.com
# @File    : connectdb.py
# @Software: PyCharm
"""
查询


"""

import pymysql
from common.handleconfig import conf


class DB:
    def __init__(self):
        # 创建一个连接对象
        self.conn = pymysql.connect(host=conf.get("db", "host"),
                                    port=conf.getint("db", "port"),
                                    user=conf.get("db", "user"),
                                    password=conf.get("db", "pwd"),
                                    charset=conf.get("db", "charset"),
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        # 创建一个游标
        self.cur = self.conn.cursor()

    def find_one(self, sql):
        """获取查询出来的第一条数据"""
        # 执行查询语句
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def find_all(self, sql):
        """获取查询出来的所有数据"""
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def find_count(self,sql):
        """返回查询数据的条数"""
        self.conn.commit()
        return self.cur.execute(sql)

    def close(self):
        """关闭游标，断开连接"""
        self.cur.close()
        self.conn.close()
