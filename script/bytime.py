import json
import config
from requests_oauthlib import OAuth1Session
import csv

import time
import schedule
from datetime import datetime

def main(from_date="201906010000", to_date="201907010000",res = None):
    url = "https://api.twitter.com/1.1/tweets/search/fullarchive/MyPortfolio.json"
    keyword = "コロナ"
    params = {'query' : keyword, 'maxResults' : 100,'fromDate':from_date,'toDate':to_date}

    #CSVのヘッダーを定義
    header = ['id','User Name','User ID','Follows','Followers','User Location','content','time']
    search_timeline = {}

    #リクエスト
    result = twitter.get(url, params = params)

    with open("daily.csv",'a') as f:
        search_timeline = json.loads(result.text)
        writer = csv.writer(f)
        writer.writerow(header)
        for tweet in search_timeline['results']:
            tmp = []
            tmp.append(tweet['id'])
            tmp.append(tweet['user']['name'])
            tmp.append(tweet['user']['screen_name'])
            tmp.append(tweet['user']['friends_count'])
            tmp.append(tweet['user']['followers_count'])
            tmp.append(tweet['user']['location'])
            tmp.append(tweet['text'])
            tmp.append(tweet['created_at'])
            writer.writerow(tmp)
            tmp = []
    

if __name__ == '__main__':
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)

    schedule.every().day.at("00:08").do(main)
  
    while True:
        schedule.run_pending()
        time.sleep(60)