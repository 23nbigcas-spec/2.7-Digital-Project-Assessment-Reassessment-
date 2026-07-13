def get_int():
    while True:
        try:
            num = int(input("\nEnter Here: "))
            return num 
            
        except ValueError:
            print("Invalid Input, Try again.")

def enter_team():
    print("How many teams would you like in the competition?")
    teams = get_int()

    team_list = []

    for i in range(teams):
        name =input(f"Team {i+1} name: ")

        team_list.append(name)

    return team_list


all_teams = enter_team()
print(all_teams)
print(f"number of teams registered: {len(all_teams)}")




