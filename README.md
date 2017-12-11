# TermProject2017
This is the collection of code for the term related to twitter

Description: TwitterSentament.py
This software is used to access and perform sentiment anlysis on tweets from certain indivduals or topics.

Installation:
This software requires several things to be installed in order to use
First install anaconda for python 2.7
Then using open command prompt and run: pip install -U textblob , pip install -U lxml , pip install -U pyquery
Then go to https://github.com/Jefferson-Henrique/GetOldTweets-python and download a copy of the repo.
Once downloaded navigate to your sitepackages folder for your python installtion.
	This will be found inside of your anaconda folder under Lib then Site-Packages
Then drag the "got" folder from the "GetOldTweets-pythonMaster" into the python 2 site packes folder.
I suggest then opening a python terminal and run import got. 

If it works then you are ready to start the scipt.

Usage:

Once opened you can adjust the number of tweets sampled by changeing maxtw to a different value.
to do a diffent set of years adjust the Syear and Eyear varibles. note Eyear needs to be set to 1 year over the target end year.
I.E if you want to end in 2017 then Eyear is 2018. If you want to end in 2016 Eyear should be 2017 ect.
then simply use the restart and run all cells command in jupyter. 
Note that this will take a large amount of time to demo. So the larger your sample size the more time it will take.
For a quick demo I recommend setting it to ~10 tweets. For a deep analysy set it higher but leave the screen open and running.
It will update you when a month has been completed with an appending message.


Description: Scrape.py
This software uses the offical twitter api in order to gather tweets and their media content.

Installation:

This requires python 2.7, twython, and you-get
you-get works best as a command line utility and not a python module.
Therefore it needs to be added to the computers path and should be accesible by typeing you-get in the command prompt
Once it is done you should be able to run the program

Usage: 
Inside the code change the line getTimeline('username', (number of tweets) , True, output)
this will aloow you to grab tweets from different time lines as well as all associated media on the timeline.
