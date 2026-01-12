import requests
import sys

def get_github(username):
    """Fetch GitHub user data from API""" 
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 404: #404 == User Not Found
            return None
        elif response.status_code == 200: #200 == Found/OK
            return response.json()
        else:
            response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error connecting to GitHub API: {e}")
        return None
        
def validate(username):
    """Validating GitHub username format"""
    if  not username or username.strip() == "":
        return False, "Username cannot be empty"
    username = username.strip()
    if not username.replace("-", "").isalnum():
        return False, "User name can only contain letters, numbers and hyphens"
    if len(username) > 39:
        return False, "Username too long (max 39 characters)"    
    return True, username
    
def get_interactive():
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


def main():
    """Checking for command-line argument first"""
    if len(sys.argv) > 1:
        username = sys.argv[1]
        is_valid, result = validate(username)
        if not is_valid:
            print(f"Error: {result}")
            sys.exit(1)
        username = result
    else:
        username = get_interactive()
        if username is None:
            print(f"Exiting...")
            sys.exit(0)

    print(f"Fetching data for '{username}'..")
    user_data = get_github(username)

    if user_data:
        print(f"\n User found: {user_data['login']}")
        print(f"Name: {user_data.get('name', 'N/A')}")
        print(f"Public repos: {user_data.get('public_repos', 0)}")
    else:
        print(f"User '{username}' not found")
        sys.exit(1)

if __name__ =="__main__":
    main()