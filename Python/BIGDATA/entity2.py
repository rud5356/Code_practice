import pandas as pd
from koalanlp.Util import initialize, finalize
from koalanlp.proc import RoleLabeler
from koalanlp import API
import requests
import numpy as np

# 분석할 데이터 파일
file_path = 'D://practice/yuna/'
# 분석 대상 파일
start_file = 'preprocess_chungbuk.csv'
# 저장할 데이터 파일
final_file = 'local_extraction_chungbuk_v2.csv'

API_KEY_1 = '9e76c797-dafc-42ef-8f3b-4daf41a7e30d'
API_KEY_2 = '073e4221-4be7-4c3e-90cc-06f98876de6c'
API_KEY_3 = '74f15b44-b9fd-4867-aba7-0bdb46be6b28'
API_KEY_4 = 'daa00bed-0891-4397-9e5c-074bcc335be1'

# 지역명 개체명 키워드들(location, organization, artifacts)
LC = ['LC_OTHERS', 'LCP_COUNTRY', 'LCP_PROVINCE', 'LCP_COUNTY', 'LCP_CITY', 'LCP_CAPITALCITY', 'LCG_RIVER', 'LCG_OCEAN',
      'LCG_BAY', 'LCG_MOUNTAIN', 'LCG_ISLAND', 'LCG_CONTINENT', 'LC_TOUR', 'LC_SPACE']
OG = ['OG_OTHERS', 'OGG_ECONOMY', 'OGG_EDUCATION', 'OGG_MILITARY', 'OGG_MEDIA', 'OGG_SPORTS', 'OGG_ART', 'OGG_MEDICINE',
      'OGG_RELIGION', 'OGG_SCIENCE', 'OGG_LIBRARY', 'OGG_LAW', 'OGG_POLITICS', 'OGG_FOOD', 'OGG_HOTEL']
AF = ['AF_ROAD', 'AF_BUILDING']

all_local = LC + OG + AF


# 개체명 추출해서 지역명관련된 키워드 추출하기
def entity(df):
    initialize(ETRI='LATEST')
    labeler = RoleLabeler(API.ETRI, etri_key=API_KEY_2)
    local_info = []
    not_local_info = []
    #for i in range(0,10):
    for i in range(len(df['내용'])):
        text = ''.join(df['내용'][i])
        sentences = labeler(text)
        for sent in sentences:
            a, b = [], []
            entities = sent.getEntities()
            if len(entities) > 0:
                for evb in entities:
                    a.append(evb.getFineLabel()) if evb.getFineLabel() in all_local else b.append(evb.getFineLabel())
            local_info.append(" ".join(a))
            #not_local_info.append(" ".join(b))
    finalize()
    return local_info, not_local_info


# 원본 데이터와 추출한 데이터 합치기
def data_sum(df, local_info, not_local_info):
    #ndf = df.assign(지역키워드=local_info, 지역제외=not_local_info)
    ndf = df.assign(지역키워드=local_info)
    ndf.to_csv(file_path + final_file, encoding='cp949')


# 추출된 키워드 좌표 반환(테스트x)
def location_extraction(local):
    a = ''
    for i in local:
        if i is not a:
            locals = i.split(' ')
            for j in locals:
                url = "http://api.vworld.kr/req/search?service=search&request=search&version=2.0$category=0501,0502&crs=EPSG:4326&&size=10&" \
                      "page=1&query={}&type=place&format=json&errorformat=json&key=437C7816-F207-304B-B849-6CB92EB8B720".format(
                    j)
                try:
                    data = requests.get(url).json()['response']['result']['items']
                    for s in range(len(data)):
                        print(data[s]['address']['road'])
                        print('------------------------------')
                    #print(data)
                except:
                    print(j)
            print('====================================')
    return data


def location_clouding(local_df):
    a = ''
    #시or도가 다르게 나오면 어떻게 처리할 것인가.

    for i in local_df:
        if i is not a:
            locals = i.split(' ')
            for j in locals:
                url = "http://api.vworld.kr/req/search?service=search&request=search&version=2.0$category=0501,0502&crs=EPSG:4326&&size=10&" \
                      "page=1&query={}&type=place&format=json&errorformat=json&key=437C7816-F207-304B-B849-6CB92EB8B720".format(
                    j)
                try:
                    data = requests.get(url).json()['response']['result']['items']
                    for s in range(len(data)):
                        print(data[s]['address']['road'])
                        print('------------------------------')
                    # print(data)
                except:
                    print(j)
            print('====================================')
    return data

if __name__ == '__main__':
    # 파일 읽기
    df = pd.read_csv(file_path + start_file, encoding='cp949')
    # 인덱스 제거
    df2 = df.loc[:, ['지역', 'ID', '날짜', '내용', '형태']]
    # 지역명 키워드 추출
    li, nli = entity(df2)
    # 원본데이터와 합침
    data_sum(df2, li, nli)
    # df = pd.read_csv(file_path+'local_extraction_chungbuk.csv',encoding='cp949')
    # local_df = df['지역키워드'].fillna("")

    # 좌표반환
    #location_extraction(df['지역키워드'].fillna(""))
