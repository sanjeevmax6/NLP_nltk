# Text Classification

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

# print(all_words["student"])

word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = document
    features = {}
    for w in word_features:
        features[w] = {w in words}
    
    return features

# print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [ (find_features(rev), category) for (rev, category) in documents]

#Naive Bayes classifier
training_set = featuresets[:1900]
testing_Set = featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Naive Bayes Algo accuracy", (nltk.classify.accuracy(classifier, testing_Set))*100)

classifier.show_most_informative_features(15)

# saving the classifier

save_classifier = open("naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()