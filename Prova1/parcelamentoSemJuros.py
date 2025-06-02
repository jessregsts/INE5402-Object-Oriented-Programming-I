 # V como valor do produto e P como parcelas
 V = int(input())
 P = int(input())
 # divisao valor e parcelas COM resto da mesma divisao
 P2 = V // P
 P1 = V % P
 #inicio do loop
 for i in range(P):
   if P1 > 0: # se o resto for maior que 0
     P1 -= 1 # desconte os valores 'subdivididos' em cada parcela
     print(P2 + 1) # parcela + o valor da subdivisao
 else:
    print(P2) # divisao de resto 0/parcela sem o valor da subdivisao
