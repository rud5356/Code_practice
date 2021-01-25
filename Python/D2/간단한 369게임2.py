import sys

sys.stdin = open("input369.txt", "r")

T = int(input())
a = []
x = 1
for i in range(1, T + 1):
    if str(i) == str(3*x):
        a.append('-' * len(str(i)))
        x+=1
    else :
        a.append('-' * len(str(i)))
print(' '.join(a))

