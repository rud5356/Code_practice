import sys
import math

sys.stdin = open("input (6).txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    result = int(input())
    a = []
    print("#{}".format(test_case))
    for i in range(0, result):
        a.append([])
        if i == 0:
            a[i].append(1)
        else:
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j-1]+a[i-1][j])
    for i in a:
        for j in i:
            print(j, end=" ")
        print()
