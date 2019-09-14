from flask import Flask, render_template, request, jsonify
import os

import tweepy
from textblob import TextBlob

os.environ

consumer_key =  os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']

access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    polarity = TextBlob(tweet.text).sentiment.polarity
    subjectivity = TextBlob(tweet.text).sentiment.subjectivity
    print(f"polarity: {polarity}")
    print(f"subjectivity: {subjectivity}")

# Define the search term and the date_since date as variables
search_words = "aapl"
date_since = "2019-09-10"

tweets = tweepy.Cursor(api.search,
            q = search_words,
            lang = 'en',
            since=date_since).items(5)

for tweet in tweets:
    print(tweet.text)
    polarity = TextBlob(tweet.text).sentiment.polarity
    subjectivity = TextBlob(tweet.text).sentiment.subjectivity
    print(f"polarity: {polarity}")
    print(f"subjectivity: {subjectivity}")