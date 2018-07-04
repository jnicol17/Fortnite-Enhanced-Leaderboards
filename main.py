import requests
import config
import json
from time import sleep
from operator import itemgetter

# These leaderboards will be populated with lists of dictionaries of player
# stats that can then be sorted and displayed
leaderboards = {"Leaderboards": {"Lifetime":[], "SoloStats":[], "DuoStats":[],
    "SquadStats":[], "CurrSolo":[], "CurrDuo":[], "CurrSquad":[]}}

# will store raw json data from fortnite tracker for all Players
# format will be { player name : fortnitetracker data }
raw_data = {}

# initialize stuff, right now just goes straight to main menu
def main():
    menu()

# main menu, user can select what they want to do from here
def menu():
    print("[1] Add/Remove Players")
    print("[2] View Individual Stats")
    print("[3] View Group Leaderboards")

    selection = input("Enter Corresponding Menu Number: ")
    if (selection == "1"):
        add_remove_players()
    elif (selection == "2"):
        view_individual_stats()

# add or remove a players data from the group leaderboards
def add_remove_players():
    names = input("Fortnite Name: ")
    names = names.replace(" ", "")
    name = names.split(",")

    print(name)
    for username in name:
        request_string = "https://api.fortnitetracker.com/v1/profile/pc/" + username
        response = requests.get(request_string, headers = config.headers)
        #print(response.text)
        data = response.json()
        print(username)

        #user = {username: data}
        raw_data[username] = data
        populate_leaderboards()
        #name = input("Fortnite Name: ")
        sleep(1)
    menu()

# view the stored stats for a player given the username, currently it asks
# for the name after the user has already selected this menu item, may
# change that so that a user can enter "2 snipe_celly34" to look up
# snipe_celly34's stats with one command
def view_individual_stats():
    name = input("Enter Users name: ")
    print_stats(raw_data[name])
    menu()

# populate the group leaderboard dictionary
def populate_leaderboards():
    print("populating leaderboards")

# print out select stats from the raw data dictionary for a given player,
# will clean this up when I start storing all the data is cleaner dictionaries
# instead of pulling from the raw JSON.
def print_stats(data):
    print("Name: " + data["epicUserHandle"])
    print("Platform: " + data["platformNameLong"])

    lifetime_stats = data["lifeTimeStats"]
    print_lifetime_stats(lifetime_stats)

    solo_lifetime_stats = data["stats"]["p2"]
    duo_lifetime_stats = data["stats"]["p10"]
    squad_lifetime_stats = data["stats"]["p9"]
    print_solo_lifetime_stats(solo_lifetime_stats)
    print_duo_lifetime_stats(duo_lifetime_stats)
    print_squad_lifetime_stats(squad_lifetime_stats)

    solo_current_stats = data["stats"]["curr_p2"]
    duo_current_stats = data["stats"]["curr_p10"]
    squad_current_stats = data["stats"]["curr_p9"]
    print_solo_current_stats(solo_current_stats)
    print_duo_current_stats(duo_current_stats)
    print_squad_current_stats(squad_current_stats)

def print_lifetime_stats(lifetime_stats):
    print("\nLIFETIME TOTAL")
    print(lifetime_stats[7]["key"] + ": " + lifetime_stats[7]["value"])
    print(lifetime_stats[8]["key"] + ": " + lifetime_stats[8]["value"])
    print(lifetime_stats[9]["key"] + ": " + lifetime_stats[9]["value"])
    print(lifetime_stats[10]["key"] + ": " + lifetime_stats[10]["value"])
    print(lifetime_stats[11]["key"] + ": " + lifetime_stats[11]["value"])

def print_solo_lifetime_stats(solo_lifetime_stats):
    print("\nLIFETIME SOLO STATS")
    print("# Matches: " + solo_lifetime_stats["matches"]["value"])
    print("# Wins: " + solo_lifetime_stats["top1"]["value"])
    print("Win %: " + solo_lifetime_stats["winRatio"]["value"])
    print("# Top 10s: " + solo_lifetime_stats["top10"]["value"])
    print("# Top 25s: " + solo_lifetime_stats["top25"]["value"])
    print("Kills: " + solo_lifetime_stats["kills"]["value"])
    print("K/D: " + solo_lifetime_stats["kd"]["value"])
    #print("# Top 25: " + test["stats"]["p2"]["top25"]["valueInt"])

