import tweepy
import os
import json
import sys
import geocoder

# API keys and tokens
# open a file called 'keys' with keys and tokens for this API
keyFile = open('keys.txt', 'r')
bearer_token = keyFile.readline().rstrip()
consumer_key = keyFile.readline().rstrip()
consumer_secret = keyFile.readline().rstrip()
access_token = keyFile.readline().rstrip()
access_token_secret = keyFile.readline().rstrip()

client = tweepy.Client(
	bearer_token=bearer_token,
	consumer_key = consumer_key,
	consumer_secret = consumer_secret,
	access_token = access_token,
	access_token_secret = access_token_secret
)

# recent tweeks from Barack Obama
query = 'from:BarackObama -is:retweet'
response = client.search_recent_tweets(query=query,
tweet_fields=['author_id', 'created_at'],
max_results=100)

print(response)

