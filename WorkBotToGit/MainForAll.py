from WorkBotToGit.Slack.Channels.askChanels import readJson
from WorkBotToGit.Slack.Channels.requestChannels import chaneelsList
from WorkBotToGit.Slack.Messages.readMessageAndConverse import readChatF, histori
import time

from WorkBotToGit.pathToFile import ChanneliD, Echat, TelegMessage
from WorkBotToGit.telegramm.Telegramm import sendMessage

chaneelsList()
readChatF(readJson())


#sendMessage(TelegMessage)
while True:
    histori(ChanneliD,Echat,TelegMessage)
    time.sleep(20)


