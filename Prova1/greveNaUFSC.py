 # d sera o 'tanto'/quantidade de dinheiro que a ufsc tem
 d = 0
 # n sao os valores citados na reuniao
 n = int(input())
 # inicio do loop 'valores'
 for i in range(n):
   x = input().split()
   t = x[0]
   # converter os gastos da universidade para inteiros
   c = int(x[1])

if t == "V": #o governo oferece verba
   d += c
else:
 # ocorre um corte
   d -= c
 # para ver se há dinheiro na conta da ufsc
 if d >= 0:
 # a ufsc tem dinheiro? a greve acaba
   print("A greve vai parar.")
 else:
 # a ufsc nao tem dinheiro/saldo negativo? nao vai ter corte, vai ter luta
   print("NAO VAI TER CORTE, VAI TER LUTA!")
