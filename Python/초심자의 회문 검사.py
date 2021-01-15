import sys
sys.stdin = open("input (7).txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    test = list(map(str, input().split()))
    test = ('').join(test)
    a = 0
    for i in range(0,int(len(test)/2)) :
        a = (lambda x : 1 if x[i] == x[len(x)-1-i] else 0)(test)
        #if test[i] == test[len(test)-1-i] :
        #    a = 1
        #else :
        #    a = 0
    print("#{} {}".format(test_case,a))
