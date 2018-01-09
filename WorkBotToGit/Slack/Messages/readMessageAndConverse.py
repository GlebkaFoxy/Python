import requests
import json
import  time
from WorkBotToGit.Slack.Channels.askChanels import readJson
from WorkBotToGit.pathToFile import Echat, ChannelID, TelegMessage
from WorkBotToGit.telegramm.Telegramm import sendMessage
from tokens import tokenVRTech, tokenCinemaVR, TelegChannel

lol ={}

def readChatF(channel):
    # Поля для запроса
    fields = {'token': tokenCinemaVR, 'channel':channel, 'count':'3'}
    # Делаем первичный запрос для последних 3 сообщений.

    histori = requests.post('https://slack.com/api/channels.history', data=fields)
    #print(histori.text)

    #Запихиваем в JSON
    with open(Echat, "w") as chat:
        json.dump(histori.json(),chat,indent=2, ensure_ascii='utf-8')


    # Сохраняем IDchannel в файл, для дальнейшего исспользования.
    with open("C:\\untitled\WorkBotToGit\Slack\JsonFiles\ChannelID.txt","w") as ChannelID:
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
    fields2 = {'token': tokenCinemaVR, 'channel': ID, 'oldest':lol.get('ts')}
    # сам запрос
    request = requests.post('https://slack.com/api/channels.history',data=fields2)
    print(request.text)

    hah = request.json()

    #print(hah)
    hoh = hah.get('messages')
    if not hoh:

        mesaage = {'teleg': 'none'}
        print(mesaage.get('teleg'))
        print()
        telegMessage = open(TelegMessage, "w")
        json.dump(mesaage, telegMessage, indent=2, ensure_ascii='utf-8')
    else:


        chat = open(Echat, "w")
        json.dump(request.json(), chat, indent=2, ensure_ascii='utf-8')
        #print(hoh)

        for i in reversed(hoh):
            text = dict(i)

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
        data = dict(jsonResponse)
        if data.get('user')==None:
            name = data.get('username')

        else:
            needItem = data.get('user')
            fields = {'token': tokenCinemaVR, 'user': needItem}
            NameInfo = requests.post('https://slack.com/api/users.info', data=fields)
            needName = dict(NameInfo.json())
            nameTake = dict(needName.get('user'))
            #print(nameTake)
            name = str(nameTake.get('name'))
        return name












