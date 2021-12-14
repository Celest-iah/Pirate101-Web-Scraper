import requests
from bs4 import BeautifulSoup

def parseWeapon():
    weaponPages = ["https://www.pirate101central.com/wiki/Category:Weapons",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Darkmoor+Deathspitter+%28Level+10%2B%29%0ADarkmoor+Deathspitter+%28Level+10%2B%29#mw-pages",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Great+Gamer%27s+Set%0AGreat+Gamer%27s+Set#mw-pages",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Nefarious+Novablaster%0ANefarious+Novablaster#mw-pages",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Spiked+Buckler%0ASpiked+Buckler#mw-pages",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Tentacular+Staff+%28Level+65%2B%29%0ATentacular+Staff+%28Level+65%2B%29#mw-pages"]

    weaponsList = []
    for sourceLink in weaponPages:
        currentPage = requests.get(sourceLink)
        currentPageHTML = BeautifulSoup(currentPage.content, 'html.parser')

        listItems = currentPageHTML.find_all("li")
        for li in listItems:
            if "Item:" in li.text:
                weaponsList.append(li.text)
    return weaponsList

def updateData():
    weaponsList = parseWeapon()
    weaponFile = open("Pirate101-Web-Scraper\weaponNames.txt", "w")
    for item in weaponsList:
        weaponFile.write(item + "\n")
    weaponFile.close()

#def getStats(weaponName):


updateData()