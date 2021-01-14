import sys
sys.stdin = open("input (4).txt", "r")

T = str(input())
result = ''
for s in T :
    result = result + str(int(ord(s))-64)+' '

print(result)