import requests
import json
import config

headers = {
    'TRN-Api-Key': config.api_key
}
response = requests.get('https://api.fortnitetracker.com/v1/profile/pc/snipe_celly34', headers = headers)

#print(response.text)
test = response.json()

#print(test["stats"]["p2"])
#print("###################")
#print(test["stats"]["p10"])
#print("###################")
#print(test["stats"]["p9"])
#print("###################")
#print(test["lifeTimeStats"])

print("LIFETIME TOTAL")
print(test["lifeTimeStats"][7]["key"] + " " + test["lifeTimeStats"][7]["value"])
print(test["lifeTimeStats"][8]["key"] + " " + test["lifeTimeStats"][8]["value"])
print(test["lifeTimeStats"][9]["key"] + " " + test["lifeTimeStats"][9]["value"])
print(test["lifeTimeStats"][10]["key"] + " " + test["lifeTimeStats"][10]["value"])
print(test["lifeTimeStats"][11]["key"] + " " + test["lifeTimeStats"][11]["value"])

print("\nCURRENT SEASON SOLO STATS")
print("# Matches: " + test["stats"]["curr_p2"]["matches"]["value"])
print("# Wins: " + test["stats"]["curr_p2"]["top1"]["value"])
print("Win %: " + test["stats"]["curr_p2"]["winRatio"]["value"])
print("# Top 10s: " + test["stats"]["curr_p2"]["top10"]["value"])
print("# Top 25s: " + test["stats"]["curr_p2"]["top25"]["value"])
print("Kills: " + test["stats"]["curr_p2"]["kills"]["value"])
print("K/D: " + test["stats"]["curr_p2"]["kd"]["value"])

#print("# Top 25: " + test["stats"]["p2"]["top25"]["valueInt"])

print("\nCURRENT SEASON DUO STATS")
print("# Matches: " + test["stats"]["curr_p10"]["matches"]["value"])
print("# Wins: " + test["stats"]["curr_p10"]["top1"]["value"])
print("Win %: " + test["stats"]["curr_p10"]["winRatio"]["value"])
print("# Top 5s: " + test["stats"]["curr_p10"]["top5"]["value"])
print("# Top 12s: " + test["stats"]["curr_p10"]["top12"]["value"])
print("Kills: " + test["stats"]["curr_p10"]["kills"]["value"])
print("K/D: " + test["stats"]["curr_p10"]["kd"]["value"])

print("\nCURRENT SEASON SQUAD STATS")
print("# Matches: " + test["stats"]["curr_p9"]["matches"]["value"])
print("# Wins: " + test["stats"]["curr_p9"]["top1"]["value"])
print("Win %: " + test["stats"]["curr_p9"]["winRatio"]["value"])
print("# Top 3s: " + test["stats"]["curr_p9"]["top3"]["value"])
print("# Top 6s: " + test["stats"]["curr_p9"]["top6"]["value"])
print("Kills: " + test["stats"]["curr_p9"]["kills"]["value"])
print("K/D: " + test["stats"]["curr_p9"]["kd"]["value"])

print("\nLIFETIME SOLO STATS")
print("# Matches: " + test["stats"]["p2"]["matches"]["value"])
print("# Wins: " + test["stats"]["p2"]["top1"]["value"])
print("Win %: " + test["stats"]["p2"]["winRatio"]["value"])
print("# Top 10s: " + test["stats"]["p2"]["top10"]["value"])
print("# Top 25s: " + test["stats"]["p2"]["top25"]["value"])
print("Kills: " + test["stats"]["p2"]["kills"]["value"])
print("K/D: " + test["stats"]["p2"]["kd"]["value"])
#print("# Top 25: " + test["stats"]["p2"]["top25"]["valueInt"])

print("\nLIFETIME DUO STATS")
print("# Matches: " + test["stats"]["p10"]["matches"]["value"])
print("# Wins: " + test["stats"]["p10"]["top1"]["value"])
print("Win %: " + test["stats"]["p10"]["winRatio"]["value"])
print("# Top 5s: " + test["stats"]["p10"]["top5"]["value"])
print("# Top 12s: " + test["stats"]["p10"]["top12"]["value"])
print("Kills: " + test["stats"]["p10"]["kills"]["value"])
print("K/D: " + test["stats"]["p10"]["kd"]["value"])

print("\nLIFETIME SQUAD STATS")
print("# Matches: " + test["stats"]["p9"]["matches"]["value"])
print("# Wins: " + test["stats"]["p9"]["top1"]["value"])
print("Win %: " + test["stats"]["p9"]["winRatio"]["value"])
print("# Top 3s: " + test["stats"]["p9"]["top3"]["value"])
print("# Top 6s: " + test["stats"]["p9"]["top6"]["value"])
print("Kills: " + test["stats"]["p9"]["kills"]["value"])
print("K/D: " + test["stats"]["p9"]["kd"]["value"])

#p2 = solo
#p10 = duo
#p9 = squad

#lifeTimeStats
