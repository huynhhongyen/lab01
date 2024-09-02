# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:44:05 2024

@author: ASUS
"""

a = int(input('Nhập a = '))
b = int(input('Nhập b = '))
if 1 <= a <= 9 and 1 <= b <= 9:
    print('Chia lấy phần nguyên:',a//b)
    print('Chia lấy phần dư:',a%b)
else:
    print('Nhập lại giá trị.')
