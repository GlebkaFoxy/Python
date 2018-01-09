from WorkBotToGit.Slack.Channels.askChanels import readJson
from WorkBotToGit.Slack.Channels.requestChannels import chaneelsList
from WorkBotToGit.Slack.Messages.readMessageAndConverse import readChatF, histori
import time

from WorkBotToGit.pathToFile import ChannelID, Echat, TelegMessage
from WorkBotToGit.telegramm.Telegramm import sendMessage

chaneelsList()
readChatF(readJson())


#sendMessage(TelegMessage)
while True:
    histori(ChannelID,Echat,TelegMessage)
    time.sleep(450)


