import praw
import time
import csv

reddit = praw.Reddit(client_id='**',
                      client_secret='**',
                     user_agent='a reddit instance',
                    username='**',
                     password='**',)
# phrase to trigger the bot
title = 'General'
text = 'Kenobi'
# check every comment in the subreddit
def subspam(subname):
    for comment in reddit.subreddit(subname).stream.comments():
        name = comment.author
        reddit.redditor('name').message(title, text)
        comment.reply('hello')
        print(name)
        time.sleep(5)
def csv():
    with open('redditusernames.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            try:
                reddit.redditor(i[0][2:]).message(title, text)
                print(i[0][2:])
            except:
                continue
subspam('myreddittesting')
