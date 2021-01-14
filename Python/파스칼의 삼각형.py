import sys
import math

sys.stdin = open("input (6).txt", "r")

T = int(input())


def combination(n, r):
    c = int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
    return str(c)


for test_case in range(1, T + 1):
    result = int(input())
    a = []
    print("#{}".format(test_case))
    for i in range(0, result):
        a.append([])
        if i == 0:
            a[i].append(combination(i, 0))
        else:
            for j in range(0, i + 1):
                a[i].append(combination(i, j))
    for i in a:
        for j in i:
            print(j, end=" ")
        print()
