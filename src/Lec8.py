# Lemmatization
#same as stemming, but the end result will be a proper word with meaning

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("rocks"))

print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("run"))