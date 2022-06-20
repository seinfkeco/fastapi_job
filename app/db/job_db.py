# -*- coding: utf-8 -*-
__auther__ = '35942'


import sqlite3

class JobDb(object):

    @classmethod
    def conn_job_logs_db(cls):
        cls.conn = sqlite3.connect("logs.sqlite")
        print("连接数据库success")

    @classmethod
    def init_job_log_table(cls):
        c = cls.conn.cursor()
        c.execute('''CREATE TABLE job_log
               (run_date CHAR(10)     NOT NULL,
               run_time    CHAR(18)  PRIMARY KEY  NOT NULL,
               job_status         INT NOT NULL);''')
        print("数据表创建成功")
        cls.conn.commit()

    @classmethod
    def job_log(cls, run_date, run_time, job_status=1):
        conn = sqlite3.connect("logs.sqlite")
        print("连接数据库success")
        c = conn.cursor()
        c.execute("""INSERT INTO job_log (run_date,run_time,job_status) \
                  VALUES ('%s', '%s', %d)"""%(run_date, run_time, job_status))
        print("记录执行记录success")
        cls.conn.commit()
        cls.conn.close()