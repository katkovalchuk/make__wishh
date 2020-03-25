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
        
def wish_time():
    os.environ['TZ'] = 'Europe/Kiev'
    time.tzset()
    current_time = time.strftime("%H:%M")
    splited_time = currentTime.split(":")
    
    perfect_time = ''
    exceprion_time = ['01:01', '02:02', '03:03', '04:04', '05:05', '06:06', '07:07', '08:08', '09:09']
    
    if splited_time[0] == splited_time[1]:
        perfect_time = splited_time[0]+':'+ splited_time[1]
    
    if perfect_time is True and perfect_time not in exception_time:
        api.update_status('It\'s ' + perfect_time +'! Make a wish!')

while True:
    wish_time()
    time.sleep(60)
