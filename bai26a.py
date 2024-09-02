# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:12:38 2024

@author: ASUS
"""

a = float(input('Nhập a = '))
b = float(input('Nhập b = '))
c = float(input('Nhập c = '))
if a > b:
    temp = a
    a = b 
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp
print('Thứ tự tăng dần là:',a,b,c)
