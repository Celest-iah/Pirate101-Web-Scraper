#Importing libraries for webscraping
import requests
from bs4 import BeautifulSoup as bs

#Importing functions from other files
import weapons
import gear
import quests

def main():
    mainLoop = True
    while mainLoop:
        print("""
1. Weapons
2. Gear
3. Quests
4. Exit""")
        userInput = input("Option: ")
        if userInput == "1":
            print("Weapons")
        elif userInput == "2":
            print("Gear")
        elif userInput == "3":
            print("Quests")
        elif userInput == "4":
            print("Exiting...")
            mainLoop = False
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()