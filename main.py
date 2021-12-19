from time import time
import tweepy
from tweepy import api
import sys

def getAllKeys():
    consumer_key = 2
    consumer_secret = 3
    access_token = 4
    access_token_secret = 5
    return consumer_key,consumer_secret,access_token,access_token_secret

def get_progress(file_name,char_num):
    with open(file_name) as f:
        character_all = f.read()
    num_diff = len(character_all) - char_num
    char_num = len(character_all)
    return

if __name__=='__main__':
    file_name = sys.argv[1]
    char_num = 0
    num_diff = 0
    consumer_key,consumer_secret,access_token,access_token_secret = getAllKeys()
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth,file_name,char_num)

    while True:
        char_num,num_diff = get_progress(file_name,char_num)
        tweet_content = "十分間の進捗は"+str(num_diff)+"字です"
        api.update_status(tweet_content)
        time.sleep(600)