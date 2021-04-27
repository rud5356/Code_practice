import sys

sys.stdin = open("greedy_exam_sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n1, n2 = list(map(int, input().split(" ")))
    k = 0
    while n1 != 1:
        if n1 < n2:
            k += (n1 - 1)
            break
        re = n1 % n2
        if re != 0:
            n1 -= re
            k += re
        else:
            n1 = int(n1 / n2)
            k += 1
    print("#{} {}".format(test_case, k))
