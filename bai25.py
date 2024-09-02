# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:08:54 2024

@author: ASUS
"""

chu = str(input('Nhập 1 chữ cái: '))
if chu == chu.lower():
    print('Chữ hoa của',chu,'là',chu.upper())
else:
    print('Chữ thường của',chu,'là',chu.lower())
