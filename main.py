import tweepy
import random
import time
import re

import MeCab
m = MeCab.Tagger ("-Ochasen")

from bot.UI import Get_infomation
from bot.polarity import sentiment_analyzer_scores
from bot.chatbot import response_talk
from bot.siritori import answer
import bot.config
api1 = bot.config.api1 
api2 = bot.config.api2
api3 = bot.config.api3
api4 = bot.config.api4
api5 = bot.config.api5
api6 = bot.config.api6


user_list = []      # 監視するユーザーの一覧
bot_choice = []     # 選択したBot


### 監視動作 ###
def monitoring(user_list):
    # まずはユーザーをフォローする
    for user in user_list:
        api1.create_friendship(user) 
        #api2.create_friendship(user) 
        #api3.create_friendship(user) 

    # 監視対象のリストに追加
    target_ids = api1.friends_ids(screen_name=api1.me().screen_name)      # botのフォローしている垢を監視リストに
    watch_list = [str(user) for user in target_ids]

    # Streamクラス継承
    myStreamListener = MyStreamListener()     
    myStream1 = tweepy.Stream(auth=api1.auth, listener=myStreamListener)
    myStream2 = tweepy.Stream(auth=api2.auth, listener=myStreamListener)
    myStream3 = tweepy.Stream(auth=api3.auth, listener=myStreamListener)
    myStream4 = tweepy.Stream(auth=api4.auth, listener=myStreamListener)
    myStream5 = tweepy.Stream(auth=api5.auth, listener=myStreamListener)
    myStream6 = tweepy.Stream(auth=api6.auth, listener=myStreamListener)

    # ストリーム開始
    myStream1.filter(follow=watch_list)      # Bot1
    myStream2.filter(follow=watch_list)      # Bot2
    myStream3.filter(follow=watch_list)      # Bot3
    myStream4.filter(follow=watch_list)      # Bot4
    myStream5.filter(follow=watch_list)      # Bot5
    myStream6.filter(follow=watch_list)      # Bot6


### Streamクラス ###
# StreamListenerを継承し、on_statusをオーバーライドするクラス
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.screen_name in user_list:
            print(status.user.name, status.user.screen_name)
            print(status.created_at)
            print(status.text)

            if bot_choice[0] == True:       # bot1
                api1.create_favorite(id=status.id)
                post_reply1(api1, status.id, status.user.screen_name, status.text)
            if bot_choice[1] == True:       # bot2
                api2.create_favorite(id=status.id)
                post_reply2(api2, status.id, status.user.screen_name, status.text)
            if bot_choice[2] == True:       # bot3
                #api3.create_favorite(id=status.id)
                post_reply3(api3, status.id, status.user.screen_name, status.text)
            if bot_choice[3] == True:       # bot4
                #api4.create_favorite(id=status.id)
                post_reply4(api4, status.id, status.user.screen_name, status.text)
            if bot_choice[4] == True:       # bot5
                api5.create_favorite(id=status.id)
                post_reply5(api5, status.id, status.user.screen_name, status.text)
            if bot_choice[5] == True:       # bot6
                api6.create_favorite(id=status.id)
                post_reply6(api6, status.id, status.user.screen_name, status.text)

            print("---------------------")

        return True


    def on_error(self, status_code):
        print('error:', str(status_code))
        return False
    
    def on_timeout(self):
        print('Timeout...')
        return False


####################
### リプライ動作 ###
####################
# リプライ飛ばす
# type1(ツイートの極性によって画像でリプライ)
def post_reply1(api, tweet_id, screen_name ,tweet):
    print("bot1")
    file_path_list = [["image/positive/posi_1.png", "image/positive/posi_2.png", "image/positive/posi_3.png"],
                      ["image/neutral/neu_1.png", "image/neutral/neu_2.png", "image/neutral/neu_3.png"], 
                      ["image/negative/nega_1.png", "image/negative/nega_2.png", "image/negative/nega_3.png"]]
    
    feeling = sentiment_analyzer_scores(tweet)
    #feeling = {'neg': 0.0, 'neu': 0.517, 'pos': 0.483, 'compound': 0.4215}
    if feeling['compound'] > 0.3:       # positive
        file_path = random.choice(file_path_list[0])
    elif feeling['compound'] < -0.2:    # negative
        file_path = random.choice(file_path_list[2])
    else:                               # neutral
        file_path = random.choice(file_path_list[1])
    print(file_path)  

    if screen_name in user_list:
        api.update_with_media(file_path, status = "@" + str(screen_name), in_reply_to_status_id = tweet_id)
        print("    ↓")
        print("reply image.")


