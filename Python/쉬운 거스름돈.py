import sys

sys.stdin = open("input (5).txt", "r")

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1, T + 1):
    result = list(map(int, input().split()))
    mlist = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(money)):
        mlist[i] = (lambda x: str(int(x / money[i])) if i == 0 else str(int(x % money[i - 1] / money[i])))(result[0])
    print("#{}\n{}".format(test_case, " ".join(mlist)))
