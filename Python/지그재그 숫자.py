import sys
sys.stdin = open("input (8).txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    test = int(input())
    result = []
    for a in range(0,test):
        result.append(a+1)
    even = sum(list(filter(lambda x : x % 2 == 0, list(map(int, result)))))
    odd = sum(list(filter(lambda x : x % 2 != 0, list(map(int, result)))))
    print("#{} {}".format(test_case, odd-even))