import pandas as pd
from sklearn.model_selection import train_test_split
import collections

file_path = 'D://practice/yuna/clean_data.csv'
categories = ['사고', '공사', '기상', '정체', '기타', '행사']

total_data = pd.read_csv(file_path, names=['content', 'content_type'], encoding='cp949')
train, test = train_test_split(total_data, random_state=30, test_size=0.2)

# x = 내용, y = 레이블
# train => 학습, test => 테스트용
X_train = train.content
test_data = test.content
X_test = test.content

# y 배열에 담을 것들 (숫자로 변환하기 위해서)
train_label = train.content_type
test_label = test.content_type

import matplotlib.pyplot as plt


def plot():
    print(train_label.unique())
    plt.plot(train_label.value_counts())
    plt.show()
    print(test_label.unique())
    plt.plot(test_label.value_counts())
    plt.show()


train_counter = collections.Counter(train_label)
test_counter = collections.Counter(test_label)
print('-------------------------------------------------------------------------------------')
print('훈련데이터 레이블 : ', train_counter)
print('테스트데이터 레이블 : ', test_counter)
print('-------------------------------------------------------------------------------------')

y_train = []
y_test = []

for i in range(len(train_label)):
    if train_label.iloc[i] == '사고':
        y_train.append([0])
    elif train_label.iloc[i] == '공사':
        y_train.append([1])
    elif train_label.iloc[i] == '기상':
        y_train.append([2])
    elif train_label.iloc[i] == '행사':
        y_train.append([3])
    elif train_label.iloc[i] == '정체':
        y_train.append([4])
    elif train_label.iloc[i] == '기타':
        y_train.append([5])

for i in range(len(test_label)):
    if test_label.iloc[i] == '사고':
        y_test.append([0])
    elif test_label.iloc[i] == '공사':
        y_test.append([1])
    elif test_label.iloc[i] == '기상':
        y_test.append([2])
    elif test_label.iloc[i] == '행사':
        y_test.append([3])
    elif test_label.iloc[i] == '정체':
        y_test.append([4])
    elif test_label.iloc[i] == '기타':
        y_test.append([5])

import numpy as np

y_train = np.array(y_train)
y_test = np.array(y_test)

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from konlpy.tag import *


def get_noun(text):
    tokenizer = Kkma()
    nouns = tokenizer.nouns(text)
    return [n for n in nouns]


cv = CountVectorizer(tokenizer=get_noun)

tdm = cv.fit_transform(X_train)

classifier = Pipeline([
    ('vectorizer', CountVectorizer(min_df=1, max_df=2)),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsOneClassifier(LinearSVC()))])

classifier.fit(X_train, y_train)

predicted = classifier.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, predicted))
