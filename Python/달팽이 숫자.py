import sys

sys.stdin = open("input_달팽이.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    test = int(input())
    print("#{}".format(test_case))
    a = [[0 for j in range(test)] for i in range(test)]
    x, row, col, sw = 1, 0, -1, 0
    while test > 0:
        for i in range(sw, test):
            col += 1
            a[row][col] = x
            x += 1
        sw += 1
        test = test - 1
        for j in range(sw, test + 1):
            row += 1
            a[row][col] = x
            x += 1
        for y in range(test + 1, sw, -1):
            col -= 1
            a[row][col] = x
            x += 1
        sw += 1
        for z in range(test + 1, sw, -1):
            row -= 1
            a[row][col] = x
            x += 1
        sw -= 1
    for i in a:
        for j in i:
            print(j, end=" ")
        print()
