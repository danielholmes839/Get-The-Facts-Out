# Daniel Holmes
# 2019/9/19
# processing.py
# functions to process text and make predictions

import joblib
from nltk.tokenize import sent_tokenize, word_tokenize

glove = joblib.load('app/glove.joblib')         # glove model from gensim
model = joblib.load('app/model2000d.joblib')    # trained objective/subjective sentence classifier


def pad(vector, length):
    """ pad a vector with trailing 0's """
    n = length - len(vector)
    for i in range(n):
        vector.append(0)
    return vector[:2000]


def embed_word(word):
    """ embed a word """
    try:
        return list(glove[word.lower()])
    except KeyError:
        return None


def pipeline(text):
    """
    pipeline which separates text into sentences and classifies each sentence
    returns a list of sentences and predictions
    """
    sentences = sent_tokenize(text)
    predictions = []

    for sentence in sentences:
        # split by sentences
        sentence_vec = []
        words = word_tokenize(sentence)

        for word in words:
            # split words in the sentence
            word_vec = embed_word(word)

            if word_vec:
                sentence_vec += word_vec

        # pad the vector and make a prediction
        sentence_vec = pad(sentence_vec, 2000)
        prediction = model.predict([sentence_vec])[0]
        predictions.append(prediction)

    # return a list of sentences and the prediction
    return sentences, predictions
