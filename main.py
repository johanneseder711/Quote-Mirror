from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

@app.route("/")
def home():
    quote = []
    author = []
    with open('Lebensweisheiten.txt') as f:
        for line in f.readlines():
            if line != '\n':
                sentence = line.strip()
                if sentence.startswith('„'):
                    quote.append(sentence)
                else:
                    author.append(sentence)
    dictionary = dict(zip(author,quote))
    random_author = random.choice(author)
    quote_ = dictionary[random_author]
    return(render_template("index.html",  author=random_author, quote=quote_))

if __name__ == "__main__":
    app.run(debug = True)
