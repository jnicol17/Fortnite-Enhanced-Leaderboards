import requests
import json
import config

headers = {
    'TRN-Api-Key': config.api_key
}
response = requests.get('https://api.fortnitetracker.com/v1/profile/pc/snipe_celly34', headers = headers)

#print(response.text)
data = response.json()

print("Name: " + data["epicUserHandle"])
print("Platform: " + data["platformNameLong"])

lifetime_stats = data["lifeTimeStats"]

solo_lifetime_stats = data["stats"]["p2"]
duo_lifetime_stats = data["stats"]["p10"]
squad_lifetime_stats = data["stats"]["p9"]

solo_current_stats = data["stats"]["curr_p2"]
duo_current_stats = data["stats"]["curr_p10"]
squad_current_stats = data["stats"]["curr_p9"]

print("\nLIFETIME TOTAL")
print(lifetime_stats[7]["key"] + ": " + lifetime_stats[7]["value"])
print(lifetime_stats[8]["key"] + ": " + lifetime_stats[8]["value"])
print(lifetime_stats[9]["key"] + ": " + lifetime_stats[9]["value"])
print(lifetime_stats[10]["key"] + ": " + lifetime_stats[10]["value"])
print(lifetime_stats[11]["key"] + ": " + lifetime_stats[11]["value"])

print("\nLIFETIME SOLO STATS")
print("# Matches: " + solo_lifetime_stats["matches"]["value"])
print("# Wins: " + solo_lifetime_stats["top1"]["value"])
print("Win %: " + solo_lifetime_stats["winRatio"]["value"])
print("# Top 10s: " + solo_lifetime_stats["top10"]["value"])
print("# Top 25s: " + solo_lifetime_stats["top25"]["value"])
print("Kills: " + solo_lifetime_stats["kills"]["value"])
print("K/D: " + solo_lifetime_stats["kd"]["value"])
#print("# Top 25: " + test["stats"]["p2"]["top25"]["valueInt"])

print("\nLIFETIME DUO STATS")
print("# Matches: " + duo_lifetime_stats["matches"]["value"])
print("# Wins: " + duo_lifetime_stats["top1"]["value"])
print("Win %: " + duo_lifetime_stats["winRatio"]["value"])
print("# Top 5s: " + duo_lifetime_stats["top5"]["value"])
print("# Top 12s: " + duo_lifetime_stats["top12"]["value"])
print("Kills: " + duo_lifetime_stats["kills"]["value"])
print("K/D: " + duo_lifetime_stats["kd"]["value"])

print("\nLIFETIME SQUAD STATS")
print("# Matches: " + squad_lifetime_stats["matches"]["value"])
print("# Wins: " + squad_lifetime_stats["top1"]["value"])
print("Win %: " + squad_lifetime_stats["winRatio"]["value"])
print("# Top 3s: " + squad_lifetime_stats["top3"]["value"])
print("# Top 6s: " + squad_lifetime_stats["top6"]["value"])
print("Kills: " + squad_lifetime_stats["kills"]["value"])
print("K/D: " + squad_lifetime_stats["kd"]["value"])

print("\nCURRENT SEASON SOLO STATS")
print("# Matches: " + solo_current_stats["matches"]["value"])
print("# Wins: " + solo_current_stats["top1"]["value"])
print("Win %: " + solo_current_stats["winRatio"]["value"])
print("# Top 10s: " + solo_current_stats["top10"]["value"])
print("# Top 25s: " + solo_current_stats["top25"]["value"])
print("Kills: " + solo_current_stats["kills"]["value"])
print("K/D: " + solo_current_stats["kd"]["value"])

#print("# Top 25: " + test["stats"]["p2"]["top25"]["valueInt"])

print("\nCURRENT SEASON DUO STATS")
print("# Matches: " + duo_current_stats["matches"]["value"])
print("# Wins: " + duo_current_stats["top1"]["value"])
print("Win %: " + duo_current_stats["winRatio"]["value"])
print("# Top 5s: " + duo_current_stats["top5"]["value"])
print("# Top 12s: " + duo_current_stats["top12"]["value"])
print("Kills: " + duo_current_stats["kills"]["value"])
print("K/D: " + duo_current_stats["kd"]["value"])

print("\nCURRENT SEASON SQUAD STATS")
print("# Matches: " + squad_current_stats["matches"]["value"])
print("# Wins: " + squad_current_stats["top1"]["value"])
print("Win %: " + squad_current_stats["winRatio"]["value"])
print("# Top 3s: " + squad_current_stats["top3"]["value"])
print("# Top 6s: " + squad_current_stats["top6"]["value"])
print("Kills: " + squad_current_stats["kills"]["value"])
print("K/D: " + squad_current_stats["kd"]["value"])

#p2 = solo
#p10 = duo
#p9 = squad

#lifeTimeStats
