import json

from main_deps.teams import get_teams
from main_deps.rosters import get_rosters
from main_deps.players import get_players



all_teams = get_teams()

all_rosters = {}

for team in all_teams:
    roster = get_rosters(team)
    
    if roster: #Skips None/null/blank rosters
        all_rosters[team] = roster
    
print(all_rosters)

with open(r"data/rosters.json", "w", encoding="utf-8") as f:
    json.dump(all_rosters, f, indent=4)


active_players = get_players(r"data/rosters.json")

with open(r"data/players.json", "w", encoding="utf-8") as f:
        json.dump(active_players, f, indent=4)