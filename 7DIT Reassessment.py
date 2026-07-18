def get_int():
    while True:
        try:
            num = int(input("\nEnter Here: "))
            return num 
            
        except ValueError:
            print("Invalid Input, Try again.")

standings = [{"Team": "Wakatipu", "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0},
             {"Team": "Lakes waves", "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0},
             {"Team": "Cromwell", "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0},
             {"Team": "Mac", "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0}]

def enter_team():
    team_name = input("\nWhat is the team name you would like to add?: ").strip().capitalize()
    standings.append({"Team": team_name, "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0})
    print(*standings, sep="\n")

def remove_team():
    team_name = input("\nWhat is the team name you would like to remove?: ").strip().capitalize()

    try:
        for i in range(len(standings)):
            if standings[i]["Team"] == team_name:
                standings.pop(i)
                break

        print(*standings, sep="\n")
    
    except ValueError: 
        print("Invalid Input, Try again.")

def view_teams():
    print(f'{"TEAMS":<10}') 
    print("--------------------")
    for i in range(len(standings)):
        print(f'{standings[i]["Team"]}')

def admin_menu():
    print("\n---ADMIN MENU---")
    print("1. Enter match result ")
    print("2. Manage team lists")
    print("3. View Leaderboard")
    print("4. View all registered teams")
    print("5. Reset all standings")
    print("6. Exit")

def manage_team_menu():
    print("1. Add Team")
    print("2. Remove Team")

def update_standings(team_name, result):
    for row in standings:
        if row["Team"] == team_name:
            row["P"] += 1
        
            if  result == "W":
                row["W"] += 1
                row["PTS"] += 3
            elif result == "D":
                row["W"] += 1
                row["PTS"] += 1
            elif result == "L":
                row["L"] += 1

def record_game():
    active_teams = []
    for i in range(len(standings)):
        active_teams.append(standings[i]["Team"])
    print(f"Team options")
    print(*active_teams)
    while True:
        home_team = input("\nWhat is the first team in this match?: ").strip().capitalize()

        if home_team in active_teams:
            print(f"{home_team} is available for this game")
            break
        else:
            print("invalid team name entered")

    while True:
        away_team = input("\nWhat is the second team in this match?: ").strip().capitalize()
    
        if away_team in active_teams and away_team != home_team :
            print(f"{away_team} is available for this game")
            break
        else:
            print("invalid team name entered, team must be in list and not the same as home team.")

    print(f"{home_team} VS {away_team}")

    print(f"How many goals did {home_team} score?")
    home_goals = get_int()

    print(f"How many goals did {away_team} score?")
    away_goals = get_int()



    if home_goals > away_goals:
        print(f"{home_team} WON")
        update_standings(home_team, "W")
        update_standings(away_team, "L")
    elif home_goals < away_goals:
        print(f"{away_team} WON")
        update_standings(home_team, "L")
        update_standings(away_team, "W")
    elif home_goals == away_goals:
        print(f"{home_team} and {away_team} DREW")
        update_standings(home_team, "D")
        update_standings(away_team, "D")

def reset_standings():
    for i in range(len(standings)):
        standings[i]["W"] = 0
        standings[i]["P"] = 0
        standings[i]["L"] = 0
        standings[i]["D"] = 0
        standings[i]["PTS"] = 0

    print("\nSTANDINGS RESET")

