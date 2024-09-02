# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:14:27 2024

@author: ASUS
"""

a = int(input('Nhập a = '))
b = int(input('Nhập b = '))
c = int(input('Nhập c = '))
d = int(input('Nhập d = '))
if a < b and a < c and a < d:
    print('Giá trị nhỏ nhất là:',a)
elif b < a and b < c and b < d:
    print('Giá trị nhỏ nhất là:',b)
elif c < a and c < b and c < d:
    print('Giá trị nhỏ nhất là:',c)
else:
    print('Giá trị nhỏ nhất là:',d)
    