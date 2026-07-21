"""this is a program regarding a local fooball league.

My program aims to helps sort out the different wins and losses each team has.

And shows them in a aesthetically pleasing manner.
"""

MAX_VALUE = 10


def get_int():
    """Prompt user for a value, value must be positive."""
    while True:
        try:
            num = int(input("\nEnter Here: "))

            if num < 0:
                print("This cannot be negative, try again.")
            elif num >= MAX_VALUE:
                print("Number is Too high, please use a reasonable number.")
            else:
                return num
        except ValueError:
            print("Invalid Input, Try again.")


standings = [{"Team": "WAKATIPU", "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0},
             {"Team": "LAKES WAVES", "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0},
             {"Team": "CROMWELL", "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0},
             {"Team": "MAC", "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0}]


def print_standings():
    """Display the list called standings."""
    for i in standings:
        print(" ".join(f"|{k}: {v}|" for k, v in i.items()))


def enter_team():
    """Enter a team name, make sure it is unique and add it to the league."""
    while True:
        team_name = input(
            "\nWhat is the team name you would like to add?: "
            ).strip().upper()

        if len(team_name) < 15:
            break
        else:
            print("\n Team name is too long, please shorten")

        if not team_name:
            print("\nTeam name cannot be blank.")

        duplicate = False
        for teams in standings:
            if teams["Team"] == team_name:
                duplicate = True

        if duplicate:
            print("That team exists, please enter an original team.")
            continue
        break

    standings.append(
        {"Team": team_name, "P": 0, "W": 0, "L": 0, "D": 0, "PTS": 0}
        )
    print("NEW TEAM LIST")
    print("-" * 15)
    print_standings()


def view_teams():
    """Print a numbered list of all the registered teams."""
    print(f'\n{"TEAMS":<10}')
    print("-" * 15)
    for i in range(len(standings)):
        print(f'\n {i + 1}. {standings[i]["Team"]}')


def remove_team():
    """Remove a specific team from standings, if it exists."""
    view_teams()
    team_name = input(
        "\nWhat is the name of the team you would like to remove?: "
        ).strip().upper()

    check = False
    for i in range(len(standings)):
        if standings[i]["Team"] == team_name:
            standings.pop(i)
            print(f"\n{team_name} removed.")
            check = True
            break

    if not check:
        print("\nInvalid removal, please enter a proper team name.")


def admin_menu():
    """Display all options for user in menu."""
    print("\n---ADMIN MENU---")
    print("1. Enter match result ")
    print("2. Manage team lists")
    print("3. View Leaderboard")
    print("4. View all registered teams")
    print("5. Reset all standings")
    print("6. Exit")


def manage_team_menu():
    """Display enu for second option on admin menu."""
    print("1. Add Team")
    print("2. Remove Team")


def update_standings(team_name, result):
    """Update match statistics, and give respective points."""
    for row in standings:
        if row["Team"] == team_name:
            row["P"] += 1

            if result == "W":
                row["W"] += 1
                row["PTS"] += 3
            elif result == "D":
                row["D"] += 1
                row["PTS"] += 1
            elif result == "L":
                row["L"] += 1


def record_game():
    """Record scores from 2 teams and update standings."""
    active_teams = []
    for i in range(len(standings)):
        active_teams.append(standings[i]["Team"])
    print("Team options")
    print("=" * 15)
    print(*active_teams, sep="\n")

    if len(active_teams) < 2:
        print("\n2 teams must be in the league in order to record a game")
        return

    while True:
        home_team = input(
            "\nWhat is the first team in this match?: "
            ).strip().upper()

        if home_team in active_teams:
            print(f"{home_team} is available for this game")
            break
        else:
            print("invalid team name entered")

    while True:
        away_team = input(
            "\nWhat is the second team in this match?: "
            ).strip().upper()

        if away_team in active_teams and away_team != home_team:
            print(f"{away_team} is available for this game")
            break
        else:
            print(
                "invalid team name entered,"
                "team must be in list and not the same as home team."
                )

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
    """Reset all team statistics to 0."""
    for i in range(len(standings)):
        standings[i]["W"] = 0
        standings[i]["P"] = 0
        standings[i]["L"] = 0
        standings[i]["D"] = 0
        standings[i]["PTS"] = 0

    print("\nSTANDINGS RESET")


def starting_message():
    """Kind message to start programme."""
    print("=" * 15)
    print(" WELCOME to NHICO's SPORTS STANDING TRACKER")
    print("=" * 15)


def main():
    """Start main code."""
    while True:

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
            else:
                print("\nInvalid option, try again.")

        elif admin_choice == 3:
            print_standings()

        elif admin_choice == 4:
            view_teams()

        elif admin_choice == 5:
            reset_standings()

        elif admin_choice == 6:
            print("Thank you for using our service.")
            break

        else:
            print("INVALID OPTION, TRY AGAIN")


main()
