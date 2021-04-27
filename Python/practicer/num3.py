from selenium import webdriver
import csv
import datetime
import time

path = "C://Users/rud53/anaconda3/Lib/site-packages/chromedriver_autoinstaller/88/chromedriver.exe"
pageName = ['message']
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
file_path='D://practice/4/message.csv'
month = ''
while (True):
    driver = webdriver.Chrome(path, options=options)
    try:
        f2 = open(file_path, 'r', encoding='cp949')
        line = f2.readlines()
        lines = list(map(lambda s: s.strip(), line))
        line = [v for v in lines if v]
        if line != '\n':
            line = line[-1].split(",", 4)
    except:
        pass
    f1 = open(file_path, 'a', encoding='cp949', newline="\n")
    csvWriter = csv.writer(f1)
    try:
        driver.get('https://www.tbn.or.kr/traffic/tr_textinfo.tbn?BOARD_ID=T005&area_code=12')
        table = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[3]/table/tbody')
        rows = table.find_element_by_tag_name("tr")
        result = rows.text.split(" ",4)
        if line[-1].find("\""):
            line[-1] = line[-1].replace("\"", "")
        if line != result:
            csvWriter.writerow(result)
    except :
        print(datetime.datetime.now())
        print('error')
    time.sleep(10)
    f1.close()
    driver.close()
    # print(result)


