import praw
import prawcore
import datetime
import time

reddit = praw.Reddit('bot', user_agent='cs40')

count=0
for submission in reddit.subreddit("SocialDemocracy").hot(limit=None):
    try:
        if submission.selftext:
            reddit.subreddit('BotTown2').submit(submission.title, submission.selftext)
        else:
            reddit.subreddit('BotTown2').submit(submission.title, submission.url)
    except praw.exceptions.RedditAPIException:
        pass
    count+=1
    print('reposted posts and comments =', count)
    time.sleep(15)
