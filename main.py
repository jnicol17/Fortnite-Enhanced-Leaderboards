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
    "Lifetime":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "SoloStats":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "DuoStats":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "SquadStats":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "CurrSolo":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "CurrDuo":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "CurrSquad":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    }
}



group_map = {
    "Lifetime": "lifeTimeStats",
    "SoloStats": "p2",
    "DuoStats": "p10",
    "SquadStats": "p9",
    "CurrSolo": "curr_p2",
    "CurrDuo": "curr_p10",
    "CurrSquad": "curr_p9"
}



# will store raw json data from fortnite tracker for all Players
# format will be { player name : fortnitetracker data }
raw_data = {}

# initialize stuff, right now just goes straight to main menu
def main():
    add_players()
    print_group_stats()

# add or remove a players data from the group leaderboards
def add_players():
    names = input("Fortnite Name: ")
    names = names.replace(" ", "")
    name = names.split(",")

    #print(name)
    for username in name:
        request_string = "https://api.fortnitetracker.com/v1/profile/pc/" + username
        response = requests.get(request_string, headers = config.headers)
        #print(response.text)
        data = response.json()
        #print(username)

        populate_solo_leaderboards(username, data)
        populate_group_leaderboards(username, data)

        sleep(1)

# view the stored stats for a player given the username, currently it asks
# for the name after the user has already selected this menu item, may
# change that so that a user can enter "2 snipe_celly34" to look up
# snipe_celly34's stats with one command
def view_individual_stats():
    name = input("Enter Users name: ")
    print_solo_stats(name)

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

    # Need to add lifetime stats separately because they are not indexed the
    # same way in the data json that we receive from FortniteTracker
    group_leaderboards["Lifetime"]["Matches Played"].append({"name" : username, "value" : int(data["lifeTimeStats"][7]["value"])})
    group_leaderboards["Lifetime"]["Wins"].append({"name" : username, "value" : int(data["lifeTimeStats"][8]["value"])})
    group_leaderboards["Lifetime"]["Win %"].append({"name": username, "value": float(data["lifeTimeStats"][9]["value"].strip("%"))})
    group_leaderboards["Lifetime"]["Kills"].append({"name": username, "value": int(data["lifeTimeStats"][10]["value"])})
    group_leaderboards["Lifetime"]["K/D"].append({"name": username, "value": float(data["lifeTimeStats"][11]["value"])})
    #print(group_leaderboards)

    # For all other stats we can automate the collection using a mapping of
    # our labels to the data labels
    for key in group_map.keys():
        if (key != "Lifetime"):
            group_leaderboards[key]["Matches Played"].append({
                "name": username,
                "value": int(data["stats"][group_map[key]]["matches"]["value"])
            })
            group_leaderboards[key]["Wins"].append({
                "name": username,
                "value": int(data["stats"][group_map[key]]["top1"]["value"])
            })
            group_leaderboards[key]["Win %"].append({
                "name": username,
                "value": float(data["stats"][group_map[key]]["winRatio"]["value"])
            })
            group_leaderboards[key]["Kills"].append({
                "name": username,
                "value": int(data["stats"][group_map[key]]["kills"]["value"])
            })
            group_leaderboards[key]["K/D"].append({
                "name": username,
                "value": float(data["stats"][group_map[key]]["kd"]["value"])
            })
    #print(group_leaderboards)
    # sort the group Leaderboards
    for key in group_map.keys():
        group_leaderboards[key]["Matches Played"] = sorted(
            group_leaderboards[key]["Matches Played"],
            key=itemgetter('value'),
            reverse=True
        )
        group_leaderboards[key]["Wins"] = sorted(
            group_leaderboards[key]["Wins"],
            key=itemgetter('value'),
            reverse=True
        )
        group_leaderboards[key]["Win %"] = sorted(
            group_leaderboards[key]["Win %"],
            key = itemgetter('value'),
            reverse=True
        )
        group_leaderboards[key]["Kills"] = sorted(
            group_leaderboards[key]["Kills"],
            key = itemgetter('value'),
            reverse=True
        )
        group_leaderboards[key]["K/D"] = sorted(
            group_leaderboards[key]["K/D"],
            key = itemgetter('value'),
            reverse=True
        )
        #print(group_leaderboards[key]["Wins"])
        #print(group_leaderboards[key]["Win %"])
        #print(group_leaderboards[key]["Kills"])
        #print(group_leaderboards[key]["K/D"])
    #print(group_leaderboards)

def print_group_stats():
    print("\n")
    for headers in group_leaderboards:
        print(headers)
        for keys, values in group_leaderboards[headers].items():
            print(keys)
            for element in values:
                print(element["name"] + ": " + str(element["value"]))

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

# KNOWN ISSUES

# if the user hasnt played in the current season they have no stats for curr_
