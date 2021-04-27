import pandas as pd
from koalanlp.Util import initialize, finalize
from koalanlp.proc import RoleLabeler
from koalanlp import API
import requests
import csv

API_KEY = '9e76c797-dafc-42ef-8f3b-4daf41a7e30d'

initialize(ETRI='LATEST')
labeler = RoleLabeler(API.ETRI, etri_key=API_KEY)
local = ['OG', 'AF_ROAD', 'AF_BUILDING', 'LCP_COUNTY', 'LC_OTHERS','LCG_RIVER','OGG_EDUCATION','OGG_ECONOMY','OGG_RELIGION','LC_TOUR']

sentence = '용잠로'
sentences = labeler(sentence)
for sent in sentences:
    entities = sent.getEntities()
    if len(entities) > 0:
        for entity in entities:
            print(entity)
url = "http://api.vworld.kr/req/search?service=search&request=search&version=2.0$category=0501,0502&crs=EPSG:4326&&size=10&" \
      "page=1&query={}&type=place&format=json&errorformat=json&key=437C7816-F207-304B-B849-6CB92EB8B720".format(
    sentence)
data = requests.get(url).json()['response']['result']['items']
print(data)

finalize()
