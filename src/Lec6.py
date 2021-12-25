# Chinking

# Same as chunk, we chink something from the chunk. that is we remove something from the chunk
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

        chunkGram = """ Chunk: {<.*>+}
                                }<VB.?|IN|DT>+{""" # A chink has closed braces first and then open braces
        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(tagged)
        chunked.draw()

process_content()