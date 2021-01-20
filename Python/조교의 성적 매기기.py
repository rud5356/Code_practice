import sys
sys.stdin = open("input (9).txt", "r")

T = int(input())
score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for test_case in range(1,T+1):
    N, K = map(int, input().split())
    a = []
    c = 0
    for t_case in range(1, N + 1):
        test = list(map(int, input().split(" ")))
        a.append(test[0] * 0.35 + test[1] * 0.45 + test[2] * 0.20)
    k_score = a[K-1]
    a.sort(reverse=True)
    c = a.index(k_score)//(N//10)
    print("#{} {}".format(test_case, score[c]))
