import sys
sys.stdin = open("D://Code_practice/Python/input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    result = list(map(int, input().split(" ")))
    result.sort(reverse=True)
    print("#{} {}".format(test_case,result[0]))
