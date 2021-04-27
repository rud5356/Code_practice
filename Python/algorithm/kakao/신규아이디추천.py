import sys

sys.stdin = open("D:/Code_practice/Python/kakao/input.txt", "r")


def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    n = ""
    for i in new_id:
        if i.isalnum() or i in '-_.':
            n += i
    # 3단계
    while '..' in n:
        n = n.replace('..', '.')
    # 4단계
    n = n[1:] if n[0] == '.' else n
    n = n[:-1] if len(n) > 1 and n[-1] == '.' else n
    # 5단계
    if n == "": n = "a"
    # 6단계
    n = n[0:15]
    n = n[:-1] if len(n) > 1 and n[-1] == '.' else n
    # 7단계
    if len(n) <= 2: n += n[-1] * (3 - len(n))
    return print(n)


for t in range(1, int(input()) + 1):
    solution(str(input().split()))
