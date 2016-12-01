from TwitterAPI import TwitterAPI, TwitterRestPager


WORDS_TO_COUNT = ['lion', 'wildbeest', 'snake']


API_KEY = 'NZow9q4lgFxhPw2omwqJ2VtIj'
API_SECRET = 'r5fYLio2Da9T6n9TcgasSWLuTV0KPkInOo4mddSfotNX9VfArM'
ACCESS_TOKEN = '1538574218-U5Y8z6DsJJKT0xwHBqIs4tygi048fBLwtwMgNtU'
ACCESS_TOKEN_SECRET = 'cKeAv9F67ckA8UynkGalpzaQTwtx2NAjWTwt2DtR20VpN'


api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
words = ' OR '.join(WORDS_TO_COUNT)
counts = dict((word,0) for word in WORDS_TO_COUNT)


def process_tweet(text):
	text = text.lower()
	for word in WORDS_TO_COUNT:
		if word in text:
			counts[word] += 1
	print(counts)


r = TwitterRestPager(api, 'search/tweets', {'q':words, 'count':100})
for item in r.get_iterator(wait=6):
	if 'text' in item:
		process_tweet(item['text'])
	elif 'message' in item and item['code'] == 88:
		print('\n*** SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message'])
		break
