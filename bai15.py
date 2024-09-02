# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:36:06 2024

@author: ASUS
"""

a = float(input('Nhập a = '))
b = float(input('Nhập b = '))
a_sqrt = pow(a,1/3)
b_sqrt = pow(b,1/3)
c_sqrt = pow((a*b),1/3)
A = ((a+b)/(a_sqrt + b_sqrt) - (c_sqrt))/(pow(a_sqrt - b_sqrt,2))
print('Giá trị biểu thức:',A)
