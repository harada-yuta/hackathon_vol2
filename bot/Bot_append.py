### consumer_tokenとconsumer_secretからredirect_urlを取得 ###

import tweepy
consumer_token = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
redirect_url = auth.get_authorization_url()
print(redirect_url)


### oauth_tokenとoauth_verifierからaccess_tokenを取得 ###
import  sys

from requests_oauthlib import OAuth1Session
from urllib.parse import parse_qsl

base_url = 'https://api.twitter.com/'
access_token_url = base_url + 'oauth/access_token'

oauth_token = ""
oauth_verifier = ""

sys.stderr.write("*** 開始 ***\n")

twitter = OAuth1Session(
        consumer_token,
        consumer_secret,
        oauth_token,
        oauth_verifier,
    )

response = twitter.post(
        access_token_url,
        params={'oauth_verifier': oauth_verifier}
    )

access_token = dict(parse_qsl(response.content.decode("utf-8")))

print(access_token)
sys.stderr.write("*** 終了 ***\n")
