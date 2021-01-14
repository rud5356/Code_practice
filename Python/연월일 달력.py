import sys
sys.stdin = open("input (3).txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    result = list(map(str, input().split()))
    result = ''.join(result)
    year = int(result[0:4])
    month = int(result[4:6])
    day = int(result[6:8])
    if 1 > month or month > 12:
        print("#{} {}".format(test_case, "-1"))
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 0 or day > 31:
            print("#{} {}".format(test_case, "-1"))
        else :
            print("#{}".format(test_case) + " {0:04d}".format(year) + "/{0:02d}".format(month) + "/{0:02d}".format(day))
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 0 or day > 30:
            print("#{} {}".format(test_case, "-1"))
        else :
            print("#{}".format(test_case) + " {0:04d}".format(year) + "/{0:02d}".format(month) + "/{0:02d}".format(day))
    elif month == 2:
        if day <= 0 or day > 28:
            print("#{} {}".format(test_case, "-1"))
        else :
            print("#{}".format(test_case) + " {0:04d}".format(year) + "/{0:02d}".format(month) + "/{0:02d}".format(day))

