from nltk.stem import LancasterStemmer
import nltk


def stemming(text):
    """does stemming"""
    words_list = nltk.word_tokenize(text)
    words_set = set()

    ps = LancasterStemmer()

    for word in words_list:
        words_set.add(ps.stem(word))

    return words_set
