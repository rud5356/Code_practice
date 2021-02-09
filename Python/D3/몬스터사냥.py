import sys
sys.stdin = open("D:/Code_practice/Python/D3/input_몬스터사냥.txt", "r")

def dmg(D,L,N):
    dam = D + D*L*N*0.01
    return int(dam)

for t in range(1, int(input())+ 1):
    D,L,N=map(int,input().split())
    s = 0
    for i in range(N): s+=dmg(D,L,i)
    print(f"#{t} {s}")
