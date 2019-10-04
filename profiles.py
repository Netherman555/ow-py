BASE_URL = 'https://ovrstat.com/{platform}/{username}'
ACCEPTED_PLATFORMS = ['pc', 'xbl', 'psn']

import requests

class Profile():
  def __init__(self, platform, gamertag):
    ##Creates a class for a persons profile.
    ##Supports all three current platforms to an extent, primarily PC.
    ##
    ##Takes in 2 arguments:
    ## 
    ## - platform: Either pc, xbl, or psn (case sensitive)
    ## - gamertage: On XBL or PSN it is just the gamertag, for PC it
    ##              is the battle.net name, including the number at 
    ##              the end.

    self.url = BASE_URL
    self.username = gamertag

    if(platform not in ACCEPTED_PLATFORMS):
      raise Exception("Invalid Platform")
    else:
      self.platform = platform
      self.url = self.url.replace('{platform}', self.platform)

    self.url = self.url.replace('{username}', self.username)

    self.jsondata = requests.get(url=self.url).json()
