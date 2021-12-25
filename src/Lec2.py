#Stop word removal

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_Sent = "This is an example of stop word filtration."
stop_words = set(stopwords.words('english'))
# print(stop_words)
words = word_tokenize(example_Sent)

filtered_sentence = []

# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)

# replacement for above
filtered_sentence = [w for w in words if not w in stop_words] 

print(filtered_sentence)