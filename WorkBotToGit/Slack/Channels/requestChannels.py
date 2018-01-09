import json

import requests

from WorkBotToGit.Slack.MainToSlack.fields import fieldChannelsList
from WorkBotToGit.pathToFile import Ecoding, Locations

lol ={}


def chaneelsList():
    #f = open('Locations.json', 'w')
    number = 0
    field = fieldChannelsList
    result = requests.post('https://slack.com/api/channels.list', data=field)

    print(result.text)
    with open(Ecoding,'w')as firt:
        json.dump(result.json(), firt, indent=2, ensure_ascii='utf-8')
        firt.close()

    #with open(open("E:\\untitled\WorkBotToGit\Slack\JsonFiles\Ecoding.json", "w")as lol:
    with open(Ecoding, encoding='utf-8') as data_file:
        data = dict(json.loads(data_file.read()))
        data_file.close()

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
        file.close()