def print_duo_lifetime_stats(duo_lifetime_stats):
    print("\nLIFETIME DUO STATS")
    print("# Matches: " + duo_lifetime_stats["matches"]["value"])
    print("# Wins: " + duo_lifetime_stats["top1"]["value"])
    print("Win %: " + duo_lifetime_stats["winRatio"]["value"])
    print("# Top 5s: " + duo_lifetime_stats["top5"]["value"])
    print("# Top 12s: " + duo_lifetime_stats["top12"]["value"])
    print("Kills: " + duo_lifetime_stats["kills"]["value"])
    print("K/D: " + duo_lifetime_stats["kd"]["value"])

def print_squad_lifetime_stats(squad_lifetime_stats):
    print("\nLIFETIME SQUAD STATS")
    print("# Matches: " + squad_lifetime_stats["matches"]["value"])
    print("# Wins: " + squad_lifetime_stats["top1"]["value"])
    print("Win %: " + squad_lifetime_stats["winRatio"]["value"])
    print("# Top 3s: " + squad_lifetime_stats["top3"]["value"])
    print("# Top 6s: " + squad_lifetime_stats["top6"]["value"])
    print("Kills: " + squad_lifetime_stats["kills"]["value"])
    print("K/D: " + squad_lifetime_stats["kd"]["value"])

def print_solo_current_stats(solo_current_stats):
    print("\nCURRENT SEASON SOLO STATS")
    print("# Matches: " + solo_current_stats["matches"]["value"])
    print("# Wins: " + solo_current_stats["top1"]["value"])
    print("Win %: " + solo_current_stats["winRatio"]["value"])
    print("# Top 10s: " + solo_current_stats["top10"]["value"])
    print("# Top 25s: " + solo_current_stats["top25"]["value"])
    print("Kills: " + solo_current_stats["kills"]["value"])
    print("K/D: " + solo_current_stats["kd"]["value"])

def print_duo_current_stats(duo_current_stats):
    print("\nCURRENT SEASON DUO STATS")
    print("# Matches: " + duo_current_stats["matches"]["value"])
    print("# Wins: " + duo_current_stats["top1"]["value"])
    print("Win %: " + duo_current_stats["winRatio"]["value"])
    print("# Top 5s: " + duo_current_stats["top5"]["value"])
    print("# Top 12s: " + duo_current_stats["top12"]["value"])
    print("Kills: " + duo_current_stats["kills"]["value"])
    print("K/D: " + duo_current_stats["kd"]["value"])

def print_squad_current_stats(squad_current_stats):
    print("\nCURRENT SEASON SQUAD STATS")
    print("# Matches: " + squad_current_stats["matches"]["value"])
    print("# Wins: " + squad_current_stats["top1"]["value"])
    print("Win %: " + squad_current_stats["winRatio"]["value"])
    print("# Top 3s: " + squad_current_stats["top3"]["value"])
    print("# Top 6s: " + squad_current_stats["top6"]["value"])
    print("Kills: " + squad_current_stats["kills"]["value"])
    print("K/D: " + squad_current_stats["kd"]["value"])

#program runs here
if __name__ == '__main__':
    main()

#=============== FUTURE IDEAS ===============#

# Leaderboard ideas
#   1. Most wins (Total)
#   2. Most kills (Total)
#   3. Highest K/d (Total)
#   4. Most Wins (Solo)
#   5. Most Kills (Solo)
#   6. Highest K/d (Solo)
#   7. Most Wins (Duo)
#   8. Most Kills (Duo)
#   9. Highest K/d (Duo)
#   10. Most Wins (Squad)
#   11. Most Kills (Squad)
#   12. Highest K/d (Squad)

# Start screen: Enter 1 or more usernames, no spaces, separated by commas
# loading screen for each username
# main menu where you can:
#   add a person to the list
#   remove a person from the list
#   view personal leaderboards for a user (input username)
#   view leaderboards for the group
# view leaderboards for a user
#   Select one leaderboard
#   Select all leaderboards
# view leaderboards for the group
#   Select one Leaderboard
#   Select all Leaderboards

# Some test code for sorting and printing dictionaries
#print(config.leaderboard["Leaderboards"]["Lifetime"])
#config.leaderboard["Leaderboards"]["Lifetime"].append({"name": "test", "value": 4})
#config.leaderboard["Leaderboards"]["Lifetime"].append({"name": "test2", "value": 6})
#print(config.leaderboard["Leaderboards"]["Lifetime"])
#newlist = sorted(config.leaderboard["Leaderboards"]["Lifetime"], key=itemgetter('value'), reverse=True)
#print(newlist)
#print(newlist[0]["value"])
