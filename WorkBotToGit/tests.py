import json

import requests

from WorkBotToGit.Libraries.Slack import Channels
from WorkBotToGit.pathToFile import Ecoding, Locations, Errors
from tokens import tokenCinemaVR, tokenVRTech


def chan():
    fields = {'token':tokenVRTech}
    channelID = requests.post('https://slack.com/api/channels.list',data=fields)
    print(channelID.text)

def chaneelsList():
    #f = open('Locations.json', 'w')
    number = 0
    fieldChannelsList = {'token': tokenVRTech, 'limit': '0'}
    result = requests.post('https://slack.com/api/channels.list', data=fieldChannelsList)

    print(result.text)
    errors = dict(result.json())
    print(errors)
    if errors.get('channels')!=None:

        with open(Ecoding,'w')as firt:
            json.dump(result.json(), firt, indent=2, ensure_ascii='utf-8')


    #with open(open("E:\\untitled\WorkBotToGit\Slack\JsonFiles\Ecoding.json", "w")as lol:
        with open(Ecoding, encoding='utf-8') as data_file:
            data = dict(json.loads(data_file.read()))
            print(data)
        mass = data.get("channels")
        for i in mass:
        #print(i)
            for g in list(i):
                if g!='id' and g!='name'and g!='members':
                    del i[g]
        #print(i)
            mass[number]=i
            number += 1

        with open(Locations,'w') as file:
            json.dump(mass, file, indent=2, ensure_ascii='utf-8')
    else:
        print(result.text)
        with open(Errors,'w') as fileError:
            print('Смотри файл errors')
            json.dump(result.json(), fileError, indent=2, ensure_ascii='utf-8')
        exit()


Channels.Histori(tokenCinemaVR,'C7R2Y199S',3)
