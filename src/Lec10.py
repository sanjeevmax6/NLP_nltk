# WordNet - One of the largest corpora along with nltk

from nltk.corpus import wordnet

syns = wordnet.synsets("program") # All meanings will ve obtained

# # print(syns)
# print(syns[0].lemmas())

# # Just a word
# print(syns[0].lemmas()[0].name())

# #definiton
# print(syns[0].definition())

# print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        # print("l :", l)
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#Semantic similarity

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")

print(w1.wup_similarity(w2))
