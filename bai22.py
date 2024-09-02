# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:49:21 2024

@author: ASUS
"""

a = float(input('Nhập hệ số a: '))
b = float(input('Nhập hệ số b: '))
if a == 0:
    if b == 0:
        print('Phương trình có vô số nghiệm.')
    else: 
        print('Phương trình vô nghiệm.')
else:
    print('Phương trình có nghệm duy nhất là:',-b/a)
