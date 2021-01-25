import sys
import statistics
sys.stdin = open("D://Code_practice/Python/input (1).txt", "r")

T = int(input())
result = list(map(int, input().split(" ")))
#result.sort()
#a = int(T/2)
#print("{}".format(result[a]))

print(statistics.median(result))
