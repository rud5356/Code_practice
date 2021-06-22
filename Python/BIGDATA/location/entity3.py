import tensorflow as tf
from transformers import BertConfig, BertModel, BertForPreTraining, BertTokenizer
from unicodedata import normalize

tokenizer = BertTokenizer('D:/002_bert_morp_tensorflow/vocab.korean_morp.list')
model = BertModel.from_pretrained('D:/002_bert_morp_tensorflow/model.ckpt.data-00000-of-00001', encoding='cp949')

sentence = '상당로 방아다리사거리 사거리 상당사거리 2차로 버스2대'
inputs = tokenizer(sentence, return_tensors="tf")
labels = torch.tensor([1]).unsqueeze(0)
outputs = model(**inputs, labels = labels)

print(outputs[:2])

#print(tokenizer.tokenize(to_subchar(sentence)))