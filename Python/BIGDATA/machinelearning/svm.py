import pandas as pd

file_path1 = 'D://practice/yuna/'

# 분석할 데이터 파일
start_file = 'preprocess_message_label_o.csv'

from sklearn.model_selection import train_test_split

data = pd.read_csv(file_path1 + start_file, encoding="cp949")
data = data.loc[:, ("내용", "형태")]
train, test = train_test_split(data, test_size=0.33, random_state=42)

print(train.groupby("형태").count())
print(test.groupby("형태").count())

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from konlpy.tag import *


def get_noun(text):
    tokenizer = Kkma()
    nouns = tokenizer.nouns(text)
    return [n for n in nouns]


cv = CountVectorizer(tokenizer=get_noun)

tdm = cv.fit_transform(train["내용"])

text_clf_svm = Pipeline([('vect', CountVectorizer(tokenizer=get_noun)),
                         ('tfidf', TfidfTransformer()),
                         ('clf-svm',
                          SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter_no_change=5, random_state=42))])

text_clf_svm = text_clf_svm.fit(train["내용"], train["형태"])

from sklearn.model_selection import cross_val_predict

y_train_pred = cross_val_predict(text_clf_svm, train["내용"], train["형태"], cv=5)

from sklearn.metrics import classification_report

print(classification_report(train["형태"], y_train_pred))