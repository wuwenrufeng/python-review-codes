#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@File: 5_multi_statements.py
@Project: basic
@Desc: 多行语句
@Time: 2021/11/28 21:19:02
@Author: wuwenrufeng (wuwenrufeng@163.com)
@Last Modified: 2021/11/28 21:19:24
@Modified By: wuwenrufeng (wuwenrufeng@163.com)
@Version: 1.0
@License: Copyright(C) 2021 - 2021 wuwenrufeng, Borland
"""

# 使用反斜线\
# [],{},()中不使用
total = 1 + \
        2 + \
        3
print(total)

# 一行中包含多条语句,用;分割 
import sys; x="abc"; sys.stdout.write(x + "\n")