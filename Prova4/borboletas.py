# -*- coding: utf-8 -*-
p = []
q = []
N = int(input())
for i in range(N):
    p.append(list(map(int, input().split())))
for i in range(N * 2):
    x, y = map(int, input().split())
    q.append(p[x - 1][y - 1])
q = set(q)
print(len(q))
