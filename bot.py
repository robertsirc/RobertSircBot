from posts import get_todays_post
from tweets import see_if_tweet_exist, tweet_latest_post
import schedule
import time


def main():
    schedule.every().day.at("09:00").do(run_new_post)

    while True:
        schedule.run_pending()
        time.sleep(1)


def run_new_post():
    print('start')
    post = get_todays_post()
    if post.link:
        if not see_if_tweet_exist(post.link):
            tweet_latest_post(post)
    print('end')


if __name__ == '__main__':
    main()
