n = int(input())  # número de crianças
m = f = 0         # carrinhos (m) e bonecas (f)

# contador de crianças de acordo com o sexo
for i in range(n):
    crianca = input().split()
    if crianca[1] == 'M':
        m += 1
    if crianca[1] == 'F':
        f += 1

# print do número de carrinhos e bonecas
print(f'{m} carrinhos')
print(f'{f} bonecas')
