#############################################################################
#####                                                                   #####
#####  https://github.com/netplexflix/Exclusion-Label-Manager-for-Plex  #####
#####                                                                   #####
#############################################################################
from plexapi.myplex import MyPlexAccount
import requests
import xml.etree.ElementTree as ET

# Configuration
PLEX_TOKEN = "YOUR_PLEX_TOKEN"

def get_users():
    url = f"https://plex.tv/api/users?X-Plex-Token={PLEX_TOKEN}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        users = []
        for user_elem in root.findall('User'):
            users.append({
                'id': user_elem.get('id'),
                'username': user_elem.get('username').lower(),
                'title': user_elem.get('title'),
                'moviesFilter': user_elem.get('filterMovies', ''),
                'televisionFilter': user_elem.get('filterTelevision', '')
            })
        return users
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []

def update_label(user, label, sections, action="add"):
    url = f"https://plex.tv/api/users/{user['id']}?X-Plex-Token={PLEX_TOKEN}"
    params = {}
    changed = False

    for section in sections:
        current_filter = user.get(f'{section}Filter', '')
        filters = current_filter.split('&') if current_filter else []
        exclusion_syntax = f"label!={label}"
        
        if action == "add":
            if exclusion_syntax not in filters:
                filters.append(exclusion_syntax)
                param_name = "filterMovies" if section == "movies" else "filterTelevision"
                params[param_name] = '&'.join(filters)
                changed = True
        elif action == "remove":
            new_filters = [f for f in filters if f != exclusion_syntax]
            if new_filters != filters:
                param_name = "filterMovies" if section == "movies" else "filterTelevision"
                params[param_name] = '&'.join(new_filters)
                changed = True

    if not changed:
        return False

    try:
        response = requests.put(url, params=params)
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Error updating {user['title']}: {e}")
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
        if user['username'] in skip_users:
            print(f"Skipping user: {user['title']}")
            continue
        
        if update_label(user, label, sections, "add"):
            print(f"Added '{label}' exclusion to {user['title']}")
        else:
            print(f"No changes needed for {user['title']}")

def remove_label_action():
    label = input("Enter the label to remove: ").strip()
    if not label:
        print("Error: Label cannot be empty")
        return

    confirm = input(f"Remove '{label}' exclusion from all users? (y/n): ").lower()
    if confirm not in ('y', 'yes'):
        print("Operation canceled")
        return

    users = get_users()
    total_removed = 0
    
    for user in users:
        removed = False
        for section in ["movies", "television"]:
            current_filter = user.get(f'{section}Filter', '')
            if f"label!={label}" in current_filter.split('&'):
                if update_label(user, label, [section], "remove"):
                    removed = True
        if removed:
            print(f"Removed '{label}' exclusion from {user['title']}")
            total_removed += 1
    
    print(f"\nOperation complete. Removed from {total_removed} users.")

def main():
    print("Exclusion Label Manager for Plex")
    print("--------------------------------")
    
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