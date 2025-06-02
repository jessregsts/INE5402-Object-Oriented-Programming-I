n = int(input())  # número de elfos
total = 0
dicionario = {
    'bonecos': 0,
    'arquitetos': 0,
    'musicos': 0,
    'desenhistas': 0
}

for i in range(n):
    nome, profissao, tempo = input().split()
    tempo = int(tempo)
    dicionario[profissao] += tempo

# cada profissão contribui com uma quantidade diferente de trabalho
total += dicionario['bonecos'] // 8
total += dicionario['arquitetos'] // 4
total += dicionario['musicos'] // 6
total += dicionario['desenhistas'] // 12

print(total)
