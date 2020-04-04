import tweepy
from configuration import CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


def see_if_tweet_exist(post_url):
    tweets = api.user_timeline()
    for tweet in tweets:
        if tweet['entities']['urls']:
            urls = tweet['entities']['urls']
            for url in urls:
                if url['expanded_url'] == post_url:
                    return True
    return False


def tweet_latest_post(post):
    api.update_status(build_tweet(post))


def build_tweet(post):
    return 'Latest write up: ' + post.title + ' ' + post.link


