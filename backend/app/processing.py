import joblib
from nltk.tokenize import sent_tokenize, word_tokenize

glove = joblib.load('app/glove.joblib')
model = joblib.load('app/model2000d.joblib')


def pad(vector, length):
    """ pad a vector with trailing 0's """
    n = length - len(vector)
    for i in range(n):
        vector.append(0)
    return vector[:length]


def embed_word(word):
    """ embed the vector """
    try:
        return list(glove[word.lower()])
    except KeyError:
        return None


def pipeline(text):
    """ pipeline """
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
        predictions.append(model.predict([sentence_vec])[0])

    # return a list of sentences and the prediction
    return sentences, predictions
