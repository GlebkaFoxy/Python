import json

from WorkBotToGit.pathToFile import Locations

slovar ={}

def readJson():

        data = json.load(open(Locations))
        print(data)
        for i in data:
            slovar = dict(i)
            print(slovar.get('name'))

        channel = input("Выберите из списка название канала и введите его после двоеточия: ")
        print(channel)


        for g in data:
            if g.get('name')==channel:

                return (g.get('id'))
