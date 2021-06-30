import pandas as pd
from koalanlp.Util import initialize, finalize
from koalanlp.proc import RoleLabeler
from koalanlp import API
import requests
import operator

API_KEY_1 = '9e76c797-dafc-42ef-8f3b-4daf41a7e30d'
API_KEY_2 = '073e4221-4be7-4c3e-90cc-06f98876de6c'
API_KEY_3 = '74f15b44-b9fd-4867-aba7-0bdb46be6b28'
API_KEY_4 = 'daa00bed-0891-4397-9e5c-074bcc335be1'
API_KEY_5 = '053a8578-919c-4e09-b5bb-bf6ebf8d1916'
API_KEY_6 = '48018cce-69c8-4e55-aefe-fae8eabe63f0'
apiKey = [API_KEY_1, API_KEY_2, API_KEY_3, API_KEY_4, API_KEY_5, API_KEY_6]
# 지역명 개체명 키워드들(location, organization, artifacts)
LC = ['LC_OTHERS', 'LCP_COUNTRY', 'LCP_PROVINCE', 'LCP_COUNTY', 'LCP_CITY', 'LCP_CAPITALCITY', 'LCG_RIVER', 'LCG_OCEAN',
      'LCG_BAY', 'LCG_MOUNTAIN', 'LCG_ISLAND', 'LCG_CONTINENT', 'LC_TOUR', 'LC_SPACE']
OG = ['OG_OTHERS', 'OGG_ECONOMY', 'OGG_EDUCATION', 'OGG_MILITARY', 'OGG_MEDIA', 'OGG_SPORTS', 'OGG_ART', 'OGG_MEDICINE',
      'OGG_RELIGION', 'OGG_SCIENCE', 'OGG_LIBRARY', 'OGG_LAW', 'OGG_POLITICS', 'OGG_FOOD', 'OGG_HOTEL']
AF = ['AF_ROAD', 'AF_BUILDING']
all_local = LC + OG + AF


# 개체명 추출해서 지역명관련된 키워드 추출하기
def entity(df, api, local_info_df):
    try:
        initialize(ETRI='LATEST')
        labeler = RoleLabeler(API.ETRI, etri_key=api)
        local_info = []
        x = 0
        # 한줄씩 분석 실행
        for i in df['내용']:
            local_info.append([])
            text = ''.join(i)
            sentences = labeler(text)
            # 개체명 태그 부여
            for sent in sentences:
                entities = sent.getEntities()
                # 부여된 태그가 있을 경우
                if len(entities) > 0:
                    for evb in entities:
                        # 태그가 지역명과 관련이 있을 경우
                        if evb.getFineLabel() in all_local:
                            local_info[x].append(f"{evb.getSurface()}:{evb.label}")
            x += 1
        local_info_df = pd.DataFrame(local_info)
        finalize()
    except:
        print("error")
    return local_info_df


# 저장 함수
def save_data(data, path, file):
    data.to_csv(path + file, encoding='cp949', index=False)


def location_clouding(local_df):
    a = []
    tag = {"OG": 1, "LC": 2, "AF": 3}
    # 딕셔너리 형태로 저장
    address_ori = []
    # 딕셔너리 value값만 저장
    address_upg = []
    for i in range(len(local_df)):
        local_tag = {}
        # nan을 빈 공백으로 변경
        locals = list(local_df.loc[i].fillna(""))
        # 빈 공백 제거
        locals = list(filter(bool, locals))
        if not locals:
            local_tag['empty'] = 'empty'
        else:
            s_address = {}
            num = 0
            nowTag = ''
            # print(locals)
            for z in locals:
                fir, sec = z.split(':')
                fir = fir.split(' ')
                if len(fir) >= 2:
                    fir = fir[-1]
                fir = ''.join(fir)
                local_tag[fir]=sec
            local_tag = sorted(local_tag.items(), reverse=True, key=operator.itemgetter(1))
            # print(local_tag)
            for j in local_tag:
                address_upg.append([])
                fir = j[0]
                sec = j[1]
                url = "http://api.vworld.kr/req/search?service=search&request=search&version=2.0$category=0501,0502&crs=EPSG:4326&&size=10&" \
                      "page=1&query={}&type=place&format=json&errorformat=json&key=437C7816-F207-304B-B849-6CB92EB8B720".format(fir)
                try:
                    data = requests.get(url).json()['response']['result']['items']
                    for s in range(len(data)):
                        # 시이름 제외
                        if fir[-1] != "시":
                            ad = data[s]['address']['road'].split(' ')
                            ad = ' '.join(ad[:2])
                            if s == 0:
                                s_address[fir] = ad
                                nowTag = sec
                            else:
                                if ad not in s_address.values() and ad != '':
                                    nowTag=sec
                                    s_address[fir] = ad
                except:
                    s_address[fir] = ''
            address_ori.append(s_address)
            address_upg.append(s_address.values())
    return address_upg


def extractionProgress(a, b):
    local_info_df = pd.DataFrame()
    # 파일 읽기
    df = pd.read_csv(file_path + start_file, encoding='cp949')
    # 합칠 데이터프레임 생성
    df2 = pd.read_csv(file_path + entity_file, header=None, skiprows=[0], encoding='cp949')
    # 지역명 키워드 추출
    for i in range(len(apiKey)):
        print(f"{i}번째 시작")
        df3 = df[b+a*i:b+a*(i+1)]
        li = entity(df3, apiKey[i], local_info_df)
        df2 = pd.concat([df2, li])
    save_data(df2, file_path, entity_file)


def addressProgress():
    # 주소추출
    df_lo = pd.read_csv(file_path + entity_file, encoding='cp949')
    local = location_clouding(df_lo)
    local_data = pd.DataFrame(local)
    save_data(local_data, file_path, local_path)


if __name__ == '__main__':
    # 분석할 데이터 파일
    file_path = 'D://practice/yuna/'
    # 분석 대상 파일
    start_file = 'preprocess_event_merge.csv'
    # 저장할 데이터 파일
    entity_file = 'local_extraction_v6.csv'
    # 위치 데이터 파일
    local_path = 'local_cloud_v4.csv'

    # 하나의 api 마다 읽을 행 개수
    num = 1000
    # 기존 파일에 존재하는 행 개수
    already_row_num = 5600
    # 지역 키워드 추출 함수 실행
    extractionProgress(num, already_row_num)
    # 행정구역 추출 함수 실행(완벽하지 않음)
    # addressProgress()