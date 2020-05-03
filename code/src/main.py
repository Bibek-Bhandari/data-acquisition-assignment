import spacy

import csv

from spacy.lang.en import English

nlp = English()


def getTrainSplit():
	with open('../data/train-test-split.csv') as csvfile:
		spamreader = list(csv.reader(csvfile, delimiter=";"))
	split = []
	for row in spamreader:
		if row[1] == "TRAIN":
			split.append(row[0])
	return split


split = getTrainSplit()
essays = []
for s in split:
	f = open('../data/UKP-OpposingArgumentsInEssays_v1.0/UKP-OpposingArgumentsInEssays_v1.0/essays/'+s+'.txt','rt');
	essays.append(f.read())

print("No of essays: "+str(len(essays)))

        	



