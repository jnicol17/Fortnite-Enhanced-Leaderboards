import requests
import config
#import json
from time import sleep

def main():

    headers = {
        'TRN-Api-Key': config.api_key
    }

    name = input("Fortnite Name: ")
    while (name != "e"):
        request_string = "https://api.fortnitetracker.com/v1/profile/pc/" + name
        response = requests.get(request_string, headers = headers)
        #print(response.text)
        data = response.json()
        print_stats(data)
        #p2 = solo
        #p10 = duo
        #p9 = squad
        #lifeTimeStats
        name = input("Fortnite Name: ")
        sleep(1)



def print_stats(data):
    print("Name: " + data["epicUserHandle"])
    print("Platform: " + data["platformNameLong"])

    lifetime_stats = data["lifeTimeStats"]

    solo_lifetime_stats = data["stats"]["p2"]
    duo_lifetime_stats = data["stats"]["p10"]
    squad_lifetime_stats = data["stats"]["p9"]

    solo_current_stats = data["stats"]["curr_p2"]
    duo_current_stats = data["stats"]["curr_p10"]
    squad_current_stats = data["stats"]["curr_p9"]

    print_lifetime_stats(lifetime_stats)

    print_solo_lifetime_stats(solo_lifetime_stats)
    print_duo_lifetime_stats(duo_lifetime_stats)
    print_squad_lifetime_stats(squad_lifetime_stats)

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

#program runs here
if __name__ == '__main__':
    main()
