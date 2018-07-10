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
    "LIFETIME STATS":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "LIFETIME SOLO STATS":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "LIFETIME DUO STATS":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "LIFETIME SQUAD STATS":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "CURRENT SEASON SOLO STATS":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "CURRENT SEASON DUO STATS":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    },
    "CURRENT SEASON SQUAD STATS":{
        "Matches Played": [],
        "Wins": [],
        "Win %": [],
        "Kills": [],
        "K/D": []
    }
}

group_map = {
    "LIFETIME STATS": "lifeTimeStats",
    "LIFETIME SOLO STATS": "p2",
    "LIFETIME DUO STATS": "p10",
    "LIFETIME SQUAD STATS": "p9",
    "CURRENT SEASON SOLO STATS": "curr_p2",
    "CURRENT SEASON DUO STATS": "curr_p10",
    "CURRENT SEASON SQUAD STATS": "curr_p9"
}

# will store raw json data from fortnite tracker for all Players
# format will be { player name : fortnitetracker data }
raw_data = {}

# initialize stuff, right now just goes straight to main menu
def main():
    welcome_message()
    command = input("Enter Command: ")
    while(command != "--exit"):
        if (command == "--help"):
            help_message()
        else:
            add_players(command)
        #print_group_stats()
        command = input("Enter Command: ")

def welcome_message():
    print("Welcome to Fortnite Enhanced Leaderboards by James Nicol")
    print("Enter '--help' for a list of commands")

def help_message():
    print("Commands:")
    print("\n##############################################################\n")
    print("'--exit' - Exit the program")
    print("\n##############################################################\n")
    print("'--players' - view a list of all players current stored", end = "")
    print("in the system")
    print("\n##############################################################\n")
    print("'--stats p_name' - Display stats for player with username p_name")
    print("\n##############################################################\n")
    print("'--group p_n1, p_n2' - Display group leaderboards ", end = "")
    print("for 1 or more players, in this case p_n1 and p_n2")
    print("\n##############################################################\n")
    print("'--group all' - Display group leaderboards for all ", end = "")
    print("players current stored in the system")
    print("\n##############################################################\n")
    print("'--remove p_n1, p_n2' - Remove one or more players from ", end = "")
    print("the system, in this case p_n1 and p_n2")
    print("\n##############################################################\n")
    print("'--group all --remove p_n1' - Display group ", end = "")
    print("leaderboards for all players current stored in the ", end = "")
    print("system except for p_n1")
    print("NOTE: This command does not remove p_n1 from the system")
    print("\n##############################################################\n")


# add or remove a players data from the group leaderboards
def add_players(names):
    names = names.replace(" ", "")
    name = names.split(",")

    #print(name)
    for username in name:
        request_string = "https://api.fortnitetracker.com/v1/profile/pc/" + username
        response = requests.get(request_string, headers = config.headers)
        #print(response.text)
        data = response.json()
        #print(username)

        if(username not in solo_leaderboards):
            populate_solo_leaderboards(username, data)
            populate_group_leaderboards(username, data)
            #print_solo_stats(username)
            sleep(1)
        else:
            print(username + " already exists")


# populate the group leaderboard dictionary
def populate_solo_leaderboards(username, data):

    print("populating leaderboards for " + username)
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
    solo_leaderboards[username]["LIFETIME SOLO STATS"] = {
        "Matches Played": solo_lifetime_stats["matches"]["value"],
        "Wins": solo_lifetime_stats["top1"]["value"],
        "Win %": solo_lifetime_stats["winRatio"]["value"],
        "Top 10s": solo_lifetime_stats["top10"]["value"],
        "Top 25s": solo_lifetime_stats["top25"]["value"],
        "Kills": solo_lifetime_stats["kills"]["value"],
        "K/D": solo_lifetime_stats["kd"]["value"]
        }

    duo_lifetime_stats = data["stats"]["p10"]
    solo_leaderboards[username]["LIFETIME DUO STATS"] = {
        "Matches Played": duo_lifetime_stats["matches"]["value"],
        "Wins": duo_lifetime_stats["top1"]["value"],
        "Win %": duo_lifetime_stats["winRatio"]["value"],
        "Top 5s": duo_lifetime_stats["top5"]["value"],
        "Top 12s": duo_lifetime_stats["top12"]["value"],
        "Kills": duo_lifetime_stats["kills"]["value"],
        "K/D": duo_lifetime_stats["kd"]["value"]
    }

    squad_lifetime_stats = data["stats"]["p9"]
    solo_leaderboards[username]["LIFETIME SQUADS STATS"] = {
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
    group_leaderboards["LIFETIME STATS"]["Matches Played"].append({"name" : username, "value" : int(data["lifeTimeStats"][7]["value"])})
    group_leaderboards["LIFETIME STATS"]["Wins"].append({"name" : username, "value" : int(data["lifeTimeStats"][8]["value"])})
    group_leaderboards["LIFETIME STATS"]["Win %"].append({"name": username, "value": float(data["lifeTimeStats"][9]["value"].strip("%"))})
    group_leaderboards["LIFETIME STATS"]["Kills"].append({"name": username, "value": int(data["lifeTimeStats"][10]["value"])})
    group_leaderboards["LIFETIME STATS"]["K/D"].append({"name": username, "value": float(data["lifeTimeStats"][11]["value"])})
    #print(group_leaderboards)

    # For all other stats we can automate the collection using a mapping of
    # our labels to the data labels
    for key in group_map.keys():
        if (key != "LIFETIME STATS"):
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

def print_group_stats():
    for headers in group_leaderboards:
        print(headers)
        for keys, values in group_leaderboards[headers].items():
            print(keys)
            for element in values:
                print(element["name"] + ": " + str(element["value"]))

#program runs here
if __name__ == '__main__':
    main()

# Next Steps
# Error checking
# Command line commands
# Output formatting

# KNOWN ISSUES

# if the user hasnt played in the current season they have no stats for curr_p2
