import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = '-'
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

import time, os
#import sys

def wish_time():
    os.environ['TZ'] = 'Europe/Kiev'
    time.tzset()
    current_time = time.strftime("%H:%M")
    splited_time = current_time.split(":")
    
    perfect_time = ''
    exception_time = ['01:01', '02:02', '03:03', '04:04', '05:05', '06:06', '07:07', '08:08', '09:09']
    
    if splited_time[0] == splited_time[1]:
        perfect_time = splited_time[0]+':'+ splited_time[1]
    
    if bool(perfect_time) is True and perfect_time not in exception_time:
        api.update_status('It\'s ' + perfect_time +'! Make a wish!')

def delete_old_tweets():
    for status in tweepy.Cursor(api.user_timeline).pages():
        i = 0
        while i < len(status):
            if str(status[i].created_at.date()) != time.strftime("%Y-%m-%d"):
                api.destroy_status(status[i].id)
                #print("Deleted:", status[i].id)
            i = i + 1

while True:
    wish_time()
    time.sleep(60)

while True:
    delete_old_tweets()
    time.sleep(60)
   #time.sleep(86400) sys.stdout.flush()
