import sys
sys.stdin = open("D:/Code_practice/Python/D2/date_calculator.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    day = [31,28,31,30,31,30,31,31,30,31,30,31]
    result = 0
    for i in range(m1,m2):
        result+=day[i-1]
    result = result-d1+d2+1
    print(f"#{test_case} {result}")
