from collections import Counter
from konlpy.tag import *
import csv
r=open('D://practice/3/accident.csv',encoding='cp949')
data=csv.reader(r)
lines=[]
for rr in data:
    lines.append(rr[4])
r.close()
del lines[0]

hannanum = Hannanum()
kkma = Kkma()
komoran = Komoran()
okt = Okt()

for i in lines:
    noun = hannanum.nouns(i)
    print(noun)
#count=Counter(noun)

#noun_list = count.most_common(100)
#for v in noun_list:
#    print(v)
