from flask import Flask, request, jsonify, send_from_directory
import spacy
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app, origins=["http://127.0.0.1:5000"])

nlp = spacy.load("en_core_web_sm")

@app.route("/")
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route("/highlight", methods=["POST"])
def highlight_adjectives():
    data = request.json
    text = data.get("text", "")
    doc = nlp(text)

    result = ""
    for token in doc:
        if token.pos_ == "ADJ":
            result += f'<span style="background-color: yellow">{token.text}</span>'
        else:
            result += token.text
        result += token.whitespace_

    return jsonify({"highlighted": result})

if __name__ == "__main__":
    app.run(debug=True)
