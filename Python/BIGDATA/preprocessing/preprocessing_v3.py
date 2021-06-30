from konlpy.tag import *
from tqdm import tqdm
import re
import pandas as pd
import numpy as np

file_path = 'D://practice/yuna/'
# 입력 데이터 파일
start_file = 'event_merge.csv'
# 고속도로제거 파일
highway_remove = 'highway_remove_message_v2.csv'
# 마지막 저장되는 파일
final_file = 'preprocess_event_merge.csv'


# 노이즈제거
def clean_text(text):
    text = text.replace(".", " ").strip()
    # 한글, 영어, 숫자만 남긴다.
    pattern = '[^ ㄱ-ㅣ가-힣|0-9|a-zA-Z]+'
    text = re.sub(pattern=pattern, repl=' ', string=text)
    return text


# 고속도로 데이터 제거
def remove_highway(data):
    data['내용'] = data['내용'].apply(clean_text)
    dataResult = data[~data['내용'].str.contains("나들목|고속도로|분기점", na=False, case=False)]
    return dataResult


# 불용어 제거
def get_nouns(tokenizer, sentence):
    stop_words = "한국도로공사 긴급 최초 TBN 경인교통방송 안 중 "
    stop_words = stop_words.split(' ')
    # 명사 추출
    nouns = tokenizer.nouns(sentence)
    # 불용어 제거
    nouns = list(filter(lambda w: True if w not in stop_words else '', nouns))
    noun = []
    for i in nouns:
        if len(i) > 2:
            noun.append(i)
    return noun


# 토큰화, 노이즈, 불용어제거
def tokenize(df):
    tokenizer = Kkma()
    prd_data = []
    for sent in tqdm(df['내용']):
        # 노이즈제거
        sentence = clean_text(sent.replace('\n', '').strip())
        # 불용어 제거, 명사 추출
        prd_data.append(' '.join(get_nouns(tokenizer, sentence)))
    return prd_data


# 저장 함수
def save_data(df, path, file):
    df.to_csv(path + file, encoding='cp949', index=False)


def preprocess():
    # 도로교통 데이터 읽기
    df = pd.read_csv(file_path + start_file, names=['지역', 'ID', '날짜', '형태', '내용'], header=0, encoding='cp949')
    df1 = df.dropna()
    # 고속도로 데이터를 제거
    df_v2 = remove_highway(df1)
    # 고속도로 데이터 제거 파일 저장
    save_data(df_v2, file_path, highway_remove)
    # 토큰화
    processed_data = tokenize(df_v2)
    df_v3 = pd.DataFrame(
        {'지역': df_v2['지역'], 'ID': df_v2['ID'], '날짜': df_v2['날짜'], '내용': processed_data, '형태': df_v2['형태']})
    # Null 제거
    df_v3.replace('', np.nan, inplace=True)
    df_V4 = df_v3.dropna()
    # 날짜순 정렬
    df_finished = df_V4.sort_values(by='날짜').reset_index(drop=True)
    # 토큰 분리한 데이터를 저장
    save_data(df_finished, file_path, final_file)


if __name__ == '__main__':
    preprocess()
