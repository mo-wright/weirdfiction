## not actually sure if i'll use this file - it's here for me to practice some stuff :)
## feel free to use this skeleton for whatever if any of it is useful

import os
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import PlaintextCorpusReader

corpus_root = 'corpora'
corpus = PlaintextCorpusReader(corpus_root, '.*')

poeSentences = corpus.words('poeSentences.txt')
lovecraftSentences = corpus.words('lovecraftSentences.txt')
poeQuotes = corpus.words('poeQuotes.txt')
lovecraftQuotes = corpus.words('lovecraftQuotes.txt')

#smoke test
print(poeSentences)