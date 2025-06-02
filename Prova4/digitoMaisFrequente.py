# -*- coding: utf-8 -*-
while True:
    try:
        n = input()
        j = [0] * 10  # contadores de 0 a 9
        for i in n:
            j[int(i)] += 1
        print(9 - j[::-1].index(max(j)))  # dígito com maior frequência
    except EOFError:
        break
