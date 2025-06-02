# -*- coding: utf-8 -*-
SM = -100  # variável soma total
SA = 0  # variável soma atual
N = int(input())  # entrada N
V = list(map(int, input().split()))  # entrada V/lista
for i in range(N):  # loop com os valores da lista
    SA += V[i]  # soma do valor da lista com soma atual
    if SA > SM:  # se soma atual for a maior registrada, substituir a SM pela SA
        SM = SA
    if SA < 0:  # se a soma atual negativa, ignorar a soma
        SA = 0
print(SM)  # printa o resultado
