# -*- coding: utf-8 -*-
while True:
    try:
        N = int(input())  # insere N inteiro
        resultado = []  # organiza a matriz a ser montada
        coluna2 = N - 1  # regra para formação da coluna 2
        for i in range(N):
            tmp = []
            for j in range(N):
                if j == coluna2:
                    tmp.append(2)
                elif i == j:
                    tmp.append(1)
                else:
                    tmp.append(3)
            coluna2 -= 1
            resultado.append(tmp)
        for i in range(N):
            X = ''
            for j in range(N):
                X += str(resultado[i][j])
            print(X)
    except EOFError:
        break
