#numero de xicaras de cada alimento
 A, B, C = map(int, input().split())
 # criei um programa para que nao aconteça 'desperdicio'
 resto = 0
 while A >= 2 and B >= 3 and C >= 5:
   A -= 2
   B -= 3
   C -= 5
   resto += 1
