from joblib import dump
import gensim.downloader as api

glove = api.load('glove-wiki-gigaword-50')
dump(glove, 'glove.joblib')