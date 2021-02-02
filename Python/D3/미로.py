import sys
sys.stdin = open("D:/Code_practice/Python/D3/input_미로.txt", "r")

dx=[0,1,0,-1]
dy=[1,0,-1,0]

#dfs함수 구현
def DFS(x,y,s):
    global val
    #s+=graph[x][y] # 행렬 값을 더함
    if val == 3 : return 1  #전체 더한 값이 최소합보다 크면 종료
    # 행렬 끝까지 갔다면 합을 최소합으로 지정 후 종료
    if y==(size-1) and x==(size-1) :
        min = s
        return
    # dx의 크기만큼 돌면서 오른쪽으로 이동하다가 막히면 아래쪽으로 이동.
    for i in range(len(dx)):
        nextx = x+dx[i]
        nexty = y+dy[i]
        if graph[nextx][nexty] == 0:
            DFS(nextx, nexty, s)

for i in range(1,int(input())+1):
    size = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    val = 0
    DFS(0,0,0)
    print(f"#{i} {min}")
