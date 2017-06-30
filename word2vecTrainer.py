# -*- coding: utf-8 -*-

import word2vec
import sys


#Step 1
word2vec.word2phrase('E:\DEV\nlp\output_AK.txt', '/Users/BSSoper/Downloads/out-phrases_v4', verbose=True)

#Step 2
word2vec.word2vec('/Users/BSSoper/Downloads/out-phrases_v4', '/Users/BSSoper/Downloads/out_v42.bin', size=100, verbose=True)

#Step 3
# word2vec.word2clusters('/Users/BSSoper/Downloads/output_v4', '/Users/BSSoper/Downloads/out-clusters_v4.txt', 200, verbose=True)

#Step 4
model = word2vec.load('/Users/BSSoper/Downloads/out_v4.bin')

print model.vocab
word= raw_input("word: ")
print word
indexes, metrics = model.cosine(word)
print model.generate_response(indexes, metrics).tolist()



