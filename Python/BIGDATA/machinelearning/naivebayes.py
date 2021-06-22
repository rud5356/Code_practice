import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import numpy as np

file_path1 = 'D://practice/yuna/'

# 분석할 데이터 파일
start_file = 'preprocess_message_label_o.csv'

# 데이터 로드
# message 일부 레이블 처리해서 불러오기
df = pd.read_csv(file_path1+start_file,encoding='cp949')

# 0 -> 관련 O, 1 -> 관련 X
labels = [0, 1]

x_data = df['내용'].to_numpy()
y_data = df['형태'].to_numpy()

# 단어 카운트 가중치
transformer = TfidfVectorizer()
transformer.fit(x_data)
x_data = transformer.transform(x_data)


x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=777, stratify=y_data)

# 모델 생성
model = MultinomialNB(alpha=1.0)

# 모델 학습

model.fit(x_train, y_train)

# 모델 검증
print(model.score(x_test, y_test))