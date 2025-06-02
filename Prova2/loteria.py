flavinho = input().split()  # a aposta de flavinho
sorteio = input().split()   # o sorteio
resultado = ['azar', 'azar', 'azar', 'terno', 'quadra', 'quina', 'sena']  # os resultados possíveis
resto = 0

# quantos números flavinho acertou
for i in flavinho:
    if i in sorteio:
        resto += 1

# a condição para o resultado
if resto == 6:
    print('sena')
elif resto == 5:
    print('quina')
elif resto == 4:
    print('quadra')
elif resto == 3:
    print('terno')
else:
    print('azar')
