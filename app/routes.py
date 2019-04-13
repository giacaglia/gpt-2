from app import app
from flask import request
from prediction import interactive_conditional_samples

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/predict_next_word')
def get_prediction():
    sentence = request.args.get('sentence')
    print(sentence)
    if not sentence:
        sentence = "I'm doing good, how are"
    next_word = interactive_conditional_samples.prediction_next_word(sentence=sentence)
    print(next_word)
    return next_word