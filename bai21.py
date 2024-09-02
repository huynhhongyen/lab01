# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:36:51 2024

@author: ASUS
"""

a = int(input('Nhập một số bất kì: '))
chu_so = ['Khong','Mot','Hai','Ba','Bon','Nam','Sau','Bay','Tam','Chin']
if 0 <= a <= 9:
    print(chu_so[a])
else:
    print('Khong doc duoc')
    