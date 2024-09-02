# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:54:38 2024

@author: ASUS
"""

print('\tHình vuông: v')
print('\tHình chữ nhật: n')
print('\tHình tròn: t')
hinh = str(input('Nhập hình (v, n, t): '))
if hinh == 'v':
    print('Tính P và S của hình vuông')
    canh = float(input('Nhập cạnh = '))
    print('Kết quả: P =',canh*4,'\tS =',canh**2)
elif hinh == 'n':
    print('Tính P và S của hình chữ nhật')
    rong = float(input('Nhập chiều rộng = '))
    dai = float(input('Nhập chiều dài = '))
    print('Kết quả: P =',(dai+rong)*2,'\tS =',dai*rong)
elif hinh == 't':
    print('Tính P và S của hình tròn')
    r = float(input('Nhập bán kính = '))
    pi = 3.14
    print('Kết quả: P =',2*pi*r,'\tS =',pi*r*r)
else:
    print('Nhập lại hình.')
