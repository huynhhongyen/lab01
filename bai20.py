# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:33:38 2024

@author: ASUS
"""

a = float(input('Nhập a = '))
b = float(input('Nhập b = '))
c = float(input('Nhập c = '))
if a > b and a > c:
    print('Giá trị lớn nhất là:',a)
elif b > a and b > c:
    print('Giá trị lớn nhất là:',b)
else:
    print('Giá trị lớn nhất là:',c)
    