import requests

from main_deps.config import roster_url



def get_rosters(team):
    
    team_roster_url = roster_url+f"/{team}/current"
    
    print(f"Attempting pull from: {team_roster_url}")

    r = requests.get(team_roster_url)

    print(f"{team} roster status code: {r.status_code}")
    
    if r.status_code == 404:
        return 

    # Convert response object to dict
    response_dict = r.json()

    # Process results
    print(response_dict.keys())

    team_roster = {
        f"{team}": response_dict
    }

    
    return response_dict
    