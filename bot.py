import tweepy

CONSUMER_KEY = 'PttCikEHkWuNErM3bCMhKdJ74'
CONSUMER_SECRET = 'fh0mBe0nxrEvi6DHoBJhlMsR89PNtyFRJ7xb8gQZzuJ3V2d0t7'
ACCESS_KEY = '1237398688567308288-8YX1jWRiuPGBGgjTpL0vcvgGt1NPIk'
ACCESS_SECRET = 'HpwIs7afOGxoCR8RsXHokNxJWTgWBwwAsagnCoeUA2rrn'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

import time
import os

def delete_old_tweets():
    for status in tweepy.Cursor(api.user_timeline).pages():
        i = 0
        while i < len(status):
            if str(status[i].created_at.date()) != time.strftime("%Y-%m-%d"):
                api.destroy_status(status[i].id)
                print("Deleted:", status[i].id)
            i = i + 1
        
def wishTime():
    os.environ['TZ'] = 'Europe/Kiev'
    time.tzset()
    currentTime = time.strftime("%H:%M")
    splitedTime = currentTime.split(":")
    
    perfectTime = ''
    exceprion_time = ['01:01', '02:02', '03:03', '04:04', '05:05', '06:06', '07:07', '08:08', '09:09']
    
    if splitedTime[0] == splitedTime[1] and splitedTime[0] not in exceprion_time:
        perfectTime = splitedTime[0]+':'+ splitedTime[1]
        
    if perfectTime:
        api.update_status('It\'s ' + perfectTime +'! Make a wish!')

while True:
    wishTime()
    time.sleep(60)
