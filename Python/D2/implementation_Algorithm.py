import sys
sys.stdin = open("impl_exam_sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n=str(input())
    n1, n2 = 0, 0
    for i in range(0,len(n)//2):
        n1 += int(n[i])
        n2 += int(n[len(n)-i-1])
    if n1 == n2:
        a = "LUCKY"
    else:
        a = "READY"
    print(f"#{test_case} {a}")


