import os
from markovbot import MarkovBot
from keys import keyReturn


# # # # #
# INITIALISE

# Initialise a MarkovBot instance
tweetbot = MarkovBot()


# # # # #
# TEXT GENERATION

# Generate text by using the generate_text method:
#   The first argument is the length of your text, in number of words
#   The 'seedword' argument allows you to feed the bot some words that it
#   should attempt to use to start its text. It's nothing fancy: the bot will
#   simply try the first, and move on to the next if he can't find something
#   that works.
my_first_text = "MY WIFE"

# Print your text to the console
print(u'\ntweetbot says: "%s"' % (my_first_text))


# # # # #
# TWITTER

keyAccess = keyReturn()

# Consumer Key (API Key)
cons_key = keyAccess.getConsumerKey()
# Consumer Secret (API Secret)
cons_secret = keyAccess.getConsumerKeySecret()
# Access Token
access_token = keyAccess.getAccessToken()
# Access Token Secret
access_token_secret = keyAccess.getAccessTokenSecret()

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# The target string is what the bot will reply to on Twitter. To learn more,
# read: https://dev.twitter.com/streaming/overview/request-parameters#track
targetstring = 'my wife'
# Keywords are words the bot will look for in tweets it'll reply to, and it
# will attempt to use them as seeds for the reply
keywords = []
# The prefix will be added to the start of all outgoing tweets.
prefix = None
# The suffix will be added to the end of all outgoing tweets.
suffix = 'MY WIFE'
# The maxconvdepth is the maximum depth of the conversation that the bot will
# still reply to. This is relevant if you want to reply to all tweets directed
# at a certain user. You don't want to keep replying in the same conversation,
# because that would be very annoying. Be responsible, and allow your bot only
# a shallow conversation depth. For example, a value of 2 will allow the bot
# to only reply in conversations where there are two or less replies to the
# original tweet.
maxconvdepth = None

# Start auto-responding to tweets by calling twitter_autoreply_start
# This function operates in a Thread in the background, so your code will not
# block by calling it.
tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)
 
# Start periodically tweeting. This will post a tweet every X days, hours, and
# minutes. (You're free to choose your own interval, but please don't use it to
# spam other people. Nobody likes spammers and trolls.)
# This function operates in a Thread in the background, so your code will not
# block by calling it.
tweetbot.twitter_tweeting_start(days=0, hours=19, minutes=30, keywords=None, prefix=None, suffix='MY WIFE')

# DO SOMETHING HERE TO ALLOW YOUR BOT TO BE ACTIVE IN THE BACKGROUND
# You could, for example, wait for a week:
secsinweek = 7 * 24 * 60
time.sleep(secsinweek)
 
# Use the following to stop auto-responding
# (Don't do this directly after starting it, or your bot will do nothing!)
tweetbot.twitter_autoreply_stop()

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
tweetbot.twitter_tweeting_stop()