import csv
import os

os.chdir("D://practice/4/")

pageName = ['accident', 'trafficJam', 'construction', 'event', 'weather', 'etc']

file_unity = open('b.csv', 'w', encoding='cp949',newline='')
wcsv = csv.writer(file_unity)

count = 0

for category_element in pageName:
    file = open(category_element + '.csv', 'r', encoding='cp949')
    line = csv.reader(file)
    try:
        for line_text in line:
            wcsv.writerow([line_text[0], line_text[1], line_text[2], line_text[3], line_text[4]])
    except:
        pass

