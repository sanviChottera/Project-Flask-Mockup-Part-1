from flask import Flask, jsonify
import csv

all_articles = []
with open("articles.csv" , encoding='utf-8' )as f:
    r = csv.reader(f)
    data = list(r)
    all_articles = data[1:]

like_articles = []
unliked_articles = []


app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome"

@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data":all_articles[0], "status":"success"
    })


@app.route("/liked-articles", methods = ["POST"] )
def like_articles():
    article = all_articles[0]
    like_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movies", methods = ["POST"] )
def unliked_movie():
    article = all_articles[0]
    unliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201


if __name__ == "__main__":
    app.run(debug = True)