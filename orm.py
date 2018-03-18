# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:04:18 2018

@author: 28148
"""

__author__ = 'Vi huang'

def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
            host=kw.get('host', 'localhost'),
            port=kw.get('port', 3306),
            user=kw['user'],
            password=kw['password'],
            db=kw[db],
            charset=kw.get('charset', 'utf8'),
            autocommit=kw.get('autocommit', True),
            maxsize=kw.get('maxsize', 10),
            minsize=kw.get('minszie', 1),
            loop = loop
            )
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur =  yield