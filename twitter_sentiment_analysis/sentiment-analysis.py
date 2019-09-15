from flask import Flask, render_template, request, jsonify
import os

import tweepy
from textblob import TextBlob

consumer_key =  os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']

access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods=["POST"])
def search():
    search_words = request.form.get("search_query")
    t = []
    date_since = "2019-09-10"
    tweets = tweepy.Cursor(api.search,
            q = search_words,
            lang = 'en',
            since=date_since).items(20)

    for tweet in tweets:
        polarity = TextBlob(tweet.text).sentiment.polarity
        subjectivity = TextBlob(tweet.text).sentiment.subjectivity
        t.append([tweet.text,polarity,subjectivity])

    return jsonify({"success": True, "tweets": t})



