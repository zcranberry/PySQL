#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import psycopg2
import sys
conn = None
cursor = None
def log_info(level, file_name, line, msg):
    level = 'D'
    file_name = 'abc.sql'
    line = 2
    msg = 'echo_hello'
    curr_time = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())

    output_msg = '%s %s %d %s' % (level, curr_time, line, msg)


def db_conn(host = 'localhost', db, usr):
    global conn, cusror
    conn = psycopg2.connect(database = db, user = usr)
    cursor = conn.cursor()

def db_disc():



def sql_exec():

def sql_line_process():



def main(): #python PySQL.py abc.sql
    if (len(sys.argv) < 2):
        return 1
    SQL_file = sys.argv[1]

    global conn, cursor
    db_conn()


    f = open(SQL_file)

    sql_line = None

    try:
        cursor.execute(sql_line)
    except psycopg2.Error as e:
        print e.pgerror





