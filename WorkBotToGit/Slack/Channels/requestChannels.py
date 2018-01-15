import json

from WorkBotToGit.Libraries.Slack import Channels
from WorkBotToGit.pathToFile import Ecoding, Locations, Errors
from tokens import tokenCinemaVR,tokenVRTech

lol ={}


def chaneelsList():
    #f = open('Locations.json', 'w')
    number = 0



    result = dict(Channels.List(tokenCinemaVR))
    print(result)
    if result.get('channels')!=None:

        with open(Ecoding,'w')as firt:
            json.dump(result, firt, indent=2, ensure_ascii='utf-8')


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


