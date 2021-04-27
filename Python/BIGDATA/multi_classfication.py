import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
stop_words = "한국도로공사 긴급 최초 경인교통방송 " \
                 "서울외곽순환고속도로 경부고속도로 고창담양고속도로 " \
                 "광주대구고속도로 남해고속도로 당진영덕고속도로 대전남부순환고속도로 " \
                 "동해고속도로 무안광주고속도로 서울양양고속도로 서울외곽순환고속도로 서천공주고속도로 " \
                 "서해안고속도로 순천완주고속도로 영동고속도로 익산포항고속도로 제2경인고속도로 제2중부고속도로 " \
                 "중부고속도로 중부내륙고속도로 중부내륙선지고속도로 중앙고속도로 통영대전고속통영대전고속도로 " \
                 "통영대전선고속도로 평택제천고속도로 호남고속도로 호남선지고속도로 경부고속도로 경인고속도로 " \
                 "남해고속도로 남해제1지고속도로 남해제2지고속도로 동해고속도로 부산외곽고속도로 " \
                 "부산외곽순환고속도로 부산울산고속도로 울산고속도로 중앙선지고속도로 안 중 "
stop_words = stop_words.split(' ')

file_path='D://practice/yuna/'
start_file = 'data.csv'
middle_file = 'preprocessing.csv'
final_file = 'clean_data.csv'

total_data = pd.read_csv(file_path+final_file, names=['content', 'content_type'], encoding='cp949')
categories = ['사고', '공사', '기상', '정체', '기타','행사']

train, test = train_test_split(total_data,random_state=30, test_size=0.2)

X_train = train.content
X_test = test.content
train_label = train.content_type
test_label = test.content_type

print(X_test.head(5),X_train.head(5),train_label.head(5),test_label.head(5))


print('Naive Bayes')
NB_pipeline = Pipeline([
                ('tfidf', TfidfVectorizer(stop_words=stop_words)),
                ('clf', OneVsRestClassifier(MultinomialNB(
                    fit_prior=True, class_prior=None))),
            ])
for category in categories:
    print('... Processing {}'.format(category))
    # train the model using X_dtm & y
    NB_pipeline.fit(X_train, train_label)
    # compute the testing accuracy
    prediction = NB_pipeline.predict(X_test)
    print('Test accuracy is {}'.format(accuracy_score(test_label, prediction)))

print('LinearSVC')
SVC_pipeline = Pipeline([
                ('tfidf', TfidfVectorizer(stop_words=stop_words)),
                ('clf', OneVsRestClassifier(LinearSVC(), n_jobs=1)),
            ])
for category in categories:
    print('... Processing {}'.format(category))
    # train the model using X_dtm & y
    SVC_pipeline.fit(X_train, train_label)
    # compute the testing accuracy
    prediction = SVC_pipeline.predict(X_test)
    print('Test accuracy is {}'.format(accuracy_score(test_label, prediction)))

print('Logistic Regression')
LogReg_pipeline = Pipeline([
                ('tfidf', TfidfVectorizer(stop_words=stop_words)),
                ('clf', OneVsRestClassifier(LogisticRegression(solver='sag'), n_jobs=1)),
            ])
for category in categories:
    print('... Processing {}'.format(category))
    # train the model using X_dtm & y
    LogReg_pipeline.fit(X_train, train_label)
    # compute the testing accuracy
    prediction = LogReg_pipeline.predict(X_test)
    print('Test accuracy is {}'.format(accuracy_score(test_label, prediction)))