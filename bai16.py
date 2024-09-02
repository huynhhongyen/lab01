# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:20:06 2024

@author: ASUS
"""

hour = int(input('Nhập giờ (0-23): '))
min = int(input('Nhập phút (0-60): '))
sec = int(input('Nhập giây (0-60): '))
if hour > 23 or min > 60 or sec > 60:
    print('Nhập lại giờ, phút, giây.')
else:
    print('{}h{}p{}s'.format(hour,min,sec))
    print('Đổi ra giây:',hour*3600 + min*60 + sec)
