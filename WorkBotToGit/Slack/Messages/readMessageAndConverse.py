import json
import time

from WorkBotToGit.Libraries.Slack import Channels
from WorkBotToGit.Libraries.Slack.Users import Users
from WorkBotToGit.pathToFile import Echat
from WorkBotToGit.telegramm.Telegramm import sendMessage
from tokens import tokenCinemaVR,tokenVRTech, TelegChannel
from WorkBotToGit.pathToFile import ChanneliD
lol ={}

def readChatF(channel):
    #Запихиваем в JSON
    with open(Echat, "w") as chat:
        json.dump(Channels.Histori(tokenCinemaVR,channel,3),chat,indent=2, ensure_ascii='utf-8')


    # Сохраняем IDchannel в файл, для дальнейшего исспользования.
    with open(ChanneliD,"w") as ChannelID:
        ChannelID.write(channel)


def histori(ChannelID,Echat,TelegMessage):
    #открываем файл в котором IDchannel
    with open(ChannelID, "r") as ChannelID:
        ID = ChannelID.read()
        #print(ID)


    # достаём последний TS
    with open(Echat, encoding='utf-8') as Echate:
        data = dict(json.loads(Echate.read()))

        i=data.get('messages')
        lol=dict(i[0])
        #print(lol.get('ts'))

    # подготавливаем запрос на проверку новых сообщений
    hah = dict(Channels.Histori(tokenCinemaVR,ID,oldest=lol.get('ts')))
    print(hah)


    hoh = hah.get('messages')
    if not hoh:

        mesaage = {'teleg': 'none'}
        print(mesaage.get('teleg'))
        print()
        telegMessage = open(TelegMessage, "w")
        json.dump(mesaage, telegMessage, indent=2, ensure_ascii='utf-8')
    else:
        chat = open(Echat, "w")
        json.dump(hah, chat, indent=2, ensure_ascii='utf-8')
        #print(hoh)

        for i in reversed(hoh):
            text = dict(i)
            print(text)
            nameUser(text)

            mesaage = {'teleg': nameUser(text)+' '+text.get('text')}
            print(mesaage.get('teleg'))
            print()
            telegMessage = open(TelegMessage, "w")
            json.dump(mesaage, telegMessage, indent=2, ensure_ascii='utf-8')
            telegMessage.close()
            time.sleep(1)
            sendMessage(TelegMessage,TelegChannel)
            chat.close()


def nameUser(jsonResponse):
        data = jsonResponse
        print(data)

        i = data.get('user')
        print(i)

        needName = dict(Users.Info(tokenCinemaVR,i))
        nameTake = dict(needName.get('user'))
        name = nameTake.get('name')
        return name















