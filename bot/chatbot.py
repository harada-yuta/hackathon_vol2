import requests
import json


# リクルートのA3RT提供の「Talk API」
class Talk:
    def __init__(self):
        self.key = ''
        self.api = ''

    def get(self,talking):
        url = self.api
        r = requests.post(url,{'apikey':self.key,'query':talking})
        data = json.loads(r.text)
        if data['status'] == 0:
            t = data['results']
            ret = t[0]['reply']
        else:
            ret = '・・・・・・・・・'
        return ret

def response_talk(sentence):
    talk = Talk()
    response = talk.get(sentence)
    #print(response)
    return response

if __name__ == '__main__':
    response_talk("今日もいい天気だね")
