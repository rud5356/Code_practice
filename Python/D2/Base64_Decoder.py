import sys
sys.stdin = open("D:/Code_practice/Python/D2/input_Base64Decoder.txt", "r")

from base64 import b64decode
T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case} {b64decode(input()).decode()}')
