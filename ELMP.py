#############################################################################
#####                                                                   #####
#####  https://github.com/netplexflix/Exclusion-Label-Manager-for-Plex  #####
#####                                                                   #####
#############################################################################
from plexapi.myplex import MyPlexAccount
import requests

# Configuration
PLEX_TOKEN = "YOUR_PLEX_TOKEN"

def get_users():
    try:
        account = MyPlexAccount(token=PLEX_TOKEN)
        return account.users()
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []

def update_label(user, label, sections, action="add"):
    url = f"https://plex.tv/api/users/{user.id}"
    headers = {"X-Plex-Token": PLEX_TOKEN}
    params = {}

    for section in sections:
        current_filter = getattr(user, f'{section}Filter', '') or ''
        filters = current_filter.split(',') if current_filter else []
        
        exclusion_syntax = f"label!={label}"  # "label=" writes to "ALLOW", "label!=" writes to "EXCLUDE"
        
        if action == "add":
            new_filter = ','.join(sorted(set(filters + [exclusion_syntax])))
        elif action == "remove":
            new_filter = ','.join([f for f in filters if f != exclusion_syntax])
        
        param_name = "filterMovies" if section == "movies" else "filterTelevision"
        params[param_name] = new_filter

    try:
        response = requests.put(url, headers=headers, params=params)
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Error updating {user.title}: {e}")
        return False

def add_label_action():
    label = input("Enter the label to add: ").strip()
    if not label:
        print("Error: Label cannot be empty")
        return

    skip_users = []
    skip_input = input("Enter comma-separated usernames to skip (or 'None'): ").strip()
    if skip_input.lower() != 'none':
        skip_users = [u.strip().lower() for u in skip_input.split(',') if u.strip()]

    sections = []
    while not sections:
        sections_input = input("Enter sections to apply (1=Movies, 2=TV Shows): ").strip()
        for s in sections_input.split(','):
            if s.strip() == '1':
                sections.append("movies")
            elif s.strip() == '2':
                sections.append("television")
        
        if not sections:
            print("Error: Please select at least one valid section")

    users = get_users()
    for user in users:
        if user.username.lower() in skip_users:
            print(f"Skipping user: {user.username}")
            continue
        
        if update_label(user, label, sections, "add"):
            print(f"Added '{label}' to {user.username}")
        else:
            print(f"Failed to update {user.username}")

def remove_label_action():
    label = input("Enter the label to remove: ").strip()
    if not label:
        print("Error: Label cannot be empty")
        return

    confirm = input(f"Remove '{label}' from all users and sections? (y/n): ").lower()
    if confirm not in ('y', 'yes'):
        print("Operation canceled")
        return

    users = get_users()
    for user in users:
        if update_label(user, label, ["movies", "television"], "remove"):
            print(f"Removed '{label}' from {user.username}")
        else:
            print(f"Failed to update {user.username}")

def main():
    print("Exclusion Label Manager for Plex")
    print("----------------------------")
    
    while True:
        action = input("\nChoose action (ADD/REMOVE/EXIT): ").strip().upper()
        if action == 'EXIT':
            break
        if action == 'ADD':
            add_label_action()
        elif action == 'REMOVE':
            remove_label_action()
        else:
            print("Invalid action. Please choose ADD, REMOVE, or EXIT.")

if __name__ == '__main__':
    main()