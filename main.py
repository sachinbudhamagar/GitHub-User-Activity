import requests
import sys

def get_github(username):
    #Fetch GitHub API 
    try:
        response = response.get("https://api.github.com/users/{username}")
        if response.status_code == 404:
            return None
        elif response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    except response.RequestException as e:
        print(f"Error conneting to GitHub API: {e}")
        return None
        