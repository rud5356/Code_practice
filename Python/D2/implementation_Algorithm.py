import sys
sys.stdin = open("D:/Code_practice/Python/D2/impl_exam_sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n=str(input().strip())
    n1 = sum(map(int,n[:len(n)//2]))
    n2 = sum(map(int,n[len(n)//2:]))
    print(f"#{test_case} LUCKY"  if n1==n2 else f"#{test_case} READY")
