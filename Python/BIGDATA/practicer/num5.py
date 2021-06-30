import csv
import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime
import pandas as pd
import schedule
import json
import urllib3

urllib3.disable_warnings()


def crowling():
    response = urllib.request.urlopen(get_url_its.format(api_key))
    file_name = f'D://practice/yuna/ITS/ITS_{today_1}_{today_2}.csv'
    json_object = json.load(response)
    result = json_object["body"]["items"]
    df = pd.json_normalize(result)
    df.to_csv(file_name, encoding='cp949')


def mes_crowling():
    req = requests.get(get_url_mes, verify=False)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    f2 = open(file_path_2, 'r', encoding='cp949')
    line = f2.readlines()
    lines = list(map(lambda s: s.strip(), line))
    line = [v for v in lines if v]
    # print(line[-3])
    if line != '\n':
        line = line[-1].split(",", 3)
    f1 = open(file_path_2, 'a', encoding='cp949', newline="\n")
    csvWriter = csv.writer(f1)
    try:
        columns = soup.find("tbody").find_all("td")
        columnlist = []
        for i in range(4):
            columnlist.append(columns[i].text)
        line[-1] = line[-1].replace('\"', '')
        # print(line, columnlist)
        if line != columnlist:
            csvWriter.writerow(columnlist)
            # print(columnlist)
    except:
        print(datetime.datetime.now())
        print('error')
    f1.close()


def other_crowling():
    for i in range(len(page)):
        f1 = open(file_path_1.format(today_1, pageName[i]), 'r', encoding='cp949')
        line = f1.readlines()
        lines = list(map(lambda s: s.strip(), line))
        line = [v for v in lines if v]
        if line != '\n':
            line = line[-1].split(",", 4)
        f1 = open(file_path_1.format(today_1, pageName[i]), 'a', encoding='cp949', newline="\n")
        csvWriter = csv.writer(f1)
        req = requests.get(get_url_others.format(page[i]), verify=False)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        try:
            cl = soup.find('div', class_="box").get_text().strip().split("\n")
            for c in range(len(cl)):
                cl[c] = cl[c].strip()
                cl[c] = cl[c].replace('\t', '')
                cl[c] = cl[c].replace('\r', '')
                if cl[c] == "<" or cl[c] == ">":
                    cl[c] = ""
            cl = [v for v in cl if v]
            cllist = list(filter(None, cl))
            # print(cllist)
            # print(line)
            line[4] = line[4].replace("\"", "")
            if line != cllist:
                csvWriter.writerow(cllist)
        except:
            print(pageName[i] + " except발생 ")
            print(datetime.datetime.now())
        f1.close()


if __name__ == '__main__':
    today_1 = datetime.datetime.today().month
    today_2 = datetime.datetime.today().day
    # 카테고리 별 상세 주소 값
    page = ['A04', 'A01', 'A02', 'A03', 'A05', 'A06']
    # 카테고리 별 이름
    pageName = ['accident', 'trafficJam', 'construction', 'event', 'weather', 'etc']
    # 저장할 경로
    file_path_1 = 'D://practice/{}/{}.csv'
    file_path_2 = f'D://practice/{today_1}/message.csv'
    # 도로 교통 api
    api_key = "529be81770b6430cbacf313407f0308d"
    # 각 홈페이지 주소
    get_url_mes = 'https://www.tbn.or.kr/traffic/tr_textinfo.tbn?BOARD_ID=T005&area_code=12'
    get_url_others = 'http://www.tbn.or.kr/traffic/tr_accident.tbn?page_code=0&BOARD_ID=T006&nowUrl=%2Ftraffic%2Ftr_accident.tbn&traffic_type={}'
    get_url_its = 'https://openapi.its.go.kr:9443/eventInfo?apiKey={}&type=its&eventType=all&minX=126.800000&maxX=127.890000&minY=34.900000&maxY=35.100000&getType=json'
    schedule.every().day.at("23:30").do(crowling)
    while (True):
        mes_crowling()
        other_crowling()
        try:
            schedule.run_pending()
        except:
            print('schedule오류')
