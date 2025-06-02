# -*- coding: utf-8 -*-
J0, J1 = 0, 0  # variaveis soma do primeiro e segundo exercito
N, M, S = map(int, input().split())  # entradas n, m, s
CoefAng = N / M  # coeficiente angular do rio
for _ in range(S):  # loop soldados
    X, Y, H = map(int, input().split())  # entradas x, y, h
    if X < Y * CoefAng:  # condicao soldado acima do rio
        J0 += H  # soma para o primeiro exercito
    else:  # entao soldado abaixo do rio
        J1 += H  # soma para o segundo exercito
print("{0} {1}".format(J0, J1))  # printa o resultado
