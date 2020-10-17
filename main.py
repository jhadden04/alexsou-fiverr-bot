import praw
import time
import csv

reddit = praw.Reddit(client_id='O-gpEre-AApeVw',
                      client_secret='OFL5X-qnNiHx4kIefPJEpLemKCc',
                     user_agent='a reddit instance',
                    username='loverofgirl32',
                     password='pulapula',)
# phrase to trigger the bot
title = 'Brick dealer'
text = '''Hello, I am a BRICK dealer. My Discord: diablo#5179

* Current exchange rate is: 1000 BRICKS= ~35 USD$

You can sell me your BRICKS that you accumulated on the r/FortniteBR subreddit and I will buy them from you.

1. I can pay with Paypal/Other Similar Payment Methods / Gift Cards / In Game Items

2. I am willing to send you the money FIRST, but only for small transactions so I can assure you won't scam me.

3. I can provide proof of a lot of satisfied people who bought from me, I keep a DISCORD channel where I am fully transparent on how I deal with my clients.

4. I know you may think I will try to scam you and I understand you, there are a lot of scammers here I am WILLING to provide all the PROOF you need and be fully transparent that I am 100% LEGIT.


In additional, I am willing to provide you with clarity if you have any questions, you just gotta ask


**** DONT MESSAGE ME HERE, I CAN'T SEE/RESPOND TO YOUR MESSAGES! add on discord: diablo#5179

Make sure you write the discord name WITHOUT capital letters'''
# check every comment in the subreddit
def subspam(subname):
    for comment in reddit.subreddit(subname).stream.comments():
        name = comment.author
        reddit.redditor('name').message(title, text)
        print(name)
        time.sleep(20)
def csvreader():
    with open('redditusernames.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:

            try:
                reddit.redditor(i[0][2:]).message(title, text)
                print(i[0][2:])
                time.sleep(20)
            except Exception as e:
                    print(e)
                    time.sleep(2)
                    continue
csvreader()
