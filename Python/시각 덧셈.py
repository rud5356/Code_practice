import sys

sys.stdin = open("시각덧셈.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    hour1, minute1, hour2, minute2 = map(int, input().split(" "))
    time = (hour1+hour2) * 60 + minute1 + minute2
    print("#{} {} {}".format(test_case, (time // 60 if time // 60 < 13 else time // 60 - 12), time % 60))
