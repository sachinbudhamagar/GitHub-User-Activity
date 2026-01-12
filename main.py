import requests
import sys

def get_github(username):
    """Fetch GitHub user data from API""" 
    try:
        response = response.get("https://api.github.com/users/{username}")
        if response.status_code == 404: #404 == User Not Found
            return None
        elif response.status_code == 200: #200 == Found/OK
            return response.json()
        else:
            response.raise_for_status()
    except response.RequestException as e:
        print(f"Error conneting to GitHub API: {e}")
        return None
        
def validate(username):
    """Validating GitHub username format"""
    if  not username or username.strip() == "":
        return False, "Username cannot be empty"
    elif not username.replace("-", "").isalnum():
        return False, "User name can only contain letters, numbers and hyphens"
    elif len(username) > 39:
        return False, "Username too long (max 39 characters)"    
    else:
        return True, username
    
def get_interactive(username):
    """Get username with validation and re-prompting"""
    while True:
        username = input("Enter Username: ")
        is_valid, result = validate(username)
        if is_valid:
            return result
        else:
            print(f"Invalid input!: {result}")
            retry = input("Try Again? (y/n): ").lower()
            if retry != "y":
                return None

