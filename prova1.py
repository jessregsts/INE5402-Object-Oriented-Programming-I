# BATALHA DOS 5 EXÉRCITOS

# Os representandes do exército
 H, E, A, O, W, X = input().split()
 H = int(H)
 E = int(E)
 A = int(A)
 O = int(O)
 W = int(W)
 X = int(X)

# Com Bilbo
 aSalvo = H + E + A + X
 
# Contra Bilbo
 emPerigo = O + W

# Comparando as duas situacoes
 if aSalvo > emPerigo:
   print ('Middle-earth is safe.')
 else:
   print ('Sauron has returned.')

# RESTO 1

# Para ajudar john
 A = int(input())
 B = int(input())
 # Primeiro passo: '%' = resto na linguagem Python
 # Segundo passo: logo, é simples criar um programa ao amigo
 print(A % B)

# PARCELAMENTO SEM JUROS
# V como valor do produto e P como parcelas
 V = int(input())
 P = int(input())
 
# Divisao valor e parcelas COM resto da mesma divisao
 P2 = V // P
 P1 = V % P
 
# Inicio do loop
 for i in range(P):
   if P1 > 0: # Se o resto for maior que 0
     P1 -= 1 # Desconte os valores 'subdivididos' em cada parcela
     print(P2 + 1) # Parcela + o valor da subdivisao
 else:
    print(P2) # divisao de resto 0/parcela sem o valor da subdivisao
 
# A IDADE DE DONA MONICA

# Idade da dona monica e de seus dois filhos
 m = int(input())
 a = int(input())
 b = int(input())
 
# Idade do terceiro filho que sera calculada
 c = m - (a + b)

# Comparaçao entre as idades (qual a maior)
 if a > b and a > c:
   print(a)
 elif b > a and b > c:
   print(b)
 elif c > a and c > b:
   print(c)

# GREVE NA UFSC
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

# RECEITA DE BOLO
 #numero de xicaras de cada alimento
 A, B, C = map(int, input().split())
 # criei um programa para que nao aconteça 'desperdicio'
 resto = 0
   while A >= 2 and B >= 3 and C >= 5:
     A -= 2
     B -= 3
     C -= 5
     resto += 1
     
