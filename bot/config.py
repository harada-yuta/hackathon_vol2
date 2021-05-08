import tweepy

### APIの認証 ###
# 共通
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

# Bot1
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api1 = tweepy.API(auth1)

# Bot2
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth2.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api2 = tweepy.API(auth2)

# Bot3
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
auth3 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth3.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api3 = tweepy.API(auth3)

# Bot4
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
auth4 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth4.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api4 = tweepy.API(auth4)

# Bot5
ACCESS_TOKEN = "1386176723155251200-bdzc1IhYL4Hy51ubw06qMMDUQkZWBp"
ACCESS_SECRET = "BxxIrMmLXhVLjbR6qYW48mN9CBhefZrLy4Bnu0E5Amc3a"
auth5 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth5.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api5 = tweepy.API(auth5)

# Bot6
ACCESS_TOKEN = "1386177079486550018-hn9nR9MvdtM4tHrXWMH5kRsrdlv2of"
ACCESS_SECRET = "GmuFIfaYUcRGn3a4lTRmIFbPuX0lBMk7vZpLEcLbijniX"
auth6 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth6.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api6 = tweepy.API(auth6)

