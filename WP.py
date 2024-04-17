import nltk.corpus
import random

sentences = nltk.corpus.brown.sents()


n_grams = {}

for sentence in sentences:
    words = [word for word in sentence if word[0].isalpha()]
    for ix in range(len(words)-1):
        try:
            n_grams[words[ix]].append(words[ix+1])
        except KeyError as _:
            n_grams[words[ix]] = []
            n_grams[words[ix]].append(words[ix+1])


def generate_sentence(nb=7):
    words = []
    next_word = random.choice(list(n_grams.keys()))
    words.append(next_word)
    while len(words) < nb:
        next_word = random.choice(n_grams[next_word])
        words.append(next_word)
        
    return " ".join(words)


def generate_sentence_force(nb=7):
    return " ".join([random.choice(list(n_grams.keys())) for _ in range(nb)])


generate_sentence_force()
