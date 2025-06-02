# -*- coding: utf-8 -*-
from math import gcd  # máximo divisor comum

while True:
    try:
        M = int(input())  # último alinhamento
        L = list(map(int, input().split()))  # períodos orbitais das luas
        J = L[0]
        for i in L[1:]:
            J = (J * i) // gcd(J, i)  # cálculo do MMC (mínimo múltiplo comum)
        J -= M  # diferença até o próximo alinhamento
        print(J)
    except EOFError:
        break
