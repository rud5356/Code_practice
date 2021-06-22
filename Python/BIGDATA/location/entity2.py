import pandas as pd
from koalanlp.Util import initialize, finalize
from koalanlp.proc import RoleLabeler
from koalanlp import API
import requests

# 분석할 데이터 파일
file_path = 'D://practice/yuna/'
# 분석 대상 파일
start_file = 'preprocess2.csv'
# 저장할 데이터 파일
final_file = 'local_extraction_v3_1.csv'
final_file_1 = 'local_extraction_v4_2.csv'

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
def entity(df, api):
    try:
        initialize(ETRI='LATEST')
        labeler = RoleLabeler(API.ETRI, etri_key=api)
        local_info = []
        x = 0
        for i in df['내용']:
            local_info.append([])
            text = ''.join(i)
            sentences = labeler(text)
            for sent in sentences:
                entities = sent.getEntities()
                if len(entities) > 0:
                    for evb in entities:
                        if evb.getFineLabel() in all_local:
                            local_info[x].append(evb.getSurface())
            x += 1
        finalize()
    except:
        print("error")
    return local_info


# 원본 데이터와 추출한 데이터 합치기
def data_sum(local_info):
    ndf_1 = pd.DataFrame(local_info)
    # print(ndf_1.head(10))
    ndf_1.to_csv(file_path + final_file_1, index=False, encoding='cp949')


# 추출된 키워드 좌표 반환(테스트x)
def location_extraction(local):
    a = ''
    b = []
    c = []
    for i in local:
        if i is not a:
            locals = i.split(' ')
            for j in locals:
                url = "http://api.vworld.kr/req/search?service=search&request=search&version=2.0$category=0501,0502&crs=EPSG:4326&&size=10&" \
                      "page=1&query={}&type=place&format=json&errorformat=json&key=437C7816-F207-304B-B849-6CB92EB8B720".format(
                    j)
                try:
                    con1, con2 = '', ''
                    data = requests.get(url).json()['response']['result']['items']
                    e = []
                    for s in range(len(data)):
                        lo = data[s]['address']['road']
                        e.append(lo)
                    d = ''
                    for q in range(1, len(e)):
                        lo1 = e[q].split(' ')
                        lo2 = e[q - 1].split(' ')
                        if lo1[:2] == lo2[:2]:
                            print('same')
                            print(lo1, lo2)
                            if len(lo1) >= len(lo2) and len(lo1) > len(d):
                                d = lo1
                            elif len(lo1) < len(lo2) and len(lo2) > len(d):
                                d = lo2
                            else:
                                d = d
                        elif lo1[:2] != lo2[:2]:
                            print('different')
                            print(lo1, lo2)
                            for h in lo1:
                                if '로' in h:
                                    con1 = h
                            for f in lo2:
                                if '로' in f:
                                    con2 = f
                            url2 = "https://openapi.its.go.kr:9443/trafficInfo?apiKey=b5078e7bec8f4d8d88c9671aef9700ab" \
                                   "&type=all&routeNo={" \
                                   "}&minX=126.800000&maxX=127.890000&minY=34.900000&maxY=35.100000&getType=json" \
                                   "".format('1030045500')
                            url3 = "https://openapi.its.go.kr:9443/trafficInfo?apiKey=b5078e7bec8f4d8d88c9671aef9700ab" \
                                   "&type=all&routeNo={" \
                                   "}&minX=126.800000&maxX=127.890000&minY=34.900000&maxY=35.100000&getType=json" \
                                   "".format(con2)
                            data2 = requests.get(url2).json()['body']['items']
                            data3 = requests.get(url3).json()['body']['items']
                            # print(con1, con2)
                            for z in range(len(data2)):
                                # print(data2[z]['roadName'])
                                # print(data2)
                                if data2[z]['roadName'] == con1:
                                    # print(data2[z]['speed'])
                                    d = lo2 if int(data2) > int(data3) else lo1
                            # print("data2=" + data2)
                        print(d)
                    b.append(d)
                except:
                    b.append('')
            c.append(b)
            # print(c)
            # print('====================================')
    return c


def location_clouding(local_df):
    a = []
    address_ori = []
    address_upg = []
    # 시or도가 다르게 나오면 어떻게 처리할 것인가.

    for i in range(len(local_df)):
        locals = list(local_df.loc[i].fillna(""))
        locals = ' '.join(locals).split()
        if locals is not a:
            s_address = {}
            for j in locals:
                url = "http://api.vworld.kr/req/search?service=search&request=search&version=2.0$category=0501,0502&crs=EPSG:4326&&size=10&" \
                      "page=1&query={}&type=place&format=json&errorformat=json&key=437C7816-F207-304B-B849-6CB92EB8B720".format(
                    j)
                try:
                    data = requests.get(url).json()['response']['result']['items']
                    for s in range(len(data)):
                        if j[-1] != "시":
                            ad = data[s]['address']['road'].split(' ')
                            ad = ' '.join(ad[:2])
                            if s == 0:
                                s_address[j]=ad
                            else:
                                if ad not in s_address.values() and ad != '':
                                    s_address[j]=ad
                except:
                    print(j)
            address_ori.append(s_address)
            address_upg.append(', '.join(s_address.values()))
    return address_upg


if __name__ == '__main__':
    num = 500
    # 파일 읽기
    df = pd.read_csv(file_path + start_file, encoding='cp949')
    # 인덱스 제거
    df2 = df.loc[:, ['지역', 'ID', '날짜', '내용', '형태']]
    df3 = df2[num:num+500]
    # 지역명 키워드 추출
    li = entity(df3,API_KEY_1)
    # 원본데이터와 합침
    data_sum(li)
    # 주소추출
    df_lo = pd.read_csv(file_path + final_file_1, encoding='cp949')
    # local_df = li
    local = location_clouding(df_lo)
    # print(local)
    local_cloud_df = pd.DataFrame(local)
    local_cloud_df.to_csv(file_path + "local_cloud.csv", encoding='cp949')
    # 좌표반환
    # location_extraction(df['지역키워드'].fillna(""))
