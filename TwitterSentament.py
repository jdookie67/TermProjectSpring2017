import got
import sys
import re
from textblob import TextBlob
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt
from datetime import datetime
avgList = []
dateList = []
maxtw = 125000
Saverage = 0
Syear = 2015
Eyear = 2018


def printTweet(descr, t):
    print(descr)
    print("Username: %s" % t.username)
    print("Retweets: %d" % t.retweets)
    print("Text: %s" % t.text)
    print("Mentions: %s" % t.mentions)
    print("Hashtags: %s\n" % t.hashtags)


def normalize_tweet(x):
    x = " ".join(x.split())
    x = x.lower()
    x = re.sub("http[^ ]+", "", x)
    x = re.sub("#+", "", x)
    x = re.sub("(@+ )*@+", "", x)
    for punc in [".", ",", "?", "!"]:
        x = re.sub("[{}]+".format(punc), " " + punc, x)
    x = x.replace("n't", " not")
    x = " ".join(x.split())
    x = x.lstrip("MENTION ")
    return x.strip()


def receiveBuffer(tweets):
    total = 0
    count = 0
    print("processing tweet set")
    for t in tweets:
        ft = normalize_tweet(t.text)

        try:
            tbl = TextBlob(ft)
            sen = tbl.sentiment.polarity
            total = total + sen
            count = count + 1
            # print sen

            # print("Text: %s" % ft +" "+str(total))
        except:
            print("line omitted")
    print total, count
    append(total, count)


def append(total, count):
    print "appending"
    avgList.append(total / count)


def search(query, maxtw, avgList, dateList, year, smonth, emonth):
    for month in range(smonth, emonth + 1):
        sMonth = ""
        if datetime.now().year == year and datetime.now().month < month:
            break
        if month < 10:
            sMonth = "0" + str(month)
        else:
            sMonth = str(month)
        Startday = str(year) + "-" + sMonth + "-" + "1"
        endDay = str(year) + "-" + sMonth + "-" + "28"
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(Startday).setUntil(endDay).setMaxTweets(maxtw)
        # print(Startday+" "+endDay)
        got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer, maxtw)
        dateList.append(Startday)
        print avgList, dateList


for year in range(Syear, Eyear):
    search("realDonaldTrump", maxtw, avgList, dateList, year, 1, 12)
date_object = [datetime.strptime(date, '%Y-%m-%d').date() for date in dateList]
x = date_object
y = avgList
fig = plt.figure(figsize=(6.5, 5))
ax = fig.add_subplot(111)
ax.plot_date(x, y)
fig.savefig('C:\\Users\\Josh\\Documents\\test.png')
plt.plot(x, y)
plt.ylabel('Trump Sentament over time')
plt.show()
