import sys

sys.stdin = open("input369.txt", "r")

T = int(input())
a = []
for i in range(1, T + 1):
    num = str(i)
    a.append('-' * (num.count('3')+num.count('6')+num.count('9')) if '3' in num or '6' in num or '9' in num else num)
print(' '.join(a))

