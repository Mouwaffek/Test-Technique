#!/bin/python3

def solution(N, A):
    counters = [0] * N
    max_value = 0
    last_update = 0
    n1 = N+1
    for i in A:
        if i < n1:
            if counters[i-1] < last_update:
                counters[i-1] = last_update

            counters[i-1]+=1

            if counters[i-1] > max_value:
                max_value = counters[i-1]
        else:
            last_update = max_value

    for i in range(N):
        if counters[i] < last_update:
            counters[i] = last_update

    print(counters)


solution(5,[3,4,4,6,1,4,4])
