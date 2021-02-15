import sys
sys.stdin = open("D:/Code_practice/Python/D3/input_오목.txt", "r")
T=int(input())

def judge(test):
    t_len = len(test)
    for i in range(t_len):
        if test[i] in '.':
            return "NO"
        else:
            for j in range(t_len):
                if test[i][j] in '.':
                    return "NO"
    for i in range(t_len):
        if test[0][i] =='o':
            for j in range(t_len):
                if test[0+j][i+j]!='o':
                    return "NO"
                elif test[0-j][i-j]!='o':
                    return "NO"


for t in range(1, 2):
    test=[]
    for i in range(int(input())):
        test.append(list(map(str,input().split())))
    judge(test)
