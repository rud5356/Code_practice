from konlpy.tag import *
from tqdm import tqdm
import re
import pandas as pd
import csv
def clean_text(text):
    """ 한글, 영문, 숫자만 남기고 제거한다. :param text: :return: """
    text = text.replace(".", " ").strip()
    text = text.replace("·", " ").strip()
    pattern = '[^ ㄱ-ㅣ가-힣|0-9|a-zA-Z]+'
    text = re.sub(pattern=pattern, repl=' ', string=text)
    return text

def get_nouns(tokenizer, sentence):
    #불용어 제거
    stop_words = "한국도로공사 긴급 최초 TBN 경인교통방송 " \
                 "서울외곽순환고속도로 경부고속도로 고창담양고속도로 " \
                 "광주대구고속도로 남해고속도로 당진영덕고속도로 대전남부순환고속도로 " \
                 "동해고속도로 무안광주고속도로 서울양양고속도로 서울외곽순환고속도로 서천공주고속도로 " \
                 "서해안고속도로 순천완주고속도로 영동고속도로 익산포항고속도로 제2경인고속도로 제2중부고속도로 " \
                 "중부고속도로 중부내륙고속도로 중부내륙선지고속도로 중앙고속도로 통영대전고속통영대전고속도로 " \
                 "통영대전선고속도로 평택제천고속도로 호남고속도로 호남선지고속도로 경부고속도로 경인고속도로 " \
                 "남해고속도로 남해제1지고속도로 남해제2지고속도로 동해고속도로 부산외곽고속도로 " \
                 "부산외곽순환고속도로 부산울산고속도로 울산고속도로 중앙선지고속도로 안 중 "
    stop_words = stop_words.split(' ')
    nouns = []
    pos=tokenizer.pos(sentence)
    for keyword, type in pos:
        if type == "NNP":
            nouns.append(keyword)
    nouns = list(filter(lambda w: True if w not in stop_words else '', nouns))
    return nouns

def tokenize(df):
    tokenizer = Mecab()
    processed_data = []
    for sent in tqdm(df['내용']):
        sentence = clean_text(sent.replace('\n', '').strip())
        processed_data.append(get_nouns(tokenizer, sentence))
    return processed_data

def content(df):
    content_data = []
    for sent in tqdm(df['형태']):
        content_data.append(sent)
    return content_data

def save_processed_data(processed_data,content_data):
    """ 토큰 분리한 데이터를 csv로 저장 :param processed_data: :return: """
    with open('D://practice/3/npc_Mecab.csv', 'w', newline='', encoding='cp949') as f:
        writer = csv.DictWriter(f, fieldnames=['내용','형태'])
        for i in range(len(processed_data)):
            writer.writerow({'내용':processed_data[i],'형태':content_data[i]})

if __name__ == '__main__':
    # 도로교통 데이터를 읽어들인다.
    df = pd.read_csv('D://practice/3/event.csv',encoding='cp949')
    processed_data = tokenize(df)
    content_data=content(df)
    print(processed_data)
    # 내용 부분을 토크나이징 한다.
    # 토큰 분리한 데이터를 저장
    save_processed_data(processed_data,content_data)
