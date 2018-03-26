import nltk
from nltk import word_tokenize
import csv
import sys
import glob
import errno
import numpy as np


text_files = {"Donald Trump":   ["Trump_2017"],
			  "Barack Obama":   ["Obama_2016", "Obama_2015", "Obama_2014" , "Obama_2013", "Obama_2012", "Obama_2010", "Obama_2009"],
			  "Bill Clinton":   ["Clinton_2000","Clinton_1999","Clinton_1998","Clinton_1997","Clinton_1996","Clinton_1995","Clinton_1994","Clinton_1993"],
			  "George W Bush":  ["Bush_2008","Bush_2007","Bush_2006","Bush_2005","Bush_2004","Bush_2003","Bush_2002","Bush_2001"],
			  "George Bush Sr.":["Bush_1992","Bush_1991","Bush_1990","Bush_1989"]
			  }

set_of_tags = {"NN", "NNS", "NNP", "NNPS"}

speeches_per_president = {"Donald_Trump": 1, "Barack Obama": 8, "Bill Clinton" : 8, "George W Bush": 8, "George Bush Sr.": 4}


################## functions ################################
def create_counts(set_of_tags, txt_file):
	folder = open("/Users/siddharth/Desktop/3300/CS3300P2/transcripts/Trump_2017.txt", "r")			# change to match your file path
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
	return sort_array


################## functions ################################

def counts_by_SOU(set_of_tags, text_files):
	final_array = []
	for president in text_files:
		for file in text_files[president]:
			final_array.append((file, create_counts(set_of_tags, file)))
	print (final_array)


################## script ################################

################## functions ################################



################## script ################################




counts_by_SOU(set_of_tags, text_files)












