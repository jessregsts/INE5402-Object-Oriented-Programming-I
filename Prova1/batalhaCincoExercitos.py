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
     
