# -*- coding: utf-8 -*-
n = int(input())  # insere valores
l = []  # declara a lista
while n:
    n -= 1  # subtrai outro valor com o valor da variavel n
    l.append(int(input()))  # add um novo item a lista
l = set(l)  # armazena multiplos item na variavel
print(len(l))  # retorna o numero de itens do objetvo
