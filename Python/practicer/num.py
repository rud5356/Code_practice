import urllib.request
import datetime
import pandas as pd
import schedule
import json

api_key="529be81770b6430cbacf313407f0308d"
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


schedule.every().day.at("23:30").do(crowling)

while True:
    schedule.run_pending()
