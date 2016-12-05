import tweepy
import callerpy
from facepy import GraphAPI
"""to do 
1. obtain user input
2. search local database depending on input
3. search for any blank fields
4. update local database on demand

"""
def User:
    def __init__(self,userID,name,phone,email)
        self.userID = userID
	self.name = name
	self.phone = phone
	self.email = email
	self.alias = ""
def searchFacebook(user):

    {
    """todo obtain authentication token
    this may require a login implementation
    """
    graph = GraphAPI(access_token)
    graph.search(username, user.name, page=False, retry=3)
    }

def searchTwitter(user):

    {
    """search user details in twitter
    """
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)


    results = api.search(q="user.name")

    for result in results:
        print result.text
    }

def searchTruecaller(user):

    {
    """search number and name in truecaller
    """

    }

def searchOlx(user):

    {
    """search for details in olx
    """

    }
