import praw
import random
import datetime
import time

madlibs = [
    "Biden is [WONDERFUL]. I've [MET] him many times in the White House. Do not [CONFUSE] him with Grandpa Joe, as that man is [HORRIBLE] at [SINGING].",
    "Biden and Kamala are [FUN]. I've [LEARNED] many things from these [PEOPLE]. It is a [RARE] experience to meet such great patriots in my [LIFETIME].",
    "America is a [COLD] place. Biden will [DO] [MANY] things to make this [COUNTRY] better for ALL americans. Please [VISIT] the White House and see our national hero!",
    "Democrats like Biden are very [HUMBLE]. They are from [AMERICA] where good things [OFTEN] happen. Do [BUY] a Biden T-shirt [SOON]!",
    "Biden is a [NICE] [PERSON] to [EAT] [TASTELESS] White House [FOOD] with. This is why you should vote for him!!",
    "What is the [MEANING] of Biden's win? I [ASK] this [QUESTION] [MULTIPLE] times a day. I [HOPE] you understand that Biden won because God said he should!"
    ]

replacements = {
    'WONDERFUL' : ['wonderful', 'amazing', 'interesting'],
    'MET' : ['met', 'seen', 'watched'],
    'CONFUSE' : ['confuse', 'befuddle', 'confound'],
    'HORRIBLE' : ['awful', 'terrible', 'idiotic'],
    'SINGING'  : ['singing', 'chanting', 'crooning'],
    'FUN' : ['fun', 'enjoyable', 'exciting'],
    'LEARNED' : ['learned', 'studied', 'read'],
    'PEOPLE' : ['people', 'humans'],
    'RARE' : ['rare', 'unique', 'uncommon'],
    'LIFETIME'  : ['lifetime', 'days', 'lifepath'],
    'COLD' : ['cold', 'freezing', 'icy'],
    'MANY' : ['many', 'lots of', 'a lot of'],
    'DO' : ['do', 'try', 'explore'],
    'COUNTRY' : ['country', 'nation', 'land'],
    'VISIT'  : ['visit', 'come', 'explore'],
    'HUMBLE' : ['humble', 'down to earth'],
    'AMERICA' : ['america', 'murica', 'the united states'],
    'OFTEN' : ['often', 'frequently', 'regularily'],
    'BUY' : ['buy', 'purhcase', 'get'],
    'SOON' : ['soon', 'in the near-term'],
    'PERSON' : ['person', 'human', 'human being'],
    'NICE' : ['nice', 'calm', 'cool'],
    'EAT' : ['eat', 'chew', 'ingest'],
    'TASTELESS' : ['tasteless', 'disgusting', 'unappetizing'],
    'FOOD' : ['food', 'grub', 'meals'],
    'MEANING' : ['meaning', 'purpose', 'goal'],
    'ASK' : ['ask', 'ponder'],
    'QUESTION' : ['question', 'query', 'inquiry'],
    'MULTIPLE' : ['multiple', 'a bunch of'],
    'HOPE' : ['hope', 'wish', 'anticipate']
    }


# copy your generate_comment function from the madlibs assignment here
def generate_comment():
    s = random.choice(madlibs)
    for k in replacements.keys():
	    s = s.replace('['+k+']', random.choice(replacements[k]))
    return s


# connect to reddit 
reddit = praw.Reddit('bot', user_agent='cs40')


# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'ryanbotryan':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented', has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_with_no_replies=[]
        for comment in not_my_comments:
            did_not_reply=True
            for reply in comment.replies:
                if reply.author == 'ryanbotryan':
                    did_not_reply= False
            if did_not_reply:
                comments_with_no_replies.append(comment)
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_with_no_replies)=',len(comments_with_no_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        if len(comments_with_no_replies) > 0:
            comment_scores=[]
            for comment in comments_with_no_replies:
                comment_scores.append(comment.score)
            max_comment_score = max(comment_scores)
            index = comment_scores.index(max_comment_score)
            comment = comments_with_no_replies[index]
            if comment.author is 'ryanbotryan':
                comment = random.choice(comments_with_no_replies)
            try:
                comment.reply(generate_comment())
            except praw.exceptions.APIException:
                print('not replying to a comment that has been deleted')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions

    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=None)))

    print (submission.title)

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(5)