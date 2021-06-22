import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import collections
from keras_preprocessing.text import Tokenizer
import csv

file_path = 'D://practice/yuna/'
start_file = 'data.csv'
middle_file = 'preprocessing.csv'
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
print(train_counter)
print(test_counter)

max_words = 35000
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)

print("train 문장의 최대 길이 : ", max(len(l) for l in X_train))
print("train 문장의 평균 길이 : ", sum(map(len, X_train)) / len(X_train))

print("test 문장의 최대 길이 : ", max(len(l) for l in X_test))
print("test 문장의 평균 길이 : ", sum(map(len, X_test)) / len(X_test))

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

from keras_preprocessing.sequence import pad_sequences
from sklearn.ensemble import RandomForestClassifier
max_len = 40


X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen=max_len)

forest = RandomForestClassifier(n_estimators=100, random_state=2)
forest.fit(X_train,y_train)
y_predict = forest.predict(X_test)

predict_labels = np.argmax(y_predict, axis=1)
original_labels = np.argmax(y_test, axis=1)

from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.preprocessing import label_binarize
fpr = dict()
tpr = dict()
roc_auc = dict()
ytest = label_binarize(y_test,classes=categories)
ypreds = label_binarize(y_predict,classes=categories)

for i in range(6):
    fpr[i], tpr[i], _ = roc_curve(ytest[:, i], ypreds[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])
plt.figure(figsize=(15, 5))
for idx, i in enumerate(range(6)):
    plt.plot(fpr[i], tpr[i], label='ROC curve (area = %0.2f)' % roc_auc[i])
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Class %0.0f' % idx)
    plt.legend(loc="lower right")
plt.show()
print("roc_auc_score: ", roc_auc_score(ytest, ypreds, multi_class='raise'))

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
print("훈련 세트 정확도: {:.3f}".format(forest.score(X_train, y_train)))
print("테스트 세트 정확도: {:.3f}".format(forest.score(X_test, y_test)))
print(classification_report(ori_labels, pre_labels))

with open('D://practice/Analysis_v2.csv', 'w', newline='', encoding='cp949') as f:
    writer = csv.DictWriter(f, fieldnames=['내용', '형태', '예측'])
    for i in range(len(test_data)):
        writer.writerow({'내용': test_data.iloc[i].strip(), '형태': ori_labels[i], '예측': pre_labels[i]})


