import requests
import config
import json
from time import sleep
from operator import itemgetter

# Solo leaderboards
solo_leaderboards = {}

# These leaderboards will be populated with lists of dictionaries of player
# stats that can then be sorted and displayed
group_leaderboards = {
    "Lifetime":[],
    "SoloStats":[],
    "DuoStats":[],
    "SquadStats":[],
    "CurrSolo":[],
    "CurrDuo":[],
    "CurrSquad":[]
    }

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

        populate_solo_leaderboards(username, data)
        populate_group_leaderboards(username, data)

        sleep(1)
    menu()

# view the stored stats for a player given the username, currently it asks
# for the name after the user has already selected this menu item, may
# change that so that a user can enter "2 snipe_celly34" to look up
# snipe_celly34's stats with one command
def view_individual_stats():
    name = input("Enter Users name: ")
    print_solo_stats(name)
    menu()

# populate the group leaderboard dictionary
def populate_solo_leaderboards(username, data):

    print("populating leaderboards")
    raw_data[username] = data
    solo_leaderboards[username] = {}

    lifetime_stats = data["lifeTimeStats"]
    solo_leaderboards[username]["LIFETIME STATS"] = {
        "Matches Played": lifetime_stats[7]["value"],
        "Wins": lifetime_stats[8]["value"],
        "Win %": lifetime_stats[9]["value"].strip("%"),
        "Kills": lifetime_stats[10]["value"],
        "K/D": lifetime_stats[11]["value"]
        }

    solo_lifetime_stats = data["stats"]["p2"]
    solo_leaderboards[username]["SOLO STATS"] = {
        "Matches Played": solo_lifetime_stats["matches"]["value"],
        "Wins": solo_lifetime_stats["top1"]["value"],
        "Win %": solo_lifetime_stats["winRatio"]["value"],
        "Top 10s": solo_lifetime_stats["top10"]["value"],
        "Top 25s": solo_lifetime_stats["top25"]["value"],
        "Kills": solo_lifetime_stats["kills"]["value"],
        "K/D": solo_lifetime_stats["kd"]["value"]
        }

    duo_lifetime_stats = data["stats"]["p10"]
    solo_leaderboards[username]["DUO STATS"] = {
        "Matches Played": duo_lifetime_stats["matches"]["value"],
        "Wins": duo_lifetime_stats["top1"]["value"],
        "Win %": duo_lifetime_stats["winRatio"]["value"],
        "Top 5s": duo_lifetime_stats["top5"]["value"],
        "Top 12s": duo_lifetime_stats["top12"]["value"],
        "Kills": duo_lifetime_stats["kills"]["value"],
        "K/D": duo_lifetime_stats["kd"]["value"]
    }

    squad_lifetime_stats = data["stats"]["p9"]
    solo_leaderboards[username]["SQUADS STATS"] = {
        "Matches Played": squad_lifetime_stats["matches"]["value"],
        "Wins": squad_lifetime_stats["top1"]["value"],
        "Win %": squad_lifetime_stats["winRatio"]["value"],
        "Top 3s": squad_lifetime_stats["top3"]["value"],
        "Top 6s": squad_lifetime_stats["top6"]["value"],
        "Kills": squad_lifetime_stats["kills"]["value"],
        "K/D": squad_lifetime_stats["kd"]["value"]
    }

    solo_current_stats = data["stats"]["curr_p2"]
    solo_leaderboards[username]["CURRENT SEASON SOLO STATS"] = {
        "Matches Played": solo_current_stats["matches"]["value"],
        "Wins": solo_current_stats["top1"]["value"],
        "Win %": solo_current_stats["winRatio"]["value"],
        "Top 10s": solo_current_stats["top10"]["value"],
        "Top 25s": solo_current_stats["top25"]["value"],
        "Kills": solo_current_stats["kills"]["value"],
        "K/D": solo_current_stats["kd"]["value"]
    }

    duo_current_stats = data["stats"]["curr_p10"]
    solo_leaderboards[username]["CURRENT SEASON DUO STATS"] = {
        "Matches Played": duo_current_stats["matches"]["value"],
        "Wins": duo_current_stats["top1"]["value"],
        "Win %": duo_current_stats["winRatio"]["value"],
        "Top 5s": duo_current_stats["top5"]["value"],
        "Top 12s": duo_current_stats["top12"]["value"],
        "Kills": duo_current_stats["kills"]["value"],
        "K/D": duo_current_stats["kd"]["value"]
    }

    squad_current_stats = data["stats"]["curr_p9"]
    solo_leaderboards[username]["CURRENT SEASON SQUAD STATS"] = {
        "Matches Played": squad_current_stats["matches"]["value"],
        "Wins": squad_current_stats["top1"]["value"],
        "Win %": squad_current_stats["winRatio"]["value"],
        "Top 3s": squad_current_stats["top3"]["value"],
        "Top 6s": squad_current_stats["top6"]["value"],
        "Kills": squad_current_stats["kills"]["value"],
        "K/D": squad_current_stats["kd"]["value"]
    }

# print the solo stats for a given username
def print_solo_stats(username):
    for headers in solo_leaderboards[username]:
        print(headers)
        for keys, values in solo_leaderboards[username][headers].items():
            print(keys + ": " + values)

def populate_group_leaderboards(username, data):
    # add the new member
    group_leaderboards["Lifetime"].append({"name" : username, "Wins" : data["lifeTimeStats"][8]["value"]})
    print(group_leaderboards)

    # sort the group leaderboard
    group_leaderboards["Lifetime"] = sorted(group_leaderboards["Lifetime"], key=itemgetter('Wins'))
    print(group_leaderboards)

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

# Some test code for sorting and printing dictionaries
#print(config.leaderboard["Leaderboards"]["Lifetime"])
#config.leaderboard["Leaderboards"]["Lifetime"].append({"name": "test", "value": 4})
#config.leaderboard["Leaderboards"]["Lifetime"].append({"name": "test2", "value": 6})
#print(config.leaderboard["Leaderboards"]["Lifetime"])
#newlist = sorted(config.leaderboard["Leaderboards"]["Lifetime"], key=itemgetter('value'), reverse=True)
#print(newlist)
#print(newlist[0]["value"])
