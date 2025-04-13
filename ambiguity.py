import os
import nltk
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import PlaintextCorpusReader

poeAmbiguity = 0
loveAmbiguity = 0

#Reading
corpus_root = 'corpora'
corpus = PlaintextCorpusReader(corpus_root, '.*')

poeSentences = corpus.words('poeSentences.txt')
lovecraftSentences = corpus.words('lovecraftSentences.txt')
poeQuotes = corpus.words('poeQuotes.txt')
lovecraftQuotes = corpus.words('lovecraftQuotes.txt')


# Grabbing Tokens - all Sentences - can be modded for Quotes
tagsIwant = ['VBD', 'VBN', 'VBZ', 'VB'] #Change here for different Parts of Speech

poelowercaseTokens = [token.lower() for token in poeSentences]
poeUniqueTokens = set(poelowercaseTokens)

lovelowercaseTokens = [token.lower() for token in lovecraftSentences]
loveUniqueTokens = set(lovelowercaseTokens)

poetagged = pos_tag(poeUniqueTokens)
poeshort = [word for word, tag in poetagged if tag in tagsIwant]

lovetagged = pos_tag(loveUniqueTokens)
loveshort = [word for word, tag in lovetagged if tag in tagsIwant]


print(len(loveshort))
print(loveshort)
print(len(poeshort))
print(poeshort)

for w in poeshort:
    lemma = wn.morphy(w)
    lemma = lemma if lemma else w
    synsets = wn.synsets(lemma)
    poeAmbiguity += len(synsets) / len(poeshort)

print("The average ambiguity value for each verb in the Poe corpus is:")
print(poeAmbiguity)

for w in loveshort:
    lemma = wn.morphy(w)
    lemma = lemma if lemma else w
    synsets = wn.synsets(lemma)
    loveAmbiguity += len(synsets) / len(loveshort)

print('The average ambiguity value for each verb in the Lovecraft corpus is:')
print(loveAmbiguity)
# note - for some reason the values change every time you run the script. They average out to be about 7.5 and 8.1 respectively though.
# Lovecraft is always more ambiguous (verbwise) than Poe (but only slightly!)
# Noun results [NN, NNP, NNPS, NNS] values are == Poe: ~5, Lovecraft: ~5.5