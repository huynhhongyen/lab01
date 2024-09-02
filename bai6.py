# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:10:28 2024

@author: ASUS
"""

import datetime
age = int(input('Nhập vào năm sinh: '))
year = datetime.datetime.now().year
if 1900 <= age <= year:
    print('Bạn sinh năm',age,'vậy bạn',year-age,'tuổi.')
else:
    print('Nhập lại năm sinh')
