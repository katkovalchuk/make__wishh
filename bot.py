import tweepy 

CONSUMER_KEY = 'PttCikEHkWuNErM3bCMhKdJ74'
CONSUMER_SECRET = 'fh0mBe0nxrEvi6DHoBJhlMsR89PNtyFRJ7xb8gQZzuJ3V2d0t7'
ACCESS_KEY = '1237398688567308288-8YX1jWRiuPGBGgjTpL0vcvgGt1NPIk'
ACCESS_SECRET = 'HpwIs7afOGxoCR8RsXHokNxJWTgWBwwAsagnCoeUA2rrn'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

import time
def wishTime():
    currentTime = time.strftime("%H:%M")
    splitedTime = currentTime.split(":")
    
    perfectTime = []
    if splitedTime[0] == splitedTime[1]:
        perfectTime = splitedTime[0]+':'+ splitedTime[1]
    return str(perfectTime)

while True:
    api.update_status('It\'s ' + wishTime() +'! Make a wish!')