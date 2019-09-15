from flask import request
from app import app
from app.processing import pipeline


@app.route('/feedback/')
@app.route('/classify_one', methods=['POST'])
def classify_one():
    """ classify one group of text """
    data = request.get_json(force=True)
    sentences, predictions = pipeline(data['text'])

    return {
        'sentences': sentences,
        'predictions': predictions
    }


@app.route('/classify_many', methods=['POST'])
def classify_many():
    """ classify many groups of text """
    data = request.get_json(force=True)
    r = []

    for text in data['texts']:
        sentences, predictions = pipeline(text)

        r.append({
            'sentences': sentences,
            'predictions': predictions
        })

    return {'predictions': r}
