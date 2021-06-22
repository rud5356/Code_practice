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

train_counter = collections.Counter(train_label)
test_counter = collections.Counter(test_label)
print('---------------------------------------------------------------------------------------------------------------')
print('훈련데이터 레이블 : ', train_counter)
print('테스트데이터 레이블 : ', test_counter)
print('---------------------------------------------------------------------------------------------------------------')

y_train = []
y_test = []

# 레이블 숫자로 변환
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


import numpy as np

y_train = np.array(y_train)
y_test = np.array(y_test)

# 분류기 실행
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier


def get_noun(text):
    nouns = text.split(' ')
    return [n for n in nouns]


classifier = Pipeline([('vect', CountVectorizer(tokenizer=get_noun)),
                       ('tfidf', TfidfTransformer()),
                       ('clf-svm', OneVsRestClassifier(SVC(kernel='linear', probability=True, C=1000, gamma=0.1)))])
y_score = classifier.fit(X_train, y_train).decision_function(X_test)

classifier.fit(X_train, y_train)

predicted = classifier.predict(X_test)

predict_labels = np.argmax(predicted, axis=1)
original_labels = np.argmax(y_test, axis=1)


# auc, 정밀도, 재현율, f1-score, 정확도
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score


def auc_plot():
    n_classes = len(categories)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])

    mean_tpr /= n_classes

    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

    plt.figure()
    plt.plot(fpr["micro"], tpr["micro"],
             label='micro-average ROC curve (area = {0:0.2f})'
                   ''.format(roc_auc["micro"]),
             color='deeppink', linestyle=':', linewidth=4)

    plt.plot(fpr["macro"], tpr["macro"],
             label='macro-average ROC curve (area = {0:0.2f})'
                   ''.format(roc_auc["macro"]),
             color='navy', linestyle=':', linewidth=4)

    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Some extension of Receiver operating characteristic to multi-class')
    plt.legend(loc="lower right")
    plt.show()


# auc_plot()
y_prob = classifier.predict_proba(X_test)
print("roc_auc_score: ", roc_auc_score(y_test, y_prob, multi_class='ovr'))
print('---------------------------------------------------------------------')

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

import csv

with open('D://practice/multi_svm.csv', 'w', newline='', encoding='cp949') as f:
    writer = csv.DictWriter(f, fieldnames=['내용', '형태', '예측'])
    for i in range(len(test_data)):
        writer.writerow({'내용': test_data.iloc[i].strip(), '형태': ori_labels[i], '예측': pre_labels[i]})
