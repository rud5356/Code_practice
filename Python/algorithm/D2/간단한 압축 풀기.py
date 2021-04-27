import sys
sys.stdin = open("D:/Code_practice/Python/D2/input_간단한압축풀기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    lines = int(input()) #라인 개수 입력
    a = ""
    for line in range(0,lines): #각 라인의 단어와 개수를 입력받아 문자열에 저장
        word,cnt = map(str,input().strip().split())
        a+=word*int(cnt)
    print(f"#{test_case}")
    for i in range(1,len(a)+1) : #10번째 문자 출력후 줄바꿈 처리
        print(a[i-1], end = "\n" if i%10 == 0 else '')
    print()
