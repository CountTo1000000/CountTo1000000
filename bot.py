import tweepy
import time
import datetime

consumer_key= (process.env.TOKEN1)
consumer_secret= (process.env.TOKEN2)
access_token= (process.env.TOKEN3)
access_token_secret= (process.env.TOKEN4)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

i = 1
number = 1
while i <= 2:
        api.update_status(number)
        number = number + 1
        time.sleep(3600)
