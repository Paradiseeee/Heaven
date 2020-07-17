# -*- coding: utf-8 -*-
""" MySQL Helper
"""
import pymysql
import sqlalchemy
import numpy as np
import pandas as pd
from getpass import getpass
from warnings import filterwarnings

filterwarnings('ignore')


class MysqlHelper:
    ''' Frequently Used Functions for MySQL-IO'''

    def __init__(self, host='localhost', port=3306, charset='utf8'):
        '''Initialization'''

        self.host=host
        self.port=port
        self.charset=charset
        self.user = input('>>> Acount: \n')
        self.password = getpass('>>> Password: \n')
        self.database = input('>>> DataBase: \n')
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            charset=self.charset,
            user=self.user,
            password=self.password,
            database=self.database
            )
        self.cur = self.conn.cursor()
        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}' +
            f'@{host}:{port}/{self.database}?charset={charset}'
            )


    def flush_connection(self):
        '''Flush connection after update tables'''
        self.conn.close()
        self.conn = pymysql.connect(host=self.host, port=self.port, charset=self.charset, user=self.user, password=self.password, database=self.database)
        self.cur = self.conn.cursor()
        self.engine = sqlalchemy.create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?charset={self.charset}')


    def execute(self, sql, params=None):
        '''Execute and fetch all result and returns'''

        rows = self.cur.execute(sql, params)
        results = self.cur.fetchall()
        return {'affected rows': rows, 'returns': results}


    def write_df(self, df, table):
        '''Write df to table (whice has the same fields)'''

        df.to_sql(table, con=self.engine, if_exists='append', index=False)
        print('>>> Writing Succeed！')


    def create_table(self, tbname, sql=None):
        '''A general guide for create table'''

        if sql:
            self.execute(sql)
        
        else:
            fields, types, nulls = [], [], []
            while True:
                fields.append(input('>>> 请输入字段名：\n'))
                types.append(input('>>> 请定义数据类型：\n'))
                nulls.append(input('>>> 是否允许空值？（y/n） \n'))
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

        print(f'\n>>> Succefully create {tbname} ！\n')
        self.returns_to_df(f'desc {tbname};', cols=['Field', 'Type', 'NULL', 'Key', 'Default', 'Extra'])


    def returns_to_df(self, sql, cols=[], show=True):
        '''A pretty version of self.execute, needed accurate cols'''

        try:
            result = self.execute(sql)
        except Exception as e:
            return e
        # default values for frequently used query
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
        for i, row in enumerate(returns):
            for j in range(len(row)):
                df[cols[j]][i] = row[j]
        if show:
            print(df.to_markdown())
        else:
            return df


if __name__ == "__main__":

    examples = '''
    helper = MysqlHelper()
    helper.execute('show tables;')
    helper.create_table('test')
    helper.write_df(df, 'test')
    helper.flush_connection()
    helper.returns_to_df('DESC test;')
    '''
    print(examples)
