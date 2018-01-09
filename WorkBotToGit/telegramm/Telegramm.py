import requests
import json

from WorkBotToGit.pathToFile import TelegMessage
from tokens import tokenTelegram

offset = 0
URL = 'https://api.telegram.org/bot'
TOKEN = tokenTelegram


def test ():
    try:
        request = requests.post(URL+TOKEN+'/sendMessage'+'?')
        print(request.json())
        getUpdates = open('getUpdates.json','w')
        json.dump(request.json(),getUpdates,indent=2, ensure_ascii='utf-8')

    except:
        print('Error getting updates')
        return False
    if not request.status_code == 200 : return False
    if not request.json()['ok'] : return False


def sendMessage(TelegMessage,TelegChannel):
    with open(TelegMessage,encoding='utf-8') as target:
        ansver = dict(json.loads(target.read()))
        ready = str(ansver.get('teleg'))
        print(ready)

    rest ={'chat_id':TelegChannel,'text':ready}
    print(rest)
    #ITsend = URL+TOKEN+'/sendMessage?chat_id=-249367819&text='+ready

    send = requests.post(URL+TOKEN+'/sendMessage',data=rest)
    #print(send.text)



