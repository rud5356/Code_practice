import sys
sys.stdin = open("D:/Code_practice/Python/D2/input_백만장자프로젝트.txt", "r")

for t in range(1, int(input()) + 1):
    n = int(input())
    case = list(map(int,input().split()))
    x,money,a = 0,0,0
    m = case[-1]
    for i in reversed(range(n-1)):
        x += 1
        money += case[i]
        if case[i]>m:
            total = m * (x-1) - (money-case[i])
            a+=(total if total>0 else 0)
            x,money=0,0
            m = case[i]
    a+=(m*x-money)
    print(f"#{t} {a}")


