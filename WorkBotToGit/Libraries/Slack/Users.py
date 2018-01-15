import requests
import time
import json

from WorkBotToGit.pathToFile import Errors
from WorkBotToGit.telegramm.Telegramm import sendErrorMes
from tokens import TelegChannel


def DeletePhoto(token=None):

    #https://api.slack.com/methods/users.deletePhoto

    __fields = {'token': token}
    __ansver__ = requests.post('https://slack.com/api/users.deletePhoto', data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в User.DeletePhoto'
            print(mess)
            # Отправка сообщений в телеграмм, заточенный канал.
            sendErrorMes(TelegChannel, mess)

            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def GetPresence(token=None,user=None):

    #https://api.slack.com/methods/users.getPresence

    __fields = {'token':token,'user':user}
    __ansver__= requests.post('https://slack.com/api/users.getPresence',data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в User.GetPresence'
            print(mess)
            #Отправка сообщений в телеграмм, заточенный канал.
            sendErrorMes(TelegChannel, mess)

            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Identity (token=None):

    #https://api.slack.com/methods/users.identity

    __fields = {'token':token}
    __ansver__ =requests.post('https://slack.com/api/users.identity',data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в User.Identity'
            print(mess)
            # Отправка сообщений в телеграмм, заточенный канал.
            sendErrorMes(TelegChannel, mess)

            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def Info (token=None,user=None,include_locale=None):

    #https://api.slack.com/methods/users.info

    __fields = {'token':token,'user':user,'include_locale':include_locale}
    __ansver__ =requests.post('https://slack.com/api/users.info',data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в User.GetPresence'
            print(mess)
            # Отправка сообщений в телеграмм, заточенный канал.
            sendErrorMes(TelegChannel, mess)

            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def List (token=None, cursor=None, include_locale=None,limit=None,presense=None):

    #https://api.slack.com/methods/users.list

    __fields = {'token':token,'cursor':cursor,'include_locale':include_locale,'limit':limit,'presense':presense}
    __ansver__ =requests.post('https://slack.com/api/users.list',data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в User.List'
            print(mess)
            # Отправка сообщений в телеграмм, заточенный канал.
            sendErrorMes(TelegChannel, mess)

            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def LookupByEmail (token=None, email=None):

    #https://api.slack.com/methods/users.lookupByEmail

    __fields = {'token':token,'email':email}
    __ansver__ =requests.post('https://slack.com/api/users.lookupByEmail',data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в User.LookupByEmail'
            print(mess)
            # Отправка сообщений в телеграмм, заточенный канал.
            sendErrorMes(TelegChannel, mess)

            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def SetActive (token=None):

    #https://api.slack.com/methods/users.setActive

    __fields = {'token':token}
    __ansver__ =requests.post('https://slack.com/api/users.setActive',data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в User.SetActive'
            print(mess)
            # Отправка сообщений в телеграмм, заточенный канал.
            sendErrorMes(TelegChannel, mess)

            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def SetPhoto (token=None, image=None, crop_w=None,crop_x=None,crop_y=None):

    #https://api.slack.com/methods/users.setPhoto

    __fields = {'token':token,'image':image,'crop_w':crop_w,'crop_x':crop_x,'crop_y':crop_y}
    __ansver__ =requests.post('https://slack.com/api/users.setPhoto',data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в User.SetPhoto'
            print(mess)
            # Отправка сообщений в телеграмм, заточенный канал.
            sendErrorMes(TelegChannel, mess)

            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()

def SetPresence (token=None, presense=None):

    #https://api.slack.com/methods/users.setPresence

    __fields = {'token':token,'presense':presense}
    __ansver__ =requests.post('https://slack.com/api/users.setPresence',data=__fields)

    text = __ansver__.json()
    if 'error' not in text:
        return text
    else:
        with open(Errors, 'w') as fileError:
            mess = ' Смотрите файл errors, ошибка в User.SetPresence'
            print(mess)
            # Отправка сообщений в телеграмм, заточенный канал.
            sendErrorMes(TelegChannel, mess)

            json.dump(text, fileError, indent=2, ensure_ascii='utf-8')

            time.sleep(20)
        exit()