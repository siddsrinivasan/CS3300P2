import nltk
from nltk import word_tokenize
import csv
import sys
import glob
import errno
import numpy as np



presidents = {"Obama":[2009,2010, 2011, 2012, 2013, 2014, 2015, 2016]}
set_of_tags = {"NN", "NNS", "NNP", "NNPS"}

folder = open("/Users/siddharth/Desktop/3300/CS3300P2/transcripts/Bush_1989.txt", "r")			# change to match your file path
csvReader = csv.reader(folder)
speech_text = []
vocab = {}
for row in csvReader:
	for sentence in row:
		tokenize = word_tokenize(sentence)
		tagged_tokens = nltk.pos_tag(tokenize)
		for word in tagged_tokens:
			if (word[0] not in vocab) and (word[1] in set_of_tags):
				vocab[word[0]] = 1
			elif word[1] in set_of_tags:
				vocab[word[0]] = vocab[word[0]] + 1

# sort it
sort_array = []
for word in vocab:
	if vocab[word] > 1:
		sort_array.append((word,vocab[word]))

sort_array = sorted(sort_array, key=lambda x: x[1], reverse=True)

print(sort_array)








