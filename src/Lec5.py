# Chunking

# Extracting named entitites/nouns, that is who, what, were the sentence refers to should be deciphered

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# PunktSentenceTokenizer is an unsupervised model, and we can try it according to our use

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)

        chunkGram = """ Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}""" # Will search for aan adverb throughout and output 0 or 1. This is a RegEX
        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)
        chunked.draw()





#             print(tagged)
#     except Exception as err:
#         print(str(err))

process_content()

# What this does is, it recognizes words in the sentence grammatically, and creates a tuple for each word stating them to be a noun, adevrb, verb etc
