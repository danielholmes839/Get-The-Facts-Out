# Daniel Holmes
# 2019/9/19
# data.py
#

import joblib
import pandas as pd
from nltk.tokenize import word_tokenize

files = [
    'objective_cv_train.txt',
    'objective_test.txt',
    'subjective_cv_train.txt',
    'subjective_test.txt'
]

objective = [1, 1, 0, 0]


def pad(vector, length):
    """ Pad a vector with trailing 0's """
    n = length - len(vector)
    for i in range(n):
        vector.append(0)
    return vector


def embed_word(model, word):
    """ get the glove embedding of a word """
    try:
        return list(model[word])
    except KeyError:
        return None


def embed_sentences(sentences):
    """ sentences to vectors """
    model = joblib.load('glove.joblib')
    sentence_vectors = []

    for sentence in sentences:
        sentence_vec = []
        words = word_tokenize(sentence)

        for word in words:
            vector = embed_word(model, word)
            if vector:
                sentence_vec += vector

        sentence_vectors.append(pad(sentence_vec, 2000))

    return sentence_vectors


def load():
    """ load the file"""
    df = pd.read_csv('data.csv', index_col=0)
    sentences = list(df['sentence'])
    vectors = embed_sentences(sentences)
    labels = list(df['objective'])
    return vectors, labels


def preprocess(file, label):
    """ text file to df """
    df = pd.DataFrame()
    text = open('data/'+file, 'r').read()
    sentences = text.split('\n')

    for row, sentence in enumerate(sentences):
        df.at[row, 'sentence'] = sentence
        df.at[row, 'objective'] = label

    return df


if __name__ == '__main__':
    dfs = []
    for file, label in zip(files, objective):
        dfs.append(preprocess(file, label))

    df = pd.concat(dfs).reset_index(drop=True)
    df.to_csv('data.csv')
