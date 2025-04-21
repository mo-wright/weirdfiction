import os
import spacy
from nltk.corpus import wordnet as wn
import pandas as pd


nlp = spacy.load("en_core_web_md")

collPath = 'corpora'

def wordCollector(words, unit):
    wordList = []
    nodeAtts = []
    unitList = []
    synsetCounts = []
    for token in words:
        if token.pos_ == "ADJ" and len(wn.synsets(token.lemma_)) >= 25:
            synsets = len(wn.synsets(token.lemma_))
            wordList.append(token.lemma_)
            nodeAtts.append(token.pos_)
            unitList.append(unit)
            synsetCounts.append(synsets)

    data = {
        'word': wordList,
        'nodeType': nodeAtts,
        'unit': unitList,
        'synset' : synsetCounts}
    df = pd.DataFrame(data)
    return df

allDataFrames = []

for file in os.listdir(collPath):
    if file.endswith("Sentences.txt"):
        filepath = f"{collPath}/{file}"
        name, extension = os.path.splitext(file)
        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)
            myDataFrame = wordCollector(spacyRead, name)
            allDataFrames.append(myDataFrame)


# Make an output filepath
outputFilePath = 'adjFILTERED.tsv'
# Turn the list of dataframes into one dataframe:
fullDataFrame = pd.concat(allDataFrames, ignore_index=True)

fullDataFrame.to_csv(outputFilePath, sep='\t', index=False)
print('I just saved a dataframe as a TSV file.')
# Go check your filestash for the file.