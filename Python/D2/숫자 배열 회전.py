import sys
import copy
sys.stdin = open("D:/Code_practice/Python/D2/input_숫자배열회전.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    lines = int(input())
    a,result = [],[]
    # lines만큼 input 받아 배열로 저장
    for i in range(lines):
        a.append(list(map(str, input().split())))
    #90도 회전시 (0,0)->(2,0),(0,1)->(1,0),(0,2)->(2,0)... 처럼 나타나는 패턴별로 각 행별 input
    for n in range(0,lines):
        row1,row2,row3 = [], [], []
        for m in range(0,lines):
            row1.append(str(a[lines-1-m][n]))
            row2.append(str(a[lines-1-n][lines-1-m]))
            row3.append(str(a[m][lines-1-n]))
        #각 행을 한줄로 배열에 저장
        result += [''.join(row1),''.join(row2),''.join(row3)]
    print(f"#{test_case}")
    #3번 출력시 다음 줄로 넘어가도록 출력
    for x in range(0,len(result)):
        print(result[x],end="\n" if (x+1)%3==0 and x>=2 else ' ')
