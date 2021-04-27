import sys

sys.stdin = open("impl_exam_sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = str(input())
    n1 = sum(list(map(int, n[0:len(n) // 2])))
    n2 = sum(list(map(int, n[len(n) // 2:])))
    if n1 == n2:
        result = "LUCKY"
    else:
        result = "READY"
    print(f"#{test_case} {result}")
