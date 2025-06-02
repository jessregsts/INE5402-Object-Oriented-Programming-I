total, min = map(int, input().split())  # total de pessoas e número mínimo
chegada = input().split()               # horário de chegada de cada aluno
atrasos = 0

# contando e processando os atrasos
for i in range(total):
    if int(chegada[i]) > 0:
        atrasos += 1

# condição para verificar se a aula será cancelada
if (total - atrasos) < min:
    print('NO')
else:
    print('YES')
