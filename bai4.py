# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:53:54 2024

@author: ASUS
"""

N = int(input('Nhập số nguyên dương N (có 2 chữ số): '))
a = N//10
b = N%10
if 10 <= N <= 99:
    print('Tổng các chữ số của N:',a+b)
else:
    print('Nhập lại giá trị N.')
