import sys
sys.stdin = open("D:/Code_practice/Python/D3/input_미로.txt", "r")

deg = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_wall(r, c):
  if r<0 or r>= 100 or c<0 or c>= 100:
      return True
  return False

def bfs(start, end):
  Q.append(start)
  cnt = 0
  er, ec = end
  while Q:
      now = Q.pop(0)
      nr, nc = now
      maze[nr][nc] = 9

      for dr, dc in deg:
          tr, tc = nr + dr, nc + dc
          if tr == er and tc == ec:
              return 1
          if not is_wall(tr, tc) and not maze[tr][tc]:
              Q.append([tr, tc])
  return 0



for tc in range(10):
  case_num = int(input())
  maze = []
  start, end = [], []
  for i in range(100):
      tmp = []
      cnt = 0
      for j in input():
          tmp.append(int(j))
          if int(j) == 2:
              start = [i, cnt]
          if int(j) == 3:
              end = [i, cnt]
          cnt += 1
      maze.append(tmp)

  Q = []

  print(f"#{tc + 1} {bfs(start, end)}")