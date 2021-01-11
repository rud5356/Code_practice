import sys

sys.stdin = open("D://Code_practice/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    result = list(map(int, input().split(" ")))
    if result[0]!=result[1] :
        if result[0]>result[1] :
            print("#{} {}".format(test_case,">"))
        else :
            print("#{} {}".format(test_case,"<"))
    else :
        print("#{} {}".format(test_case,"="))
