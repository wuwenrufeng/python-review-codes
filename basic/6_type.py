#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@File: 6_type.py
@Project: basic
@Desc: 类型
@Time: 2021/11/28 21:25:03
@Author: wuwenrufeng (wuwenrufeng@163.com)
@Last Modified: 2021/11/28 21:25:06
@Modified By: wuwenrufeng (wuwenrufeng@163.com)
@Version: 1.0
@License: Copyright(C) 2021 - 2021 wuwenrufeng, Borland
"""

# String
word = '字符串'
sentence = "这是一个句子."
paragraph = """这是一个段落，
可以由多行组成"""

# slice
string = "123456789"
print(string)
print(string[0:-1])
print(string[0])
print(string[1:5:2]) # 起始，结束，步长

# raw string
print("\n")
print(r"\n") # r 表示输出原始字符串，不需要转义 输出：\n

# 胶水语言
print("this ""is "" python")