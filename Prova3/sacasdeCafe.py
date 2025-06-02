# -*- coding: utf-8 -*-
while True:  # loop para os casos
    s = 0  # variavel da soma
    try:  # detecta o 'fim'
        M, N = map(int, input().split())  # entradas m e n
    except EOFError:  # quebra o loop no fim
        break
    for _ in range(M):  # loop para cada linha
        s += sum(map(int, input().split()))  # faz a soma na linha
    print("{0} saca(s) e {1} litro(s)".format(s // 60, s % 60))  # printa o resultado
