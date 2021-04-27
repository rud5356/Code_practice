from selenium import webdriver
import csv
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime
import pandas as pd
import schedule
import json

path = "C://Users/rud53/anaconda3/Lib/site-packages/chromedriver_autoinstaller/88/chromedriver.exe"
page = ['A04', 'A01', 'A02', 'A03', 'A05', 'A06']
pageName = ['accident', 'trafficJam', 'construction', 'event', 'weather', 'etc']
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
file_path_1 = 'D://practice/4/{}.csv'
file_path_2 = 'D://practice/4/message.csv'
api_key = "529be81770b6430cbacf313407f0308d"


def crowling():
    today_1 = datetime.datetime.today().month
    today_2 = datetime.datetime.today().day

    response = urllib.request.urlopen('https://openapi.its.go.kr:9443/eventInfo?apiKey={'
                                      '}&type=its&eventType=all&minX=126.800000&maxX=127.890000&minY=34.900000&maxY=35'
                                      '.100000&getType=json'.format(api_key))
    file_name = 'D://practice/yuna/ITS/ITS_{0}_{1}.csv'.format(today_1, today_2)

    json_object = json.load(response)
    result = json_object["body"]["items"]

    df = pd.json_normalize(result)
    df.to_csv(file_name, encoding='cp949')
    print(df)


schedule.every().day.at("23:30").do(crowling)


def mes_crowling():
    driver = webdriver.Chrome(path, options=options)
    try:
        f2 = open(file_path_2, 'r', encoding='cp949')
        line = f2.readlines()
        lines = list(map(lambda s: s.strip(), line))
        line = [v for v in lines if v]
        if line != '\n':
            line = line[-1].split(",", 4)
    except:
        pass
    f1 = open(file_path_2, 'a', encoding='cp949', newline="\n")
    csvWriter = csv.writer(f1)
    try:
        driver.get('https://www.tbn.or.kr/traffic/tr_textinfo.tbn?BOARD_ID=T005&area_code=12')
        table = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[3]/table/tbody')
        rows = table.find_element_by_tag_name("tr")
        result = rows.text.split(" ", 4)
        if line[-1].find("\""):
            line[-1] = line[-1].replace("\"", "")
        if line != result:
            csvWriter.writerow(result)
            print(result)
    except:
        print(datetime.datetime.now())
        print('error')
    f1.close()
    driver.close()


def other_crowling():
    for i in range(len(page)):
        driver = webdriver.Chrome(path, options=options)
        f1 = open(file_path_1.format(pageName[i]), 'r', encoding='cp949')
        line = f1.readlines()
        lines = list(map(lambda s: s.strip(), line))
        line = [v for v in lines if v]
        if line != '\n':
            line = line[-1].split(",", 4)
        f1 = open(file_path_1.format(pageName[i]), 'a', encoding='cp949', newline="\n")
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
                print(cllist)
            f1.close()
            driver.close()
        except:
            print(pageName[i] + " except발생 ")
            print(datetime.datetime.now())
            # print("홈페이지 확인 요망")
            f1.close()
            driver.close()


while (True):
    mes_crowling()
    other_crowling()
    schedule.run_pending()
