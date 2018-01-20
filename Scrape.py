from twython import Twython
from twython import TwythonStreamer
import sys
import os
import subprocess

# Application Key and Application Secret from app.twitter.com
APP_KEY = 'Enter Here'
APP_SECRET = 'Enter Here'
ACCESS_TOKEN = 'Enter Here'

OAUTH_TOKEN = 'Enter Here'
OAUTH_TOKEN_SECRET = 'Enter Here'


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        temp = 0
        if True:
            if 'retweet_count' in data:
                temp = data['retweet_count']
                print(temp)
                temp = int(temp)
                print(temp)
            if 'text' in data:
                user = data['user']
                print(data['id_str'])
                print(user['screen_name'])
                print(data['contributors'])
                print(data['retweet_count'])
                print(data['text'].encode('ascii', 'ignore'))
            if 'media' in data:
                print(data['media'])
        print('\n')

    def on_error(self, status_code, data):
        print(status_code, data)


def getToken():
    twitter = Twython(APP_KEY, APP_SECRET,  oauth_version=2)
    print(twitter.obtain_access_token())


def getStatus(tweetID):
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        results = twitter.show_status(id=tweetID)
        return results


def getTimeline(screenName, tweetCount, excludeReplies, files):
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    results = twitter.get_user_timeline(screen_name=screenName, count=tweetCount)
    for result in results:
            dataprocess(result, files)


def currentTime():
    currentTime = time.strftime('%Y-%m-%d--%H-%M-%S')
    return currentTime


def dataprocess(status, file):
    ent = status['entities']
    us = status['user']
    # why try catch you say. im lazy.
    try:
        ent = status['entities']
        us = status['user']
        has = ent['hashtags']

        try:
            has1 = has[0]
            has2 = has1['text']
        except Exception as e:
            has2 = "N/A"
        try:
            med = ent['media']
            string = med[0]
            videoProcess(string['expanded_url'])

        except Exception as e:
            string = {'expanded_url': 'N/A'}
        try:
            typ = status['extended_entities']
            typ1 = typ['media']
            typ2 = typ1[0]
        except Exception as e:
            typ2 = {'type': 'Text'}
        string = str(us['screen_name'] + " " + status['text'] + " " + has2 + " " + string['expanded_url'] + " " + typ2['type']) + '\n'
        string.encode(sys.stdout.encoding, errors='replace')

        # file.write(str("[{text:" +status['text'] +",intent: None,entities:[{entity: FamilyMember,startPos: 4,endPos: 6}]},"))
        print(string)
        file.write(string)

    except Exception as e:
        # should never get here if it does we fucked
        print(e)
        print(us['screen_name'], status['text'], "fuck")


def videoProcess(vidURL):
    if(not(vidURL is 'N/A')):
        os.system("you-get " + vidURL)
    return

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#stream.statuses.filter(track=' MAGA')


output = open("out.txt", 'w')
getTimeline('@realDonaldTrump', 5, True, output)
# getStatus()
# status= getStatus(918960024256434176)#(vid) 918960024256434176 (pic) 918894502185787392 (text) 919009334016856065
