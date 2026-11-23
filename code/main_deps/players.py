import json
from datetime import date



def get_players(roster):
    active_players = {}

    with open(roster, "r", encoding="utf-8") as file:
        rosters = json.load(file)
        
    for team in rosters:
        print(team)
        
        for position in rosters[team]:
            print(f'    {position}')
            
            for player in rosters[team][position]:
                print(f'        {player}')
                print(player["id"])
                
                
                active_players[player["id"]] = {
                    "id": player["id"], 
                    "firstName": player["firstName"]["default"], 
                    "lastName": player["lastName"]["default"], 
                    "sweaterNumber": player["sweaterNumber"], 
                    "team": team, 
                    "position": position, 
                    "positionCode": player["positionCode"], 
                    "heightInInches": player["heightInInches"], 
                    "weightInPounds": player["weightInPounds"], 
                    "heightInCentimeters": player["heightInCentimeters"], 
                    "weightInKilograms": player["weightInKilograms"], 
                    "birthDate": player["birthDate"], 
                    "birthCity": player["birthCity"]["default"], 
                    "birthCountry": player["birthCountry"],  
                    "shootsCatches": player["shootsCatches"], 
                    "headshot": player["headshot"], 
                    "acquisitionDate": date.today()
                }
        
    
    return active_players
