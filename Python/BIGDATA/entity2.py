import pandas as pd
from koalanlp.Util import initialize, finalize
from koalanlp.proc import RoleLabeler
from koalanlp import API
import requests

# 분석할 데이터 파일
file_path = 'D://practice/yuna/'
# 분석 대상 파일
start_file = 'preprocess_chungbuk.csv'
# 저장할 데이터 파일
final_file = 'local_extraction_chungbuk.csv'

API_KEY = '9e76c797-dafc-42ef-8f3b-4daf41a7e30d'

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
    labeler = RoleLabeler(API.ETRI, etri_key=API_KEY)
    local_info = []
    not_local_info = []
    for i in range(len(df['내용'])):
        local_info.append([])
        not_local_info.append([])
        text = ''.join(df['내용'][i])
        sentences = labeler(text)
        for sent in sentences:
            a, b = [], []
            entities = sent.getEntities()
            if len(entities) > 0:
                for evb in entities:
                    a.append(evb.getSurface()) if evb.getFineLabel() in all_local else b.append(evb.getSurface())
            local_info[i].append(' '.join(a))
            not_local_info[i].append(' '.join(b))
    finalize()
    return local_info, not_local_info


# 원본 데이터와 추출한 데이터 합치기
def data_sum(df, local_info, not_local_info):
    ndf = df.assign(지역키워드=local_info, 지역제외=not_local_info)
    print(ndf.head(5))
    ndf.to_csv(file_path + final_file, encoding='cp949')


# 추출된 키워드 좌표 반환(테스트x)
def location_extraction(local):
    url = "http://api.vworld.kr/req/search?service=search&request=search&version=2.0$category=0501,0502&crs=EPSG:4326&&size=10&" \
          "page=1&query={}&type=place&format=json&errorformat=json&key=437C7816-F207-304B-B849-6CB92EB8B720".format(
        local)
    data = requests.get(url).json()['response']['result']['items']
    print(data)
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
    # 좌표반환
    location_extraction(li)
