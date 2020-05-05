import json
import csv
from PropFile import *

print(Flag)

finaloutput=[]
filename=[]
fileid=[]

def getId(input):
    spamreader=[]
    with open('../data/train-test-split.csv') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter=";"))
    for row in spamreader:
        if row[1] == "TRAIN" and Flag==1:
            essayobject = {}
            essayobject["id"] = int(str(row[0]).replace("essay",""))
            fileid.append(int(str(row[0]).replace("essay","")))
            paragraphobject=[]
            essayobject["paragraphs"]=paragraphobject
            filename.append(row[0])
            finaloutput.append(essayobject)
        elif row[1] == "TEST" and Flag==2:
                essayobject = {}
                essayobject["id"] = int(str(row[0]).replace("essay", ""))
                fileid.append(int(str(row[0]).replace("essay", "")))
                paragraphobject = []
                essayobject["paragraphs"] = paragraphobject
                filename.append(row[0])
                finaloutput.append(essayobject)
        elif Flag==3 and (row[1] == "TEST" or row[1] == "TRAIN"):
            essayobject = {}
            essayobject["id"] = int(str(row[0]).replace("essay", ""))
            fileid.append(int(str(row[0]).replace("essay", "")))
            paragraphobject = []
            essayobject["paragraphs"] = paragraphobject
            filename.append(row[0])
            finaloutput.append(essayobject)


def getText(input1,input2):
    spamreader = []
    i=0
    for file in input2:
        with open('../data/ArgumentAnnotatedEssays-2.0/ArgumentAnnotatedEssays-2.0/brat-project-final/brat-project-final/'+str(file)+'.txt',encoding="utf8") as csvfile:
            spamreader = list(csv.reader(csvfile))
            text=""
            for content in spamreader:
                text+=''.join(content)
            input1.__getitem__(i)["text"]=text
            i+=1

def getannotation(input1,input2):
    spamreader = []
    i = 0
    for file in input2:
        majorclaim=[]
        claims=[]
        premises=[]
        with open('../data/ArgumentAnnotatedEssays-2.0/ArgumentAnnotatedEssays-2.0/brat-project-final/brat-project-final/' + str(file) + '.ann', encoding="utf8") as csvfile:
            spamreader = list(csv.reader(csvfile, delimiter="\t"))
            for content in spamreader:
                if "MajorClaim" in content[1]:
                    majorclaimobject={}
                    dt=content[1].split(" ")
                    span=[int(dt[1]), int(dt[2])]
                    majorclaimobject["span"]=span
                    majorclaimobject["text"]=content[2]
                    majorclaim.append(majorclaimobject)
                if "Premise" in content[1]:
                    premiseclaimobject = {}
                    dt = content[1].split(" ")
                    span = [int(dt[1]), int(dt[2])]
                    premiseclaimobject["span"] = span
                    premiseclaimobject["text"] = content[2]
                    premises.append(premiseclaimobject)
                if "Claim" in content[1]:
                    claimobject = {}
                    dt = content[1].split(" ")
                    span = [int(dt[1]), int(dt[2])]
                    claimobject["span"] = span
                    claimobject["text"] = content[2]
                    claims.append(claimobject)
        input1.__getitem__(i)["major_claim"] = majorclaim
        input1.__getitem__(i)["claims"] = claims
        input1.__getitem__(i)["premises"] = premises
        i += 1

def getconfirmationbias(input1,input2):
    spamreader = []
    with open('../data/UKP-OpposingArgumentsInEssays_v1.0/UKP-OpposingArgumentsInEssays_v1.0/labels.tsv') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter="\t"))
    for content in spamreader:
        if content[0] in input2:
            if "negative" in content[1]:
                input1.__getitem__(input2.index(content[0]))["confirmation_bias"]=False
            elif "positive" in content[1]:
                input1.__getitem__(input2.index(content[0]))["confirmation_bias"] = True

def getparagraph(input1,input2):
    spamreader = []
    with open('../data/UKP-InsufficientArguments_v1.0/UKP-InsufficientArguments_v1.0/data-tokenized.tsv') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter="\t"))
    filedata=[]
    for content in spamreader[1:]:
        filedata.append(content[0])
    i=0
    for content in filedata:

        value=int(content)
        if value in fileid:
            paragraphobject={}
            paragraphobject["text"]=spamreader[1:].__getitem__(i)[2]
            if len(spamreader[1:].__getitem__(i)[3])>0:
                paragraphobject["sufficient"]=False
            else:
                paragraphobject["sufficient"] = True
            input1.__getitem__(fileid.index(value))["paragraphs"].append(paragraphobject)
        i+=1


getId(finaloutput)
getText(finaloutput,filename)
getannotation(finaloutput,filename)
getconfirmationbias(finaloutput,filename)
getparagraph(finaloutput,filename)
#print(json.dumps(finaloutput))
with open('../data/data.json', 'w') as f:
    json.dump(finaloutput, f)