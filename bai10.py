# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:41:44 2024

@author: ASUS
"""

a = str(input('Nhập số xe của bạn (gồm 4 chữ số): '))
a_so = int(a)
nut = a_so//1000 + (a_so%1000)//100 + (a_so%100)//10 + a_so%10
if len(a) == 4:
    print('Số xe của bạn được',nut%10,'nút.')
else:
    print('Nhập lại số xe của bạn.')
