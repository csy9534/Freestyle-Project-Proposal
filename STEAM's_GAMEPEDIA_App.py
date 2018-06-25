#STEAM's GAMEPEDIA App
#Developed by Shuyang Chai

import json
import urllib
from urllib.request import urlopen

menu = f"""
    -----------------------------------
            STEAM's GAMEPEDIA
    -----------------------------------

    Information index:

    * top100in2weeks - Returns Top 100 games by players in the last two weeks.
    * top100forever - Returns Top 100 games by players since March 2009.
    * top100owned - Returns Top 100 games by owners.
    * appid - Steam Application ID. If it's 999999, then data for this application is hidden on developer's request, sorry.
    * name - game's name
    * developer - comma separated list of the developers of the game
    * publisher - comma separated list of the publishers of the game
    * score_rank - score rank of the game based on user reviews
    * owners - owners of this application on Steam as a range.
    * average_forever - average playtime since March 2009. In minutes.
    * average_2weeks - average playtime in the last two weeks. In minutes.
    * median_forever - median playtime since March 2009. In minutes.
    * median_2weeks - median playtime in the last two weeks. In minutes.
    * ccu - peak CCU yesterday.
    * price - current US price in cents.
    * initialprice - original US price in cents.
    * discount - current discount in percents.
    * tags - game's tags with votes in JSON array.
    * languages - list of supported languages.
    * genre - list of genres.

    """
print(menu)

infos = []

while True:
    info = input("Pleas input the informatino index you want to check or 'DONE' to stop: ")
    if info == "DONE":
        break
    elif info != "DONE":
        infos.append(info)
    else :
        print ("\nHey, are you sure that identifier is correct? Please try again!")

url = f"https://steamspy.com/api.php?request={infos}"

response = urlopen(url)
data = response.read().decode("utf-8")

dataDict = json.loads(data)
