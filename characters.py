##A very basic class that extracts common character data from
##the API.
##
##Parameters:
##
## - characterName: A valid charactername that is included in the CHARACTERS list
##                  Will return an exception if not a valid character.
##
## - jsondata: The JSON data that the character information is being extracted
##             from.  This is just the data that the API returns and is given
##             in other files.
##
##Version v.0.0.1.0

import json
import requests

CHARACTERS = ['ana', 'ashe', 'baptiste', 'bastion', 'brigitte', 'dva', 'doomfist',
              'genji', 'hanzo', 'junkrat', 'lucio', 'mccree', 'mei', 'mercy',
              'moira', 'orisa', 'pharah', 'reaper', 'reinhardt', 'roadhog', 'sigma',
              'soldier76', 'sombra', 'symmetra', 'torbjorn', 'tracer', 'widowmaker', 'winston',
              'wrecking ball', 'zarya', 'zenyatta']
MODES = ['quickplay', 'competitive']

class Character():

    def __init__(self, characterName, jsondata):


        if(characterName not in CHARACTERS):
            raise Exception("Invalid Character ID")
        else:
            self.character = characterName

        self.jsondata = jsondata

        self.qptimePlayed = self.jsondata['quickPlayStats']['topHeroes'][self.character]['timePlayed']
        self.qpgamesWon = self.jsondata['quickPlayStats']['topHeroes'][self.character]['gamesWon']
        self.qpwinPercentage = self.jsondata['quickPlayStats']['topHeroes'][self.character]['winPercentage']
        self.qpweaponAccuracy = self.jsondata['quickPlayStats']['topHeroes'][self.character]['weaponAccuracy']
        self.qpelimsPerLife = self.jsondata['quickPlayStats']['topHeroes'][self.character]['eliminationsPerLife']
        self.qpmultiKillBest = self.jsondata['quickPlayStats']['topHeroes'][self.character]['multiKillBest']
        self.qpobjectiveKills = self.jsondata['quickPlayStats']['topHeroes'][self.character]['objectiveKills']

        self.cptimePlayed = self.jsondata['competitiveStats']['topHeroes'][self.character]['timePlayed']
        self.cpgamesWon = self.jsondata['competitiveStats']['topHeroes'][self.character]['gamesWon']
        self.cpwinPercentage = self.jsondata['competitiveStats']['topHeroes'][self.character]['winPercentage']
        self.cpweaponAccuracy = self.jsondata['competitiveStats']['topHeroes'][self.character]['weaponAccuracy']
        self.cpelimsPerLife = self.jsondata['competitiveStats']['topHeroes'][self.character]['eliminationsPerLife']
        self.cpmultiKillBest = self.jsondata['competitiveStats']['topHeroes'][self.character]['multiKillBest']
        self.cpobjectiveKills = self.jsondata['competitiveStats']['topHeroes'][self.character]['objectiveKills']
