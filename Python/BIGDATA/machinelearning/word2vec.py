# from gensim.models.word2vec import Word2Vec
# from tqdm import tqdm

# data = [sent.strip().split(",") for sent in tqdm(open('D://practice/yuna/tokenized_data_word.csv', 'r', encoding='cp949').readlines())]
# print(data[0])
# model = Word2Vec(data,         # 리스트 형태의 데이터
#                  sg=1,         # 0: CBOW, 1: Skip-gram
#                  size=40,     # 벡터 크기
#                  window=2,     # 고려할 앞뒤 폭(앞뒤 3단어)
#                  min_count=1,  # 사용할 단어의 최소 빈도(3회 이하 단어 무시)
#                  workers=4)

#model.save('word2vec.model')
# model = Word2Vec(token,         # 리스트 형태의 데이터
#                  sg=0,         # 0: CBOW, 1: Skip-gram
#                  size=40,     # 벡터 크기
#                  window=2,     # 고려할 앞뒤 폭(앞뒤 3단어)
#                  min_count=1,  # 사용할 단어의 최소 빈도(3회 이하 단어 무시)
#                  workers=4)
# model.save('word2vec2.model')
#model = Word2Vec.load('word2vec.model')
#print(model.wv.most_similar('서울시'))
#print(model.wv.most_similar(positive=['서울시', '교통정보'], negative=['교통정보']))



lo = ['전라북도','전주시','덕진구', '여산로','232']
for i in lo:
    if '로' in i:
        print(i)
#     i.find('로')
# print(lo.find('로'))