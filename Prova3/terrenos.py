# -*- coding: utf-8 -*-
X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())
X4, Y4 = map(int, input().split())

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())
A3, B3 = map(int, input().split())
A4, B4 = map(int, input().split())

AreaA = abs(((X1 + X2)*(Y1 - Y2)) + ((X2 + X3)*(Y2 - Y3)) + ((X3 + X4)*(Y3 - Y4)) + ((X4 + X1)*(Y4 - Y1)))
AreaB = abs(((A1 + A2)*(B1 - B2)) + ((A2 + A3)*(B2 - B3)) + ((A3 + A4)*(B3 - B4)) + ((A4 + A1)*(B4 - B1)))

if AreaA > AreaB:
    print('terreno A')
else:
    print('terreno B')
