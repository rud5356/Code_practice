import sys
sys.stdin = open("D:/Code_practice/Python/D3/input_최소합.txt", "r")

# dx-->오른쪽 이동, dy --> 아래쪽 이동
dx=[0,1]
dy=[1,0]

#dfs함수 구현
def DFS(x,y,s):
    global min
    s+=graph[x][y] # 행렬 값을 더함
    if s > min: return #전체 더한 값이 최소합보다 크면 종료
    # 행렬 끝까지 갔다면 합을 최소합으로 지정 후 종료
    if y==(size-1) and x==(size-1) :
        min = s
        return
    # dx의 크기만큼 돌면서 오른쪽으로 이동하다가 막히면 아래쪽으로 이동.
    for i in range(len(dx)):
        nextx = x+dx[i]
        nexty = y+dy[i]
        if nextx < size and nexty < size:
            DFS(nextx, nexty, s)

for i in range(1,int(input())+1):
    size = int(input())
    graph = [list(map(int, input().split())) for _ in range(size)]
    min = 13*13*10+1    #전체 합의 최대값
    DFS(0,0,0)
    print(f"#{i} {min}")
