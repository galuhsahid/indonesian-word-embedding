from flask import Flask, render_template, jsonify, request
from random import *
from flask_cors import CORS

import gensim
from gensim.models.keyedvectors import KeyedVectors
import requests
import json
import os

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

model = KeyedVectors.load('id/id.bin')

@app.route('/api/word_pair', methods=['GET'])
def get_word_pair():
    word_1 = request.args.get('word_1')
    word_2 = request.args.get('word_2')
    word_3 = request.args.get('word_3')
    word_pair =  model.most_similar(positive=[word_2, word_3], negative=[word_1], topn=1)
    response = {
        'wordPair': word_pair[0][0]
    }
    return jsonify(response)

@app.route('/api/similar_word', methods=['GET'])
def get_similar_word():
    word = request.args.get('word')
    top_n = int(request.args.get('n'))
    similar_words =  model.similar_by_word(word, topn=top_n)
    response = {
        'similarWords': similar_words
    }
    return jsonify(response)

@app.route('/api/similarity', methods=['GET'])
def get_similarity():
    word_1 = request.args.get('word_1')
    word_2 = request.args.get('word_2')
    similarity =  model.similarity(word_1, word_2)
    response = {
        'similarity': similarity
    }
    return jsonify(response)

@app.route('/api/similar_to_given', methods=['GET'])
def get_most_similar_to_given():
    word = request.args.get('word')
    given = request.args.getlist('given[]')
    most_similar =  model.wv.most_similar_to_given(word, given)
    response = {
        'mostSimilar': most_similar
    }
    return jsonify(response)

@app.route('/api/doesnt_match', methods=['GET'])
def get_doesnt_match():
    given = request.args.getlist('given[]')
    doesnt_match =  model.doesnt_match(given)
    response = {
        'doesntMatch': doesnt_match
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
