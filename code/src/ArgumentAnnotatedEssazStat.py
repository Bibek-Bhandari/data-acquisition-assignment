import json
import spacy
import nltk.data

nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
nlp = spacy.load("en_core_web_sm")


def getJSonObject():
    essayStringList = ''
    with open('../data/sample_output.json', errors='ignore') as f:
        for jsonObj in f:
            essayStringList = essayStringList + jsonObj
    jsonEssayObject = json.loads(essayStringList)
    return jsonEssayObject


def getAllConfirmationBiasEssay():
    allConfirmationBiasEssayList = [d for d in jsonEssaysObject if 'confirmation_bias' in d and d['confirmation_bias']
                                    is True]
    return allConfirmationBiasEssayList


def getAllNonConfirmationBiasEssay():
    allNonConfirmationBiasEssayList = [d for d in jsonEssaysObject if
                                       'confirmation_bias' in d and d['confirmation_bias']
                                       is False]
    return allNonConfirmationBiasEssayList


def getAllSufficientParagraphs():
    paragraphsListEachEssay = [d['paragraphs'] for d in jsonEssaysObject if 'paragraphs' in d]
    sufficientParagraphsList = [t['text'] for d in paragraphsListEachEssay for t in d if
                                'text' in t and t['sufficient'] is True]
    return sufficientParagraphsList


def getAllNonSufficientParagraphs():
    paragraphsListEachEssay = [d['paragraphs'] for d in jsonEssaysObject if 'paragraphs' in d]
    nonSufficientParagraphsList = [t['text'] for d in paragraphsListEachEssay for t in d if
                                   'text' in t and t['sufficient'] is False]
    return nonSufficientParagraphsList


def getAllParagraphsTextList():
    paragraphsListEachEssay = [d['paragraphs'] for d in jsonEssaysObject if 'paragraphs' in d]
    paragraphsList = [t['text'] for d in paragraphsListEachEssay for t in d if 'text' in t]
    return paragraphsList


def gatAllEssaySentences():
    eachEssayTextList = [d['text'] for d in jsonEssaysObject if 'text' in d]
    sentenceList = [sentence for text in eachEssayTextList for sentence in tokenizer.tokenize(text)]
    return sentenceList


def getAllMajorClaims():
    majorClaimsInListEachEssay = [d['major_claim'] for d in jsonEssaysObject if 'major_claim' in d]
    allMajorClaimsList = [eachMajorClaims for eachEssayMajorClaims in majorClaimsInListEachEssay for eachMajorClaims in
                          eachEssayMajorClaims]
    return allMajorClaimsList


def getAllMajorClaimsTokens():
    allMajorClaimsList = getAllMajorClaims()
    allMajorClaimsTextList = [eachMajorClaims['text'] for eachMajorClaims in allMajorClaimsList]
    allMajorClaimsTokens = [token.text for eachMajorClaimsText in allMajorClaimsTextList for token in
                            nlp(eachMajorClaimsText)]
    return allMajorClaimsTokens


def getAllClaims():
    claimsInListEachEssay = [d['claims'] for d in jsonEssaysObject if 'claims' in d]
    allClaimsList = [eachClaims for eachEssayClaims in claimsInListEachEssay for eachClaims in
                     eachEssayClaims]
    return allClaimsList


def getAllClaimsTokens():
    allClaimsList = getAllClaims()
    allClaimsTextList = [eachClaims['text'] for eachClaims in allClaimsList]
    allClaimsTokens = [token.text for eachClaimsText in allClaimsTextList for token in
                       nlp(eachClaimsText)]
    return allClaimsTokens


def getAllPremises():
    premisesInListEachEssay = [d['premises'] for d in jsonEssaysObject if 'premises' in d]
    allPremisesList = [eachPremises for eachEssayPremises in premisesInListEachEssay for eachPremises in
                       eachEssayPremises]
    return allPremisesList


def getAllPremisesTokens():
    allPremisesList = getAllPremises()
    allPremisesTextList = [eachPremises['text'] for eachPremises in allPremisesList]
    allPremisesTokens = [token.text for eachPremisesText in allPremisesTextList for token in
                         nlp(eachPremisesText)]
    return allPremisesTokens


# createEssayObject
jsonEssaysObject = getJSonObject()


# 1.Number of essays, paragraphs, sentences, and tokens
def printNoOfEPST():
    print('Number of essays = ' + str(len(jsonEssaysObject)))
    paragraphsList = getAllParagraphsTextList()
    print('Number of paragraphs = ' + str(len(paragraphsList)))
    sentenceList = gatAllEssaySentences()
    print('Number of Sentences = ' + str(len(sentenceList)))
    tokenList = [token.text for sentence in sentenceList for token in nlp(sentence)]
    print('Number of Tokens = ' + str(len(tokenList)))


printNoOfEPST()
print('-' * 100)


# 2.Number of major claims, claims, premises
def printNoOfMajorClaimsClaimsPremises():
    allMajorClaimsList = getAllMajorClaims()
    print('Number of major claims = ', len(allMajorClaimsList))

    allClaimsList = getAllClaims()
    print('Number of claims = ', len(allClaimsList))

    allPremisesList = getAllPremises()
    print('Number of premises = ', len(allPremisesList))


printNoOfMajorClaimsClaimsPremises()
print('-' * 100)


# 3.Number of essays with and without confirmation bias
def printNoOfWithWithoutConfirmationBiasEssay():
    print('Number of essays with confirmation bias = ', len(getAllConfirmationBiasEssay()))
    print('Number of essays without confirmation bias = ', len(getAllNonConfirmationBiasEssay()))


printNoOfWithWithoutConfirmationBiasEssay()
print('-' * 100)


# 4.Number of sufficient and insufficient paragraphs (arguments)
def printNoOfSufficientAndInsufficientParagraph():
    print('Number of sufficient paragraphs = ', len(getAllSufficientParagraphs()))
    print('Number of insufficient paragraphs = ', len(getAllNonSufficientParagraphs()))


printNoOfSufficientAndInsufficientParagraph()
print('-' * 100)


# 5.Average number of tokens in major claims, claims, and premises
def printAverageNoOfMajorClaimsClaimsPremisesTokens():
    allMajorClaimsTokens = getAllMajorClaimsTokens()
    allClaimsTokens = getAllMajorClaimsTokens()
    allPremisesTokens = getAllPremisesTokens()
    totalMCPTokens = len(allMajorClaimsTokens) + len(allClaimsTokens) + len(allPremisesTokens)
    print("Average number of tokens in major claims, claims, and premises = ", int(totalMCPTokens / 3))


printAverageNoOfMajorClaimsClaimsPremisesTokens()
