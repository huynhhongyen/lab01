# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:26:15 2024

@author: ASUS
"""

hour = int(input('Nhập giờ: '))
min = int(input('Nhập phút: '))
sec = int(input('Nhập giây: '))
if hour > 23 or min > 60 or sec > 60:
    print('Giờ, phút, giây không hợp lệ.')
else:
    print('Giờ, phút, giây hợp lệ.')    
