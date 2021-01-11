import sys
sys.stdin = open("D://test/input.txt", "r")
T = int(input())
for i in range(T):
    result = list(map(int, input().split(" ")))
    odd_nums = [num for num in result if num % 2 == 1]
    print("#{} {}".format(i+1, sum(odd_nums)))
