import sys
sys.stdin = open("greedy_exam_sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    result = list(map(int, input().split(" ")))
    number1 = int(result[0])
    number2 = int(result[1])
    k = 0

    if number1!=1:
        while number1:
            if number1 % number2 != 0:
                number1 -= 1
                k += 1
            else:
                number1 = int(number1 / number2)
                k += 1
            if number1==1 :
                break
    print("#{} {}".format(test_case, k))

