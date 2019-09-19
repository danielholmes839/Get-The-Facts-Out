# Daniel Holmes
# 2019/9/19
# routes.py
# backend to make predictions

from flask import request
from app import app
from app.processing import pipeline


@app.route('/classify/groups', methods=['POST'])
def classify_one():
    """ classify one group of text """
    group = request.get_json(force=True)['group']
    sentences, predictions = pipeline(group)

    return {
        'sentences': sentences,
        'predictions': predictions
    }


@app.route('/classify/group', methods=['POST'])
def classify_many():
    """ classify many groups of text """
    groups = request.get_json(force=True)['groups']
    predictions = []

    for group in groups:
        sentences, group_predictions = pipeline(group)

        predictions.append({
            'sentences': sentences,
            'predictions': group_predictions
        })

    return {'predictions': predictions}
