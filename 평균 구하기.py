import sys

sys.stdin = open("D:/Code_practice/input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    result = list(map(int, input().split(" ")))
    print("#{} {}".format(test_case, round(sum(result)/len(result))))
