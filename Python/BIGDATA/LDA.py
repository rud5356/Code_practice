from tqdm import tqdm
from gensim.models.ldamodel import LdaModel
from gensim import corpora
import logging
from gensim.models.coherencemodel import CoherenceModel
import matplotlib.pyplot as plt
def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())
        return model_list, coherence_values

def find_optimal_number_of_topics(dictionary, corpus, processed_data):
    limit = 40; start = 1; step = 8;
    model_list, coherence_values = compute_coherence_values(dictionary=dictionary, corpus=corpus, texts=processed_data, start=start, limit=limit, step=step)
    x = range(start, limit, step)
    plt.plot(x, coherence_values)
    plt.xlabel("Num Topics")
    plt.ylabel("Coherence score")
    plt.legend(("coherence_values"), loc='best')
    plt.show()

if __name__ == '__main__':
    processed_data = [sent.strip().split(",") for sent in tqdm(open('D://practice/3/tokenized_data.csv', 'r', encoding='cp949').readlines())]
    # 정수 인코딩과 빈도수 생성
    dictionary = corpora.Dictionary(processed_data)
    # 출현빈도가 적거나 자주 등장하는 단어는 제거
    dictionary.filter_extremes(no_below=10, no_above=0.05)
    corpus = [dictionary.doc2bow(text) for text in processed_data]
    print('Number of unique tokens: %d' % len(dictionary))
    print('Number of documents: %d' % len(corpus))
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # 최적의 토픽 수 찾기
    find_optimal_number_of_topics(dictionary, corpus, processed_data)
