import sys

sys.stdin = open("input_최빈수.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    z = input()
    test = list(map(int, input().strip().split()))
    cnt = [0]*101
    for i in test:
        cnt[i]+=1
    c = max(cnt)
    for j in range(100,0,-1):
        if cnt[j] == c:
            print(f"#{test_case} {j}")
            break