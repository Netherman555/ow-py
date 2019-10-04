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
##
##Version v.0.0.1.0

import json
import requests

CHARACTERS = ['ana', 'baptiste', 'bastion', 'brigitte', 'dVa', 'doomfist',
              'genji', 'hanzo', 'junkrat', 'lucio', 'mccree', 'mei', 'mercy',
              'moira', 'orisa', 'pharah', 'reaper', 'reinhardt', 'roadhog', 'sigma',
              'soldier76', 'sombra', 'symmetra', 'torbjorn', 'tracer', 'widowmaker', 'winston',
              'wrecking ball', 'zarya', 'zenyatta'] 
STATS = ['timePlayed', 'gamesWon', 'winPercentage', 'weaponAccuracy', 'eliminationsPerLife', 'multiKillsBest', 'objectiveKills']

class Character():

    def __init__(self, characterName, jsondata):

        if(characterName not in CHARACTERS):
            raise Exception("Invalid Character ID")
        else:
            self.character = characterName

        self.jsondata = jsondata
        self.quickPlayStats = {}
        self.competitiveStats = {}

        for stat in STATS:
          try:
            self.quickPlayStats[stat] = self.jsondata['quickPlayStats']['topHeroes'][self.character][stat]
          except:
            self.quickPlayStats[stat] = None

        for stat in STATS:
          try:
            self.competitiveStats[stat] = self.jsondata['competitiveStats']['topHeroes'][self.character][stat]
          except:
            self.competitiveStats[stat] = None
