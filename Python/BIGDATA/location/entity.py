import pandas as pd
from koalanlp.Util import initialize, finalize
from koalanlp.proc import RoleLabeler
from koalanlp import API
import requests
import csv

file_path = 'D://practice/yuna/'
final_file = 'tokenized_data_chungbuk_v2.csv'

total_data = pd.read_csv(file_path + final_file, names=['content', 'content_type'], encoding='cp949')
API_KEY = '9e76c797-dafc-42ef-8f3b-4daf41a7e30d'

initialize(ETRI='LATEST')
labeler = RoleLabeler(API.ETRI, etri_key=API_KEY)
LC = ['LC_OTHERS', 'LCP_COUNTRY', 'LCP_PROVINCE', 'LCP_COUNTY', 'LCP_CITY', 'LCP_CAPITALCITY', 'LCG_RIVER', 'LCG_OCEAN',
      'LCG_BAY', 'LCG_MOUNTAIN', 'LCG_ISLAND', 'LCG_CONTINENT', 'LC_TOUR', 'LC_SPACE']
OG = ['OG_OTHERS', 'OGG_ECONOMY', 'OGG_EDUCATION', 'OGG_MILITARY', 'OGG_MEDIA', 'OGG_SPORTS', 'OGG_ART', 'OGG_MEDICINE',
      'OGG_RELIGION', 'OGG_SCIENCE', 'OGG_LIBRARY', 'OGG_LAW', 'OGG_POLITICS', 'OGG_FOOD', 'OGG_HOTEL']
AF = ['AF_ROAD', 'AF_BUILDING']

all_local = LC + OG + AF
for i in total_data['content']:
    local_info = []
    try:
        ori = i.split(' ')
    except:
        ori = i
    try:
        text = ''.join(i)
    except:
        text = ' '
    sentences = labeler(text)
    for sent in sentences:
        entities = sent.getEntities()
        if len(entities) > 0:
            for entity in entities:
                # print(entity)
                if entity.getFineLabel() in all_local:
                    for j in ori:
                        if entity.getSurface() in j:
                            local_info.append(j)
        #print(local_info)
        with open(file_path + 'point_chungbuk_v3.csv', 'a', newline='', encoding='cp949') as f:
            writer = csv.DictWriter(f, fieldnames=['지역명', 'x', 'y', 'TorF'])
            if len(local_info)>0:
                try:
                    url = "http://api.vworld.kr/req/search?service=search&request=search&version=2.0$category=0501,0502&crs=EPSG:4326&&size=10&" \
                          "page=1&query={}&type=place&format=json&errorformat=json&key=437C7816-F207-304B-B849-6CB92EB8B720".format(
                        local_info[-1])
                    data = requests.get(url).json()['response']['result']['items'][0]['point']
                    writer.writerow({'지역명': local_info[-1], 'x': data['x'], 'y': data['y'], 'TorF': 1})
                except:
                    writer.writerow({'지역명': local_info[-1], 'x': 0, 'y': 0, 'TorF': 0})
            else:
                writer.writerow({'지역명': ' ', 'x': 0, 'y': 0, 'TorF': 0})
finalize()
