import praw
import random
import datetime
import time
from textblob import TextBlob

reddit = praw.Reddit('bot', user_agent='cs40')

count=0
while True:
    the_submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=None))) 
    print('submission.title=',the_submission.title)
    print('submission.url=',the_submission.url)
    text_of_submission = TextBlob(the_submission.title+the_submission.selftext)
    if ("biden" in text_of_submission.lower() and text_of_submission.sentiment.polarity>0.6):
        the_submission.upvote()
        count+=1
        print("upvoted submission. This is action #", count)
    if ("biden" in text_of_submission.lower() and text_of_submission.sentiment.polarity<-0.6):
        the_submission.downvote()
        count+=1
        print("upvoted submission. This is action #", count)
    the_submission.comments.replace_more(limit=None)
    all_comments = the_submission.comments.list()
    print("len_all_comments =", len(all_comments))
    for comment in all_comments:
        text_of_comment = TextBlob(comment.body)
        if ("biden" in text_of_comment.lower() and text_of_comment.sentiment.polarity>0.6):
            comment.upvote()
            count+=1
            print("upvoted submission. This is action #", count)
        if ("biden" in text_of_comment.lower() and text_of_comment.sentiment.polarity<-0.6):
            comment.downvote()
            count+=1
            print("upvoted submission. This is action #", count)
    
