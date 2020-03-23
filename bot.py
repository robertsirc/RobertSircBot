import sys
import tweepy
from configuration import *
from posts import *
from tweets import *


def main():
    print('start')
    post = get_todays_post()
    if post.link:
        if not see_if_tweet_exist(post.link):
            tweet_latest_post(post)


if __name__ == '__main__':
    main()