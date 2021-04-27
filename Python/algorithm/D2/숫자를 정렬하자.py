import sys
sys.stdin = open("D://Code_practice/Python/D2/input_숫자정렬.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    z = int(input())
    result = list(map(int, input().split()))
    print(f"#{test_case}", *sorted(result))
