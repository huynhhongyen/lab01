# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:05:57 2024

@author: ASUS
"""

day = int(input('Nhập ngày sinh: '))
mon = int(input('Nhập tháng sinh: '))
year = int(input('Nhập năm sinh: '))
    #câu a:
print('a) {:02}/{:02}/{:04}'.format(day,mon,year))

    #câu b:
year_short = year % 100
print('b) {:02}/{:02}/{:02}'.format(day,mon,year_short))

    #câu c:
print('c) {:04}/{:02}/{:02}'.format(year,mon,day))
