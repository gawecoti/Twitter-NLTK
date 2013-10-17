import twitter
import nltk
from nltk.corpus import stopwords

# Fill in your details
api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='',)

print api.VerifyCredentials()

def get_tweets(num_tweets):

    NUM_TWEETS = num_tweets
    i = 1

    tweets = []
    sample_tweets = api.GetStreamSample()

    # Get N tweets in English
    for tweet in sample_tweets:
        if i > NUM_TWEETS:
            break
        if tweet.has_key('id') and tweet['lang'] == 'en':
            tweets.append(tweet['text'].lower())
            i += 1

    sample_tweets.close()
    return tweets

def process(tweets):

    words = []
    add_stopwords = [u'@', u':', u'rt', u',', u'!', u'#', u'http', u'.', u'?', u';', u'&']

    print 'Processing...'

    # Word tokenize each tweet and put it into a single list
    for t in tweets:
        words += nltk.word_tokenize(t)

    # Remove stopwords from word list
    words = [word for word in words if (word not in stopwords.words('english')) and (word not in add_stopwords)]

    return nltk.FreqDist(words).items()

if __name__ == "__main__":
    tweets = get_tweets(500)
    print process(tweets)

