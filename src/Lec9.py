# NLTK Corpora

import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

# Check out /AppData/nltk_data_corpus for all corpus

sample = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample)
print(tok[5:15])