# type2(対話API)
def post_reply2(api, tweet_id, screen_name ,tweet):
    print("bot2")
    reply_word = response_talk(tweet)
    reply = "@" + str(screen_name) + "\n" + reply_word

    if screen_name in user_list:
        api.update_status(reply, tweet_id)
        print("    ↓")
        print(reply)

    
# type3(ポジティブなツイートにクソリプしてくるやつ)
def post_reply3(api, tweet_id, screen_name ,tweet):
    print("bot3")
    reply_text_list = ['FF外から失礼するゾ～（謝罪） このツイート面白スギィ！！！！！自分、RTいいっすか？ 淫夢知ってそうだからry)',
                       'いや、しらねえよ',
                       'そのツイートおもしろくないですよ',
                       'そのツイート不謹慎じゃないですか？大変な状況の人もたくさんいるんですよ。',
                       'あなたがのんきにツイートしている間も、アフリカの子供たちは苦しんでるんですよ！！']
    feeling = sentiment_analyzer_scores(tweet)
    #feeling = {'neg': 0.0, 'neu': 0.517, 'pos': 0.483, 'compound': 0.505}
    if feeling['compound'] > 0.5:    # positive
        reply_word = random.choice(reply_text_list)
        reply = "@" + str(screen_name) + "\n" + reply_word

        if screen_name in user_list:
            api.update_status(reply, tweet_id)
            print("    ↓")
            print(reply)


# type4(なんか知らんけどしりとり勝負してくるやつ)
def post_reply4(api, tweet_id, screen_name ,tweet):
    print("bot4")
    if tweet.find("@") == 0:
        tweet = re.sub(r'@[0-9a-zA-Z_:]*', "", tweet)    # ユーザー名削除
        reply_word = answer(tweet)
    else:
        reply_word = "しりとりしようぜ。俺から、じゃあ「しりとり」"
    if reply_word:
        reply = "@" + str(screen_name) + "\n" + str(reply_word)
    else:
        reply = "@" + str(screen_name) + "\n" + "やっぱやーめた"

    if screen_name in user_list:
        api.update_status(reply, tweet_id)
        print("    ↓")
        print(reply)


# type5(ネガティブな発言に励ましてくれるいいやつ)
def post_reply5(api, tweet_id, screen_name ,tweet):
    print("bot5")
    reply_text_list = ['生きててえらい！'
                       'お前は頑張ってるって',
                       '大丈夫、大丈夫',
                       '気にすんなって。',
                       '明日はきっといい日になるよ']
    feeling = sentiment_analyzer_scores(tweet)
    #feeling = {'neg': 0.0, 'neu': 0.517, 'pos': 0.483, 'compound': -0.305}
    if feeling['compound'] < -0.2:    # negative
        reply_word = random.choice(reply_text_list)
        reply = "@" + str(screen_name) + "\n" + reply_word
        if screen_name in user_list:
            api.update_status(reply, tweet_id)
            print("    ↓")
            print(reply)


# type6(挨拶を返してくれるやつ)
def post_reply6(api, tweet_id, screen_name ,tweet):
    print("bot6")
    wakati_data = m.parse(tweet).splitlines()    
    word = []
    word_list = []
    for line in wakati_data:
        if not line == "EOS":
            try:
                #print(line)
                w = line.split()

                for n in range(4):
                    word.append(w[n])

                word_class = word[3].split("-")
                for i in range(len(word_class)):
                    word.append("")
                    word[3 + i] = word_class[i]
                del word[-1]
                if word[3] == "感動詞":
                    word_list.append(word)
                word = []
            except:
                pass
    #print(word_list)
    if word_list:
        reply_word = word_list[0][2]
        reply = "@" + str(screen_name) + "\n" + reply_word
        if screen_name in user_list:
            api.update_status(reply, tweet_id)
            print("    ↓")
            print(reply)




if __name__ == '__main__':
    # ユーザー指定
    user_list, bot_choice = Get_infomation()
    #user_list = ["_dsmktmg"]
    print("監視中...")
    print("")

    monitoring(user_list)

    """
    tweet = "ハッカソン、今日で終わりやな、疲れたわ"
    print(tweet)
    #post_reply1(api1, "1234567890", "_dsmktmg", tweet)      # 画像リプライ(まるもち) OK
    post_reply2(api1, "1234567890", "_dsmktmg", tweet)     # 対話API(坊ちゃん) OK
    #post_reply3(api1, "1234567890", "_dsmktmg", tweet)      # クソリプ(田中君) OK
    #post_reply4(api1, "1234567890", "_dsmktmg", tweet)     # しりとり(しりとりマン) NG
    #post_reply5(api1, "1234567890", "_dsmktmg", tweet)      # 励まし(ハム次郎) OK
    #post_reply6(api1, "1234567890", "_dsmktmg", tweet)      # 挨拶(風紀委員) OK
    """