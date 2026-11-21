import requests

from main_deps.config import teams_url



def get_teams():
    print(teams_url)

    r = requests.get(teams_url)

    print(f"Status code: {r.status_code}")

    # Convert response object to dict
    response_dict = r.json()

    # Process results
    #print(response_dict["data"])
    
    all_teams = []
    for team in response_dict["data"]:
        all_teams.append(team["triCode"])
        
    return all_teams