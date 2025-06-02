# -*- coding: utf-8 -*-
n = int(input())  # lê o número de casos de teste
for _ in range(n):
    soma = 0
    o = input().split()  # entrada das tomadas por régua
    k = int(o[0])        # número de réguas
    resto = o[1:]        # tomadas disponíveis em cada régua
    for i in resto:
        soma += int(i)
    x = soma - k + 1  # cálculo total descontando as perdas de encaixe
    print(x)
