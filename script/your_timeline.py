import json
import config
import csv
from requests_oauthlib import OAuth1Session
from datetime import datetime

def my_timeline():
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params ={'screen_name': 'hirasawa','count' : 200}# JoeBiden
    header = ['id','User Name','User ID','Follows','Followers','User Location','content','time']
    req = twitter.get(url, params = params)
    if req.status_code == 200:
        with open('susumu_timeline_2.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            timeline = json.loads(req.text)
            for tweet in timeline:
                tmp = []
                tmp.append(tweet['id'])
                tmp.append(tweet['user']['name'])
                tmp.append(tweet['user']['screen_name'])
                tmp.append(tweet['user']['friends_count'])
                tmp.append(tweet['user']['followers_count'])
                tmp.append(tweet['user']['location'])
                tmp.append(tweet['text'])
                date = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S %z %Y')
                tmp.append(f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}:{date.second}")
                writer.writerow(tmp)
    else:
        print("ERROR: %d" % req.status_code)

if __name__ == '__main__':
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)
    my_timeline()