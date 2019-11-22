#!/usr/bin/python3

T = int(input())
for i in range(T):
    N = int(input())
    test = True
    j = 1
    s = input()
    s = s.split(" ")
    s = [int(g) for g in s]
    for v in s:
        v = int(v)
        if v != j and v != 0:
            print("NE")
            test = False
            break
        j += 1
    if test:
        print("ANO")
