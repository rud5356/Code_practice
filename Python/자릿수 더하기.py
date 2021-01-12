import sys
sys.stdin = open("input (2).txt", "r")

T = int(input())
T1 = int(T/1000)
T2 = int((T%1000)/100)
T3 = int((T%100)/10)
T4 = int(T%10)

result = T1+T2+T3+T4
print(result)