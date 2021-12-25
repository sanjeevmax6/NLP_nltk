# import nltk

# print("H")
# nltk.download()
# print("i")

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hey There, how are you doing today? The weather is great and I am good too."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)