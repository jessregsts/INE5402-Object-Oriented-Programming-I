# -*- coding: utf-8 -*-
def domino(N):
    return ((N + 1) * (N + 2)) // 2

N = int(input())
print(domino(N))
