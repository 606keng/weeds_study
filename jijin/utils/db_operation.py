#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: db_operation.py
@time: 2020/07/01 
"""
import json

import pymysql


class DbOperation():
    def __init__(self, host, user, password, database, port=3306):
        """
        host：数据库服务器地址
        user：登录数据库的用户名
        password：登录数据库的密码
        database：要连接的数据库名称
        port：连接数据库的端口
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        # 连接数据库
        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    database=self.database,
                                    port=self.port)

    def select(self, sql):
        try:
            # 使用cursor操作游标
            cursor = self.conn.cursor()
            # 执行sql
            cursor.execute(sql)
            # 获取所有记录，返回格式为元组
            results = cursor.fetchall()
            return results
        except:
            print("SQL语句: {} 无法查询".format(sql))

    def update(self, sql):
        try:
            # 使用cursor操作游标
            cursor = self.conn.cursor()
            # 执行sql
            cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # 发生错误时回滚
            self.conn.rollback()

    def delete(self, sql):
        try:
            # 使用cursor操作游标
            cursor = self.conn.cursor()
            # 执行sql
            cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # 发生错误时回滚
            self.conn.rollback()

    def insert(self, sql):
        try:
            # 使用cursor操作游标
            cursor = self.conn.cursor()
            # 执行sql
            cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # 发生错误时回滚
            self.conn.rollback()

    def run_stored_procedure(self, args):
        if type(args) is str:
            args = (args,)
        elif type(args) is list:
            args = tuple(args)
        print(args)
        """
        调用存储过程
        """
        for arg in args:
            arg = (arg,)
            try:
                cur = self.conn.cursor()
                # 调用存储过程，QSP_Clean_Data为存储过程名称，args为存储过程要传入的参数，格式为元组
                cur.callproc('QSP_Clean_Data', arg)
                self.conn.commit()
            except:
                # 发生错误时回滚
                self.conn.rollback()

    def del_black_vin(self):
        self.delete('DELETE from dht_vin_black_check WHERE car_vin="LE4WG4CB4GL152120" and op_type="BLACK_LIST";')

    def close(self):
        # 关闭数据库连接
        self.conn.close()


class DB(DbOperation):
    def __init__(self, file):
        data = json.load(file)


if __name__ == '__main__':
    test_data = {"host": "127.0.0.1",
                 "user": "root",
                 "password": "dlh480746",
                 "database": "jijin"
                 }
    db = DbOperation(**test_data).select("select * from zhishu_jijin")
    print(db)