#Importing libraries for webscraping
import requests
from bs4 import BeautifulSoup as bs
import json

#Importing functions from other files
import weapons
import gear
import quests

def updateData():
    weapons.updateData()
    print("Weapons Updated")
    gear.updateData()
    print("Gear Updated")
    quests.updateData()
    print("Quests Updated")

def main():
    mainLoop = True
    while mainLoop:
        print("""
Pirate101 Web Scraper
1. Weapons
2. Gear
3. Quests
4. Update Database
5. Exit\n""")
        userInput = input("Option: ")
        if userInput == "1":
            print("Weapons")
        elif userInput == "2":
            print("Gear")
        elif userInput == "3":
            print("Quests")
        elif userInput == "4":
            print("Updating Database...")
            updateData()
        elif userInput == "5":
            print("Exiting...")
            mainLoop = False
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()