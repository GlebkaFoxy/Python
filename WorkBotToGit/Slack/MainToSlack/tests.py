import requests
import time
from WorkBotToGit.pathToFile import ChannelID
from tokens import tokenCinemaVR


def printMessage():
    with open(ChannelID,'r') as needID:
        text = needID.read()
    fields ={'token':tokenCinemaVR,'channel':text,'text':'Hello to you'}
    piuMessage = requests.post('https://slack.com/api/chat.postMessage',data=fields)
    print(piuMessage.text)


def test():
    #needItem = data.get('user')
            fields = {'token': tokenCinemaVR, 'user': 'U72LBP36X'}
            NameInfo = requests.post('https://slack.com/api/users.info', data=fields)
            needName = dict(NameInfo.json())
            nameTake = dict(needName.get('user'))
            #print(nameTake)

            name = str(nameTake.get('name'))
            print(name)
            return name

while True:
    printMessage()
    time.sleep(449)
