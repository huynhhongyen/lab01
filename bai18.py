# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:31:06 2024

@author: ASUS
"""

    #Thời điểm 1:
hour = int(input('Nhập giờ: '))
min = int(input('Nhập phút: '))
sec = int(input('Nhập giây: '))
print('Thời điểm 1: {:02} giờ {:02} phút {:02} giây'.format(hour,min,sec))
    
    #Thời điểm 2:
h = int(input('\nNhập giờ: '))
m = int(input('Nhập phút: '))
s = int(input('Nhập giây: '))
print('Thời điểm 2: {:02} giờ {:02} phút {:02} giây'.format(h,m,s))

sum_sec = sec + s
sum_min = min + m + sum_sec//60 
sum_hour = hour + h + sum_min//60
tong_sec = sum_sec % 60
tong_min = sum_min % 60
print('\nKết quả cộng 2 giờ là: {} giờ {} phút {} giây'.format(sum_hour,tong_min,tong_sec))

time1 = hour*3600 + min*60 + sec
time2 = h*3600 + m*60 + s
t = abs(time1 - time2)
hieu_hour = t // 3600
hieu_min = (t % 3600) // 60
hieu_sec = t % 60
print('Kết quả trừ 2 giờ này là: {} giờ {} phút {} giây'.format(hieu_hour,hieu_min,hieu_sec))
