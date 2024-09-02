# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:26:51 2024

@author: ASUS
"""

weight = float(input('Nhập cân nặng (kg): '))
height = float(input('Nhập chiều cao (m): '))
bmi = weight/height**2
print('Số đo kiểm tra sức khỏe BMI là:',round(bmi,3))
