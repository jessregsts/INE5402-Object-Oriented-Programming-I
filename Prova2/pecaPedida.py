# vamos ajudar joaozinho!
n = int(input())  # as peças
pecasdejoao = list(map(int, input().split()))
pecasdejoao.sort()  # inicio da lista

for i in range(len(pecasdejoao)):
    if pecasdejoao[i] != (i + 1):
        break

if pecasdejoao[i] == (i + 1):
    i += 1

print(i + 1)
