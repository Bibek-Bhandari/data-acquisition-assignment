import json
import spacy
import nltk.data
nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
nlp = spacy.load("en_core_web_sm")

def getJSonObject():
    eassyStringList = ''
    with open('../data/data.json', errors='ignore') as f:
        for jsonObj in f:
            eassyStringList = eassyStringList + jsonObj
    jsonEassyObject = json.loads(eassyStringList)
    return jsonEassyObject


def getNoOfEPST(jsonEassyObject):
    print('Number of essays = ' + str(len(jsonEassyObject)))
    paragraphsListEachEssay = [d['paragraphs'] for d in jsonEassyObject if 'paragraphs' in d]
    paragraphsList = [t['text'] for d in paragraphsListEachEssay for t in d if 'text' in t]
    print('Number of paragraphs = ' + str(len(paragraphsList)))
    sentenceList = [sentence for text in paragraphsList for sentence in tokenizer.tokenize(text)]
    print('Number of Sentences = ' +str(len(sentenceList)))
    tokenList = [token.text for sentence in sentenceList for token in nlp(sentence)]
    print('Number of Tokens = ' + str(len(tokenList)))


jsonEassyObject = getJSonObject()

# Number of essays, paragraphs, sentences, and tokens
getNoOfEPST(jsonEassyObject)
