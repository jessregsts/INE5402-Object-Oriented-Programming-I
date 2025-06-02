# -*- coding: utf-8 -*-
while True:
    try:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        notas = (2, 5, 10, 20, 50, 100)
        troco = n - m
        existe = False
        for i in range(len(notas)):
            for j in range(len(notas)):
                if notas[i] + notas[j] == troco:
                    existe = True
        print('possible' if existe else 'impossible')
    except EOFError:
        break
