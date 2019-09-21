import joblib
import gensim.downloader as api

glove = api.load('glove-wiki-gigaword-50')
joblib.dump(glove, 'glove.joblib')