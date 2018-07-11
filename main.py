import requests
import config
import json
import re
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

input_commands = [
    "--exit",
    "--players",
    "--stats",
    "--help",
    "--group",
    "--remove"
]

# will store raw json data from fortnite tracker for all Players
# format will be { player name : fortnitetracker data }
raw_data = {}

# initialize stuff, right now just goes straight to main menu
def main():
    welcome_message()

    # regex parsing the input, we divide commands by two delimeters,
    # commas and spaces (any number of them)
    command = re.split("[, ]+", input("Enter Command: "))
    # we only want to exit when --exit is entered as the only command
    # the or condition means that we don't accept commands such as
    # "--exit rtedsadasd" because the length of the command is > 1
    # conditions are only met when command[0] is "--exit" and the
    # length is 1
    while(command[0] != "--exit" or len(command) > 1):
        # if the first input is not a valid command, display an error message
        if (command[0] not in input_commands):
            print("Invalid command, enter '--help' for valid commands")
        # display help message
        elif (command[0] == "--help"):
            help_message()
        # display a list of players currently stored in dictionary
        elif (command[0] == '--players'):
            print("printing a list of players")

        # display stats for player with name in command[1], if the player
        # is not in the system, query FortniteTracker API. If nothing is
        # returned then return an error message. If the player is in the
        # system already, pull their existing data (not stored outside of
        # runtime so not a big deal)
        elif (command[0] == '--stats'):
            print("printing stats for p_name")

        # display group leaderboards based on input parameters
        elif (command[0] == '--group'):
            print("group leaderboard commands")
            # using lazy evalutation here to prevent errors
            if (len(command) > 1 and command[1] == '--players'):
                print("all command entered")
                if (len(command) > 2 and command[2] == '--remove'):
                    print("group all command with remove players")

        # remove a players data from storage, not sure why this would be
        # super useful because data is not stored outside of runtime but
        # good to have the option
        elif (command[0] == '--remove'):
            print("removing one or more player")

        print(command)
        command = re.split("[, ]+", input("Enter Command: "))

# Message that the user sees on startup
def welcome_message():
    print("Welcome to Fortnite Enhanced Leaderboards by James Nicol")
    print("Enter '--help' for a list of commands")

# help message to explain all available commands with examples
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
    print("'--group --players' - Display group leaderboards for all ", end = "")
    print("players current stored in the system")
    print("\n##############################################################\n")
    print("'--remove p_n1, p_n2' - Remove one or more players from ", end = "")
    print("the system, in this case p_n1 and p_n2")
    print("\n##############################################################\n")
    print("'--group --players --remove p_n1' - Display group ", end = "")
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
