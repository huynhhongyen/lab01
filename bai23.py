# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:17:53 2024

@author: ASUS
"""

import math
a = float(input('Nhập hệ số a: '))
b = float(input('Nhập hệ số b: '))
c = float(input('Nhập hệ số c: '))
delta = b*b - 4*a*c

if a != 0: 
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print('Phương trình có 2 nghiệm phân biệt:',x1,'và',x2)
    
    elif delta == 0:
        x = -b/(2*a)
        print('Phương trình có nghiệm kép:',x)
    
    else:
        print('Phương trình vô nghiệm.')
else:
    print('Không phải phương trình bậc hai.')
