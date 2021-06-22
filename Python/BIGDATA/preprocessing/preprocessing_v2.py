from konlpy.tag import *
from tqdm import tqdm
import re
import pandas as pd
import numpy as np

# 입력 데이터 파일
file_path2 = 'D://practice/yuna/'
start_file = 'message_label_o.csv'

# 저장 디렉터리
file_path1 = 'D://practice/yuna/'

# 고속도로제거 파일
highway_remove = 'highway_remove_message.csv'

# 마지막 저장되는 파일
final_file = 'preprocess_message_label_o.csv'


# 노이즈제거
def clean_text(text):
    text = text.replace(".", " ").strip()
    # 한글, 영어, 숫자만 남긴다.
    pattern = '[^ ㄱ-ㅣ가-힣|0-9|a-zA-Z]+'
    text = re.sub(pattern=pattern, repl=' ', string=text)
    return text


# 고속도로 데이터 제거
def remove_highway(df):
    highway = "서울외곽순환고속도로 경부고속도로 고창담양고속도로 " \
              "광주대구고속도로 남해고속도로 당진영덕고속도로 대전남부순환고속도로 " \
              "동해고속도로 무안광주고속도로 서울양양고속도로 서울외곽순환고속도로 서천공주고속도로 " \
              "서해안고속도로 순천완주고속도로 영동고속도로 익산포항고속도로 제2경인고속도로 제2중부고속도로 " \
              "중부고속도로 중부내륙고속도로 중부내륙선지고속도로 중앙고속도로 통영대전고속통영대전고속도로 " \
              "통영대전선고속도로 평택제천고속도로 호남고속도로 호남선지고속도로 경부고속도로 경인고속도로 " \
              "남해고속도로 남해제1지고속도로 남해제2지고속도로 동해고속도로 부산외곽고속도로 " \
              "부산외곽순환고속도로 부산울산고속도로 울산고속도로 중앙선지고속도로 나들목 분기점"
    highway = highway.split(' ')
    for i in df['내용']:
        data = clean_text(i.replace('\n', '').strip())
        data = data.split(' ')
        for j in data:
            if j in highway:
                df = df[df.내용 != i]
    return df


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
    df.to_csv(path + file, encoding='cp949')


if __name__ == '__main__':
    # 도로교통 데이터를 읽어들인다.
    df = pd.read_csv(file_path2 + start_file, names=['지역', 'ID', '날짜', '내용', '형태'], header=0, encoding='utf-8')
    df1 = df.dropna()

    # 고속도로 데이터를 제거한다.
    df_v2 = remove_highway(df1)

    # 고속도로 데이터 제거 파일 저장
    save_data(df_v2, file_path1, highway_remove)

    # 토큰화
    processed_data = tokenize(df_v2)
    df_v3 = pd.DataFrame(
        {'지역': df_v2['지역'], 'ID': df_v2['ID'], '날짜': df_v2['날짜'], '내용': processed_data, '형태': df_v2['형태']})
    # Null값 제거
    df_v3['지역'].replace('', np.nan, inplace=True)
    df_v3['ID'].replace('', np.nan, inplace=True)
    df_v3['날짜'].replace('', np.nan, inplace=True)
    df_v3['내용'].replace('', np.nan, inplace=True)
    df_v3['형태'].replace('', np.nan, inplace=True)
    df_V4 = df_v3.dropna()

    # 날짜순 정렬
    df_finished = df_V4.sort_values(by='날짜').reset_index(drop=True)

    # 토큰 분리한 데이터를 저장
    save_data(df_finished, file_path1, final_file)
