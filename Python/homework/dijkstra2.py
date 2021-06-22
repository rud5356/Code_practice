import heapq


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        # dist: 지금까지 온 거리, now: 현재 기준 시작 정점.
        dist, now_vertex = heapq.heappop(q)
        # 이미 방문한 정점인지 확인
        if distance[now_vertex] < dist:
            continue
        # 현재 정점을 거쳐가는게 거리가 더 짧을 경우 최단 거리 갱신
        for next_vertex, nextDist in graph[now_vertex]:
            cost = dist + nextDist
            if cost < distance[next_vertex]:
                distance[next_vertex] = cost
                lastTrace[next_vertex] = now_vertex
                heapq.heappush(q, (cost, next_vertex))
    return trace(start, end)


# 최단 경로 추적
def trace(start, end):
    res = [end]
    lastTrace[start] = 0
    while lastTrace[end]:
        res.append(lastTrace[end])
        end = lastTrace[end]
    return PrintResult(res[::-1])


# 출력 함수
def PrintResult(res):
    print("최단 거리 : ", distance[end], end=", ")
    print("최단 경로 : ", *res)


if __name__ == "__main__":
    # 그래프를 인접리스트로 구현
    graph = [[] for i in range(6)]
    graph[1].append((2, 7))
    graph[1].append((3, 4))
    graph[1].append((4, 6))
    graph[1].append((5, 1))
    graph[3].append((2, 2))
    graph[3].append((4, 5))
    graph[4].append((2, 3))
    graph[5].append((4, 1))

    INF = int(1e9)

    distance = [INF] * len(graph)
    lastTrace = [None] * len(graph)
    #시작 정점으로부터 모든 정점까지의 최단 경로와 거리 출력
    start = 1
    for end in range(1, len(graph)):
        dijkstra(start)
