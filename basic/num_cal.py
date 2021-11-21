#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@File: num_cal.py
@Project: basic
@Desc: 常见算术运算
@Time: 2021/11/21 20:45:54
@Author: wuwenrufeng (wuwenrufeng@163.com)
@Last Modified: 2021/11/21 20:45:57
@Modified By: wuwenrufeng (wuwenrufeng@163.com)
@Version: 1.0
@License: Copyright(C) 2021 - 2021 wuwenrufeng, Borland
"""
import math

x, y = 3, 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
# 向下取整
print(x // y) 
print(math.floor(x/y))
# 向上取整
print(math.ceil(x/y))
print(x % y)
print(-x)
print(abs(-x))
print(int(3.9))
print(float(x))
print(x ** y)

# result:
5
1
6
1.5
1
1
2
1
-3
3
3
3.0
9