#!/bin/python3

def solution(A, B):
    L = max(A)
    Pmax = max(B)
 
    clmb = [0] * (L+2)
    clmb[1] = 1
    x=L+2
    for i in range(2, x):
        clmb[i] = (clmb[i-1] + clmb[i-2]) & ((1 << Pmax) - 1)

    h= len(A)
    climbs = [0] * h
 
    for j in range(h):
        climbs[j] = clmb[A[j]+1] & ((1 << B[j]) - 1)
 
    print(climbs)

'''
solution([4,4,5,5,1], [3,2,4,3,1])
'''
