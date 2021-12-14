import requests
from bs4 import BeautifulSoup

def get_weaponList_html():
    weaponsPages = ["https://www.pirate101central.com/wiki/Category:Weapons",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Darkmoor+Deathspitter+%28Level+10%2B%29%0ADarkmoor+Deathspitter+%28Level+10%2B%29#mw-pages",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Great+Gamer%27s+Set%0AGreat+Gamer%27s+Set#mw-pages",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Nefarious+Novablaster%0ANefarious+Novablaster#mw-pages",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Spiked+Buckler%0ASpiked+Buckler#mw-pages",
                    "https://www.pirate101central.com/w/index.php?title=Category:Weapons&pagefrom=Tentacular+Staff+%28Level+65%2B%29%0ATentacular+Staff+%28Level+65%2B%29#mw-pages"]
    
    weaponsList = []
    for weblink in weaponsPages:
        webpage = requests.get(weblink)
        html = BeautifulSoup(webpage.content, 'html.parser')
        
        allLIs = html.find_all("li")
        for li in allLIs:
            weaponsList.append(li.text)
    return weaponsList

def checkItem(objectName, weaponsList):
    itemID = "Item:" + objectName
    if itemID in weaponsList:
        return True
    else:
        return False
        
def get_gear_html(objectName):
    object_link = ""
    for char in objectName:
        if char != " ":
            object_link += char
        else:
            object_link += "_"
    base = "https://www.pirate101central.com/wiki/Item:"
    weblink = base + object_link
    webpage = requests.get(weblink)
    html = BeautifulSoup(webpage.content, 'html.parser')
    return html
def grabDDs(html):
    all_dds = html.find_all("dd")
    dd_list = []
    for dd in all_dds:
        if dd.text != """
""":
            dd_list.append(dd.text[:-1])
            
    return dd_list

def grabTags(html, tag):
    all_tags = html.find_all(tag)
    tag_list = []
    for tag in all_tags:
        if tag.text != """
""":
            tag_list.append(tag.text[:-1])
            
    return tag_list

def grabImg(html):
    all_imgs = html.find_all("img")
    all_img_src = []
    for item in all_imgs:
        all_img_src.append(item["src"])
    return all_img_src[4]

def cleanPrintWeapon(objectName, tag_list, img):
    imgDict = {"/w/images/thumb/f/f9/%28Icon%29_Agility.png/25px-%28Icon%29_Agility.png": "agility",
               "/w/images/thumb/d/d2/%28Icon%29_Strength.png/25px-%28Icon%29_Strength.png": "strength",
               "/w/images/thumb/e/ef/%28Icon%29_Will.png/25px-%28Icon%29_Will.png": "will"}
    print()
    print("The stats for the", objectName, "are:")
    print(tag_list[0][tag_list[0].find("Weapon Damage"):tag_list[0].find("Weapon Type")])
    print(tag_list[0][tag_list[0].find("Bonus From"):tag_list[0].find("Bonuses")][:-1] + imgDict[img])

def cleanPrintGear(objectName, tag_list):
    print()
    listLength = len(tag_list)
    print("The stats for the", objectName, "are:")
    for stat in range(int((listLength-1)/2)):
        print(tag_list[stat])
    
def main():
    weaponsList = get_weaponList_html()
    objectName = input("Enter the gear name.: ")
    isWeapon = checkItem(objectName, weaponsList)
    if isWeapon == True:
        tag = "p"
    if isWeapon == False:
        tag = "dd"
        
    html = get_gear_html(objectName)
    tag_list = grabTags(html, tag)
    
    if isWeapon == True:
        img = grabImg(html)
        cleanPrintWeapon(objectName, tag_list, img)
    if isWeapon == False:
        cleanPrintGear(objectName, tag_list)
    
if __name__ == "__main__":
    main()