# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:33:17 2024

@author: ASUS
"""

print('=========== MENU ===========')
print('\t1. Hu tieu')
print('\t2. Chao long')
print('\t3. Banh canh')
print('\t4. Bun rieu')
print('\t5. Pho bo')
print('============================')
x = int(input('Moi nhap lua chọn: '))
if x == 1:
    print('Hu tieu')
elif x == 2:
    print('Chao long')
elif x == 3:
    print('Banh canh')
elif x == 4:
    print('Bun rieu')
elif x == 5:
    print('Pho bo')
else: print('Khong co trong menu, vui long nhap lai.')
