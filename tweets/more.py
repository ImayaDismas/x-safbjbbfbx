#!/usr/bin/env python3
# %matplotlib inline
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import json
import pandas as pd
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import rcParams
from matplotlib import style
from matplotlib import dates
from datetime import datetime
import seaborn as sns
import time
import os
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import random

# from IPython import get_ipython
# get_ipython().run_line_magic(u'matplotlib inline')

# Seaborn plots
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
# for R lovers :)
style.use('ggplot')
rcParams['axes.labelsize'] = 9
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['legend.fontsize'] = 7
# rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Computer Modern Roman']
rcParams['text.usetex'] = False
rcParams['figure.figsize'] = 20, 10

access_token = "1538574218-D1Wf4IDzXIM909gsVsJqDXmRdkLk3WJouDg6Wof"
access_token_secret = "pCW35DBdIKMsb3DBsyo5rsfs4Byw6YgQNNOMIWJKQ4671"
consumer_key = "ixKovylDZWX6UMt7VnQks6vyD"
consumer_secret = "d13SZQDImUIwhedjwKM3abeMTjPZPzlISFcdkOweXXrtIx2i1n"

MAX_TWEETS = 8000

# This handles Twitter authentication and the connection to Twitter Streaming API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth, wait_on_rate_limit=True)

data = Cursor(api.search, q='TeamMganga').items(MAX_TWEETS)

mozsprint_data = []
# You will use this line in production instead of this
# current_working_dir = os.path.dirname(os.path.realpath(__file__))
current_working_dir = "./"
log_tweets = current_working_dir  + str(time.time()) + '_moztweets.txt'
with open(log_tweets, 'w') as outfile:
    for tweet in data:
        mozsprint_data.append(json.loads(json.dumps(tweet._json)))
        outfile.write(json.dumps(tweet._json))
        outfile.write("\n")

print (mozsprint_data[0])
# Create the dataframe we will use
tweets = pd.DataFrame()
# We want to know when a tweet was sent
print (mozsprint_data['created_at'][0])
tweets['created_at'] = map(lambda tweet: time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')), mozsprint_data)
# Who is the tweet owner
tweets['user'] = map(lambda tweet: tweet['user']['screen_name'], mozsprint_data)
# How many follower this user has
tweets['user_followers_count'] = map(lambda tweet: tweet['user']['followers_count'], mozsprint_data)
# What is the tweet's content
tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), mozsprint_data)
# If available what is the language the tweet is written in
tweets['lang'] = map(lambda tweet: tweet['lang'], mozsprint_data)
# If available, where was the tweet sent from ?
tweets['Location'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, mozsprint_data)
# How many times this tweet was retweeted and favorited
tweets['retweet_count'] = map(lambda tweet: tweet['retweet_count'], mozsprint_data)
tweets['favorite_count'] = map(lambda tweet: tweet['favorite_count'], mozsprint_data)

print(tweets.head())

# list_of_original_tweets = [element for element in tweets['text'].values if not element.startswith('RT')]
# print (list_of_original_tweets[0])
# print ("Number of Original Tweets : " + str(len(list_of_original_tweets)))
#
# list_of_retweets = [element for element in tweets['text'].values if element.startswith('RT')]
#
#
# print ("Number of Retweets : " + str(len(list_of_retweets)))

# General plotting function for the different information extracted
def plot_tweets_per_category(category, title, x_title, y_title, top_n=5, output_filename="plot.png"):
    """
    :param category: Category plotted, can be tweets users, tweets language, tweets country etc ..
    :param title: Title of the plot
    :param x_title: List of the items in x
    :param y_title: Title of the variable plotted
    :return: a plot that we can save as pdf or png instead of displaying to the screen
    """
    tweets_by_cat = category.value_counts()
    fig, ax = plt.subplots()
    ax.tick_params(axis='x')
    ax.tick_params(axis='y')
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.set_title(title)
    tweets_by_cat[:top_n].plot(ax=ax, kind='bar')
    fig.savefig(output_filename)
    fig.show()

plot_tweets_per_category(tweets['lang'], "#mozsprint by Language",
                             "Language",
                             "Number of Tweets",
                             2000,
                             "mozsprint_per_language.png")

plot_tweets_per_category(tweets['Location'],
                             "#mozsprint by Location",
                             "Location",
                             "Number of Tweets", 2000,
                             "mozsprint_per_location.png")

plot_tweets_per_category(tweets['user'],
                             "#mozsprint active users",
                             "Users",
                             "Number of Tweets", 20,
                             "mozsprint_users.png")
def plot_distribution(category, title, x_title, y_title, output_filename="plot.png"):
        """
        :param category: Category plotted, can be users, language, country etc ..
        :param title: Title of the plot
        :param x_title: List of the items in x
        :param y_title: Title of the variable plotted
        :return: a plot that we can save as pdf or png instead of displaying to the screen
        """
        fig, ax = plt.subplots()
        ax.tick_params(axis='x')
        ax.tick_params(axis='y')
        ax.set_xlabel(x_title)
        ax.set_ylabel(y_title)
        ax.set_title(title)
        sns.distplot(category.values, rug=True, hist=True);
        fig.savefig(output_filename)

# plot_distribution(tweets['retweet_count'],
#                   "#mozsprint retweets distribution", "", "",
#                   "retweets_distribution.png")

df = pd.DataFrame(tweets['created_at'].value_counts(), columns=['number_tweets'])
df['date'] = df.index
df.head()

days = [item.split(" ")[0] for item in df['date'].values]
df['days'] = days
grouped_tweets = df[['days', 'number_tweets']].groupby('days')
tweet_growth = grouped_tweets.sum()
tweet_growth['days']= tweet_growth.index

tweet_growth

import numpy as np
fig = plt.figure()
ax = plt.subplot(111)
x_pos = np.arange(len(tweet_growth['days'].values))
ax.bar(x_pos, tweet_growth['number_tweets'].values, align='center')
ax.set_xticks(x_pos)
ax.set_title('#mozfest hashtag growth')
ax.set_ylabel("number tweets")
ax.set_xticklabels(tweet_growth['days'].values)
fig.savefig('mozfest_growth.png')
