import sys
sys.stdin = open("D:/Code_practice/Python/D2/input_백만장자프로젝트.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    case = list(map(int,input().split()))
    money = 0
    result = case[-1]*(n-1)
    a=[]
    while n<len(case):
        for i in case[::-1]:
            if i>result:
                continue
            money+=i
        total = case[n-1]*(n-1)
        print(money,total)
        if total-money<0:
            a.append(0)
        else:
            a.append(total-money)
        money=0
        n-=1
    #if case[n-i-1]*(n-1)-money>0:
    #    result = case[n-i-1]-money
    print(a)
    #print(result)

