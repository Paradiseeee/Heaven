# -*- coding: utf-8 -*-
"""
MySQL Frequently Used Function Integrated with Python.
View Example：
https://paradiseeee.github.io/2019/03/09/Python-爬虫快速入门-下/#62-写入-mysql-数据库
"""

import pymysql
import sqlalchemy
import numpy as np
import pandas as pd
from getpass import getpass
from warnings import filterwarnings

filterwarnings('ignore')


class MysqlHelper:
    '''
    Functions：
    helper.flush_connection(self) -- flush connection after update tables.
    helper.execute(self, sql, params=None) -- execute and fetch all result and returns.
    helper.write_df(self, df, table) -- write df to table (whice has the same fileds).
    helper.create_table(self, tbname, sql=None) -- a general guide to create table (can also use sql instead of guide).
    helper.return_to_df(self, sql, cols=[], show=True) -- a pretty version of self.execute, needed accurate cols, can return or show.
    '''

    def __init__(self, host='localhost', port=3306, charset='utf8'):
        '''Initializing'''
        self.host=host
        self.port=port
        self.charset=charset
        self.user = input('>>> Acount: \n')
        self.password = getpass('>>> Password: \n')
        self.database = input('>>> DataBase: \n')
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    charset=self.charset,
                                    user=self.user,
                                    password=self.password,
                                    database=self.database)
        self.cur = self.conn.cursor()
        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}' +
            f'@{host}:{port}/{self.database}?charset={charset}'
            )
        
    def flush_connection(self):
        '''建表或更新后需要重建连接才能查询新内容'''
        self.conn.close()
        self.conn = pymysql.connect(host=self.host, port=self.port, charset=self.charset, user=self.user, password=self.password, database=self.database)
        self.cur = self.conn.cursor()
        self.engine = sqlalchemy.create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?charset={self.charset}')

    def execute(self, sql, params=None):
        '''重新定义 pymysql 的 execute 方法，一步到位'''
        rows = self.cur.execute(sql, params)
        results = self.cur.fetchall()
        return {'affected rows': rows, 'returns': results}

    def write_df(self, df, table):
        '''将 DataFrame 写入已经存在的表'''
        df.to_sql(table, con=self.engine, if_exists='append', index=False)
        print('>>> 成功写入数据库！')

    def create_table(self, tbname, sql=None):
        '''智能创建建表语句'''
        if sql:
            self.execute(sql)
        else:
            fields, types, nulls = [], [], []
            while True:
                field = input('>>> 请输入字段名：\n')
                type = input('>>> 请定义数据类型：\n')
                null = input('>>> 是否允许空值？（y/n） \n')
                fields.append(field)
                types.append(type)
                nulls.append(null)
                ctn = input('继续（1）| 撤销上次输入（2）| 结束（3）：\n')
                if ctn == '3':
                    pk = input('>>> 请定义主键：（多个用 "," 隔开）\n')
                    break
                elif ctn == '2':
                    fields.pop()
                    types.pop()
                    nulls.pop()
            nulls = ['NOT NULL' if n=='n' else 'NULL' for n in nulls]
            fields = [' '.join(tpl) for tpl in zip(fields, types, nulls)]
                
            sql = f"CREATE TABLE IF NOT EXISTS {tbname}("
            sql += f"{', '.join(fields)}, PRIMARY KEY ({pk}));"
            self.execute(sql)
        print(f'\n>>> 成功创建表 {tbname} ！')

    def returns_to_df(self, sql, cols=[], show=True):
        '''将查询结果输出为 DataFrame，cols 需要与查询的字段一一对应'''
        try:
            result = self.execute(sql)
        except Exception as e:
            return e
        if not cols:
            if 'describe' in sql.lower():
                cols = ['Field', 'Type', 'NULL', 'Key', 'Default', 'Extra']
            elif 'show tables;' == sql.lower():
                cols = ['Tables']
            elif 'show databases;' == sql.lower():
                cols = ['DataBases']      
        rows = result['affected rows']
        returns = result['returns']
        df = pd.DataFrame(np.random.randn(rows, len(cols)), columns=cols)
        for i, r in enumerate(returns):
            for j in range(len(r)):
                df[cols[j]][i] = r[j]
        if show:
            print(df.to_markdown())
        else:
            return df
