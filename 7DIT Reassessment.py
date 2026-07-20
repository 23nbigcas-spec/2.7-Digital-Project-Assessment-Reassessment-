"""this is a program regarding a local fooball league.

My program aims to helps sort out the different wins and losses each team has.

And shows them in a aesthetically pleasing manner.
"""


def get_int():
    """A function for whenever an integer is needed."""
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


def print_standings():
    """Prints the list called standings, and makes it look nice and ordered."""
    print(*standings, sep="\n")


def enter_team():
    """Has the user enter a team and inserts it into the list of teams."""
    team_name = input("\nWhat is the team name you would like to add?: ").strip().capitalize()
    standings.append({"Team": team_name, "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0})
    print(*standings, sep="\n")


def remove_team():
    """Has user enter a team and functions searches for it in list using the key Team, as a way to search."""
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
    """Searches for all of the information in each dictonary under the key Teams, and prints it out."""
    print(f'{"TEAMS":<10}')
    print("--------------------")
    for i in range(len(standings)):
        print(f'{standings[i]["Team"]}')


def admin_menu():
    """Prints all options for user in menu."""
    print("\n---ADMIN MENU---")
    print("1. Enter match result ")
    print("2. Manage team lists")
    print("3. View Leaderboard")
    print("4. View all registered teams")
    print("5. Reset all standings")
    print("6. Exit")


def manage_team_menu():
    """Menu for second option on admin menu."""
    print("1. Add Team")
    print("2. Remove Team")


def update_standings(team_name, result):
    """Uses the parameters and looks at the key Team.

    If team is same as team_name then it changes the information stored in the key.
    """
    for row in standings:
        if row["Team"] == team_name:
            row["P"] += 1

            if result == "W":
                row["W"] += 1
                row["PTS"] += 3
            elif result == "D":
                row["W"] += 1
                row["PTS"] += 1
            elif result == "L":
                row["L"] += 1


def record_game():
    """Gets user to choose 2 teams from key Teams, and gets the points scored from game.

    It has different points depending on wins/losses and changes different parts of keys"""
    active_teams = []
    for i in range(len(standings)):
        active_teams.append(standings[i]["Team"])
    print("Team options")
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

        if away_team in active_teams and away_team != home_team:
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
    """Gets all keys and resets them to 0."""
    for i in range(len(standings)):
        standings[i]["W"] = 0
        standings[i]["P"] = 0
        standings[i]["L"] = 0
        standings[i]["D"] = 0
        standings[i]["PTS"] = 0

    print("\nSTANDINGS RESET")


while True:
    """Main code"""
    admin_menu()

    admin_choice = get_int()

    if admin_choice == 1:
        record_game()

    elif admin_choice == 2:
        manage_team_menu()
        manage_choice = get_int()
        if manage_choice == 1:
            enter_team()
        elif manage_choice == 2:
            remove_team()

    elif admin_choice == 3:
        print_standings()
    
    elif admin_choice == 4:
        view_teams()

    elif admin_choice == 5:
        reset_standings()

    elif admin_choice == 6:
        print("Thank you for using our service.")
        break
