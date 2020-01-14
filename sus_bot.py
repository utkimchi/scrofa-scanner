import tweepy
import logging
from config import create_api
from gbif_occ import hogSearch
from hog_post import hogPost
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
            # and not tweet.favorited
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            # try:
            # 	tweet.favorite()
            # except Exception as e:
            # 	logger.error("Error on fav",exc_info=True)
           
            tLoc = tweet.place.bounding_box.coordinates
            bL = tLoc[0][0]
            tR = tLoc[0][2]

            print('Bounding coordinates are:')
            print ('Left - ', bL[0])
            print ('Right -', tR[0])
            print ('Bottom -', bL[1])
            print ('Top - ', tR[1])
            left = bL[0]
            right = tR[0]
            bottom = bL[1]
            top = tR[1]
            tweeter = tweet.author.screen_name
            tid = tweet.id

            piggie = hogSearch(left,right,top,bottom)
            logger.info(piggie[0])

            message = "@"+tweeter+" "+piggie[0]

            hogPost(piggie[1],message,api,tid)

    return new_since_id

# class MyStreamListener(tweepy.StreamListener):
#     def __init__(self, api):
#         self.api = api
#         self.me = api.me()

#     def on_status(self, tweet):
#         print(f"{tweet.user.name}:{tweet.text}")

#     def on_error(self, status):
#         print("Error detected")

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "HELP","save me"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()