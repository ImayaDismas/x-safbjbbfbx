import tweepy
import json
from tweepy import OAuthHandler
consumer_key = 'NZow9q4lgFxhPw2omwqJ2VtIj'
consumer_secret = 'r5fYLio2Da9T6n9TcgasSWLuTV0KPkInOo4mddSfotNX9VfArM'
access_token = '1538574218-U5Y8z6DsJJKT0xwHBqIs4tygi048fBLwtwMgNtU'
access_secret = 'cKeAv9F67ckA8UynkGalpzaQTwtx2NAjWTwt2DtR20VpN'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    data = json.dumps(tweet)
    with open('python.json', 'a') as f:
                f.write(data)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     process_or_store(status._json)

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

# for tweet in tweepy.Cursor(api.user_timeline).items():
#     process_or_store(tweet._json)
