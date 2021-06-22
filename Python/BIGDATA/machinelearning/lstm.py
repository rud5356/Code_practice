import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import collections
from keras_preprocessing.text import Tokenizer
import csv

file_path = 'D://practice/yuna/'
final_file = 'clean_data.csv'
categories = ['사고', '공사', '기상', '정체', '기타', '행사']

total_data = pd.read_csv(file_path + final_file, names=['content', 'content_type'], encoding='cp949')
train, test = train_test_split(total_data, random_state=30, test_size=0.2)

X_train = train.content
test_data=test.content
X_test = test.content
train_label = train.content_type
test_label = test.content_type


def plot():
    print(train_label.unique())
    plt.plot(train_label.value_counts())
    plt.show()
    print(test_label.unique())
    plt.plot(test_label.value_counts())
    plt.show()


train_counter = collections.Counter(train_label)
test_counter = collections.Counter(test_label)
print('---------------------------------------------------------------------')
print('훈련데이터 레이블 : ',train_counter)
print('테스트데이터 레이블 : ',test_counter)
print('---------------------------------------------------------------------')
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
threshold = 2
total_cnt = len(tokenizer.word_index)  # 단어의 수
rare_cnt = 0  # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
total_freq = 0  # 훈련 데이터의 전체 단어 빈도수 총 합
rare_freq = 0  # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

# 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
for key, value in tokenizer.word_counts.items():
    total_freq = total_freq + value

    # 단어의 등장 빈도수가 threshold보다 작으면
    if value < threshold:
        rare_cnt = rare_cnt + 1
        rare_freq = rare_freq + value
print('---------------------------------------------------------------------')
print('단어 집합(vocabulary)의 크기 :', total_cnt)
print('등장 빈도가 %s번 이하인 희귀 단어의 수: %s' % (threshold - 1, rare_cnt))
print("단어 집합에서 희귀 단어의 비율:", (rare_cnt / total_cnt) * 100)
print("전체 등장 빈도에서 희귀 단어 등장 빈도 비율:", (rare_freq / total_freq) * 100)
vocab_size = total_cnt - rare_cnt + 2
print('단어 집합의 크기 :', vocab_size)
print('---------------------------------------------------------------------')
tokenizer = Tokenizer(vocab_size, oov_token='OOV')
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)
print('---------------------------------------------------------------------')
print("train 문장의 최대 길이 : ", max(len(l) for l in X_train))
print("train 문장의 평균 길이 : ", sum(map(len, X_train)) / len(X_train))
print("test 문장의 최대 길이 : ", max(len(l) for l in X_test))
print("test 문장의 평균 길이 : ", sum(map(len, X_test)) / len(X_test))
print('---------------------------------------------------------------------')

def plot_two():
    plt.hist([len(s) for s in X_train], bins=50)
    plt.xlabel('length of Data')
    plt.ylabel('number of Data')
    plt.show()

    plt.hist([len(s) for s in X_test], bins=50)
    plt.xlabel('length of Data')
    plt.ylabel('number of Data')
    plt.show()

import numpy as np

y_train = []
y_test = []
for i in range(len(train_label)):
    if train_label.iloc[i] == '사고':
        y_train.append([0, 0, 0, 0, 0, 1])
    elif train_label.iloc[i] == '공사':
        y_train.append([0, 0, 0, 0, 1, 0])
    elif train_label.iloc[i] == '기상':
        y_train.append([0, 0, 0, 1, 0, 0])
    elif train_label.iloc[i] == '행사':
        y_train.append([1, 0, 0, 0, 0, 0])
    elif train_label.iloc[i] == '정체':
        y_train.append([0, 0, 1, 0, 0, 0])
    elif train_label.iloc[i] == '기타':
        y_train.append([0, 1, 0, 0, 0, 0])

for i in range(len(test_label)):
    if test_label.iloc[i] == '사고':
        y_test.append([0, 0, 0, 0, 0, 1])
    elif test_label.iloc[i] == '공사':
        y_test.append([0, 0, 0, 0, 1, 0])
    elif test_label.iloc[i] == '기상':
        y_test.append([0, 0, 0, 1, 0, 0])
    elif test_label.iloc[i] == '행사':
        y_test.append([1, 0, 0, 0, 0, 0])
    elif test_label.iloc[i] == '정체':
        y_test.append([0, 0, 1, 0, 0, 0])
    elif test_label.iloc[i] == '기타':
        y_test.append([0, 1, 0, 0, 0, 0])

y_train = np.array(y_train)
y_test = np.array(y_test)

from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.models import Sequential
from keras_preprocessing.sequence import pad_sequences
max_len = 40

X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen=max_len)

model = Sequential()
model.add(Embedding(vocab_size, 100))
model.add(LSTM(128))
model.add(Dense(6, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=20, batch_size=10, validation_split=0.1)
print("테스트 정확도 : {:.2f}%".format(model.evaluate(X_test, y_test)[1] * 100))


predict = model.predict(X_test)

predict_labels = np.argmax(predict, axis=1)
original_labels = np.argmax(y_test, axis=1)

from sklearn.metrics import roc_auc_score

fpr = dict()
tpr = dict()
roc_auc = dict()

print("roc_auc_score: ",roc_auc_score(y_test,predict,multi_class='ovr'))

ori_labels = []
pre_labels = []
for i in range(len(original_labels)):
    if original_labels[i] == 5:
        ori_labels.append('사고')
    elif original_labels[i] == 4:
        ori_labels.append('공사')
    elif original_labels[i] == 3:
        ori_labels.append('기상')
    elif original_labels[i] == 0:
        ori_labels.append('행사')
    elif original_labels[i] == 2:
        ori_labels.append('정체')
    elif original_labels[i] == 1:
        ori_labels.append('기타')

for i in range(len(predict_labels)):
    if predict_labels[i] == 5:
        pre_labels.append('사고')
    elif predict_labels[i] == 4:
        pre_labels.append('공사')
    elif predict_labels[i] == 3:
        pre_labels.append('기상')
    elif predict_labels[i] == 0:
        pre_labels.append('행사')
    elif predict_labels[i] == 2:
        pre_labels.append('정체')
    elif predict_labels[i] == 1:
        pre_labels.append('기타')


from sklearn.metrics import classification_report
print(classification_report(ori_labels, pre_labels))



with open('D://practice/Analysis.csv', 'w', newline='', encoding='cp949') as f:
    writer = csv.DictWriter(f, fieldnames=['내용', '형태', '예측'])
    for i in range(len(test_data)):
        writer.writerow({'내용': test_data.iloc[i].strip(), '형태': ori_labels[i], '예측': pre_labels[i]})


