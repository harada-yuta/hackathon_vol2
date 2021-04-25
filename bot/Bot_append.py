### consumer_tokenとconsumer_secretからredirect_urlを取得 ###

import tweepy
consumer_token = "mijOOpiHSv2RvgKIiXlKm4irr"
consumer_secret = "oifeayG9YAYkkMbBd1blPe8SmmJLliYphD87xBrEsqv2QrU2PH"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
redirect_url = auth.get_authorization_url()
print(redirect_url)

# reply_type2
# https://twitter.com/home?oauth_token=i0ZTfAAAAAABEwZ7AAABeO320u8&oauth_verifier=bMzpGo6E2jB1UjSAEuVqr1BUeyw900R6
# reply_type3
# https://twitter.com/home?oauth_token=vOzhJAAAAAABEwZ7AAABeO36noI&oauth_verifier=sege2uURlnd4lqt6e7gQiKfbJKejnfPE
# reply_bot4
# https://twitter.com/home?oauth_token=UEFQvAAAAAABEwZ7AAABeQdVtZs&oauth_verifier=Vxfrvz5QE74UvFr7mHI91XeFIEHii9IK
# reply_bot5
# https://twitter.com/home?oauth_token=9bPAcAAAAAABEwZ7AAABeQdX96E&oauth_verifier=qGMOPB1yYbfXjuprpKjPSvCGyqo72QWM
# reply_bot6
# https://twitter.com/home?oauth_token=ndr5LQAAAAABEwZ7AAABeQdZZYQ&oauth_verifier=gpj0gS74yxvb2rL4XKi5kBSpQVs17Lcs


### oauth_tokenとoauth_verifierからaccess_tokenを取得 ###
import  sys

from requests_oauthlib import OAuth1Session
from urllib.parse import parse_qsl

base_url = 'https://api.twitter.com/'
access_token_url = base_url + 'oauth/access_token'

oauth_token = "ndr5LQAAAAABEwZ7AAABeQdZZYQ"
oauth_verifier = "gpj0gS74yxvb2rL4XKi5kBSpQVs17Lcs"

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
