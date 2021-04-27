import sys
sys.stdin = open("D:/Code_practice/Python/D2/date_calculator.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    m1,d1,m2,d2=map(int,input().split()) #map 함수를 통해 각각의 변수에 대입
    day=[31,28,31,30,31,30,31,31,30,31,30,31] # 월별 날짜 수 배열로 입력
    result=sum(list([day[i-1] for i in range(m1,m2)]))+d2-d1+1 #해당 월의 날짜 수를 더하고 첫 달의 지난 날을 빼고 마지막 달의 지난 날을 더한 후 당일 1일 더하기
    print(f"#{test_case} {result}")
