from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import datetime

path = "C://Users/rud53/anaconda3/Lib/site-packages/chromedriver_autoinstaller/88/chromedriver.exe"
page = ['A04', 'A01', 'A02', 'A03', 'A05', 'A06']
pageName = ['accident', 'trafficJam', 'construction', 'event', 'weather', 'etc']
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
file_path='D://practice/4/{}.csv'
month = ''
while (True):
    for i in range(len(page)):
        driver = webdriver.Chrome(path, options=options)
        f1 = open(file_path.format(pageName[i]+month), 'r', encoding='cp949')
        line = f1.readlines()
        lines = list(map(lambda s: s.strip(), line))
        line = [v for v in lines if v]
        if line != '\n':
            line = line[-1].split(",", 4)
        f1 = open(file_path.format(pageName[i]+month), 'a', encoding='cp949', newline="\n")
        csvWriter = csv.writer(f1)
        try:
            driver.get(
                'http://www.tbn.or.kr/traffic/tr_accident.tbn?page_code=0&BOARD_ID=T006&nowUrl=%2Ftraffic%2Ftr_accident.tbn&traffic_type={}'.format(
                    page[i]))
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            cl = soup.find('div', class_="box").get_text().split("\n")
            cllist = list(filter(None, cl))
            line[4] = line[4].replace("\"", "")
            if line != cllist:
                csvWriter.writerow(cllist)
        except:
            print(pageName[i] + " except발생 ")
            print(datetime.datetime.now())
            print("홈페이지 확인 요망")
        f1.close()
        driver.close()
