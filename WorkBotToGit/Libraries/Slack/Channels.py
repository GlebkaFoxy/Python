import requests
import json

from WorkBotToGit.pathToFile import Errors
from WorkBotToGit.telegramm.Telegramm import sendErrorMes
from tokens import TelegChannel
import time




def Arhive(token=None,channel=None):

    fields = {'token': token, 'channel': channel}
    __ansver__ = requests.post('https://slack.com/api/channels.archive', data=fields)
    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Arhive'
            sendErrorMes(TelegChannel, mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Create(token=None,name=None,validate=None):
    __fields = {'token':token,'name':name,'validate':validate}
    __ansver__ = requests.post('https://slack.com/api/channels.create',data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Create'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Histori(token=None,channel=None,count=None,inclusive = None,latest = None, oldest = None, unreads = None):

    __fields = {'token': token, 'channel': channel, 'count': count, 'inclusive': inclusive, 'latest': latest,'oldest': oldest, 'unreads': unreads}
    __ansver__ = requests.post('https://slack.com/api/channels.history', data=__fields)

    text = dict(__ansver__.json())
    if 'error' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.History'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Info (token=None,channel=None,include_locale=None):
    __fields = {'token': token, 'channel': channel, 'include_locale': include_locale}
    __ansver__ = requests.post('https://slack.com/api/channels.info', data=__fields)


    text = dict(__ansver__.json())
    if 'error' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Info'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Invite (token=None,channel=None,user=None):
    __fields = {'token': token, 'channel': channel, 'user': user}
    __ansver__ = requests.post('https://slack.com/api/channels.invite', data=__fields)


    text = dict(__ansver__.json())
    if 'eroor' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Invite'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Join (token=None,name=None,validate=None):
    #Присоединяет только бота к каналу, либо создаёт его.
    # Обязательные аргументы token, name.
    # Данный метод создан для человека, не для бота.
    #https://api.slack.com/methods/channels.join

    __fields = {'token': token, 'name': name, 'validate': validate}
    __ansver__ = requests.post('https://slack.com/api/channels.join', data=__fields)


    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Join'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Kick (token=None,channel=None,user=None):

    #https://api.slack.com/methods/channels.kick

    __fields = {'token': token, 'channel': channel, 'user': user}
    __ansver__ = requests.post('https://slack.com/api/channels.kick', data=__fields)


    text = dict(__ansver__.json())
    if 'error' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.kick'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Leave (token=None,channel=None,user=None):

    #https://api.slack.com/methods/channels.leave

    __fields = {'token': token, 'channel': channel, 'user': user}
    __ansver__ = requests.post('https://slack.com/api/channels.leave', data=__fields)


    text = dict(__ansver__.json())
    if 'error' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Leave'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def List (token=None,cursor=None,exclude_archived=None,exclude_members=None,limit=None):
    __fieds = {'token':token,'cursor':cursor,'exclude_archived':exclude_archived,'exclude_members':exclude_members,'limit':limit}
    __ansver__ = requests.post('https://slack.com/api/channels.list', data=__fieds)

    text = dict(__ansver__.json())
    if 'error' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.List'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Mark (token=None,channel=None,ts=None):

    #https://api.slack.com/methods/channels.mark

    __fields = {'token': token, 'channel': channel, 'ts': ts}
    __ansver__ = requests.post('https://slack.com/api/channels.mark', data=__fields)


    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Mark'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Rename (token=None,channel=None,name=None,validate=None):

    #https://api.slack.com/methods/channels.rename

    __fields = {'token': token, 'channel': channel, 'name': name,'validate':validate}
    __ansver__ = requests.post('https://slack.com/api/channels.rename', data=__fields)


    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors,'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Rename'
            print(mess)
            sendErrorMes(TelegChannel,mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Replies (token=None,channel=None,thread_ts=None):

    #https://api.slack.com/methods/channels.replies

    __fields = {'token': token, 'channel': channel,'thread_ts':thread_ts}
    __ansver__ = requests.post('https://slack.com/api/channels.replies', data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Replies'
            print(mess)
            sendErrorMes(TelegChannel, mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def SetPurpose (token=None,channel=None,purpose=None):

    #https://api.slack.com/methods/channels.setPurpose

    __fields = {'token': token, 'channel': channel,'purpose':purpose}
    __ansver__ = requests.post('https://slack.com/api/channels.setPurpose', data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Replies'
            print(mess)
            sendErrorMes(TelegChannel, mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def SetTopic (token=None,channel=None,topic=None):

    #https://api.slack.com/methods/channels.setTopic

    __fields = {'token': token, 'channel': channel,'topic':topic}
    __ansver__ = requests.post('https://slack.com/api/channels.setTopic', data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.SetTopic'
            print(mess)
            sendErrorMes(TelegChannel, mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Unarchive (token=None,channel=None):

    #https://api.slack.com/methods/channels.unarchive

    __fields = {'token': token, 'channel': channel}
    __ansver__ = requests.post('https://slack.com/api/channels.unarchive', data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в Channel.Unarchive'
            print(mess)
            sendErrorMes(TelegChannel, mess)
            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()





