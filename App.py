import constants
from copy import deepcopy
import csv
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def clean_constants():
    teams = constants.TEAMS[:]
    players = deepcopy(constants.PLAYERS)
    for player in players:
        player["height"] = player['height'].split()
        player['height'] = int(player['height'][0])
        player['guardians'] = player['guardians'].split(" and ")
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    
    return players, teams


def divide_players(players, teams):
    panthers = []
    bandits = []
    warriors = []
    experienced_players = [player for player in players if player['experience'] == True]
    inexperienced_players = [player for player in players if player['experience'] == False]

    while experienced_players:
        panthers.append(experienced_players.pop())
        bandits.append(experienced_players.pop())
        warriors.append(experienced_players.pop())
    while inexperienced_players:
        panthers.append(inexperienced_players.pop())
        bandits.append(inexperienced_players.pop())
        warriors.append(inexperienced_players.pop())
    
    teams_list = [panthers, bandits, warriors]

    return panthers, bandits, warriors, teams_list


def welcome():
    app_name = "TONY's BASKETBALL TEAM STATS TOOL"
    print("~" * len(app_name))
    print(app_name)
    print("~" * len(app_name), end="\n\n")
    print("=" * 10, "MENU", "=" * 10, end="\n")


def menu():
    COMMANDS = ["Display Team Stats", "Help", "Quit"]
    for index, item in enumerate(COMMANDS, start = 1):
        print("{}) {}".format(index, item))
    print()


def sub_menu():
    for index, item in enumerate(constants.TEAMS, start=1):
        print("{}) {}".format(index, item))
    print()


def display_team_info(option):
    try:
        team = teams_list[int(option) - 1]
        players_on_team = [player['name'] for player in team]
        average_height = round(sum([player["height"] for player in team]) / len(players_on_team), 2)
        experienced_players = len([player['experience'] for player in team if player['experience'] == True])
        inexperienced_players = len([player['experience'] for player in team if player['experience'] == False])
        guardians = [", ".join(player['guardians']) for player in team]
        print("\n\nTEAM: {} Stats".format(constants.TEAMS[int(option) - 1]))
        print("~" * 26, "\n")
        print("Total Players: {}".format(len(team)))
        print("Number of Experienced Players: {}".format(experienced_players))
        print("Number of Inexperienced Players: {}".format(inexperienced_players))
        print("Average Height: {} inches\n".format(average_height))
        print("Players on Team: ""\n", end="")
        for player in players_on_team:
            if player == players_on_team[-1]:
                print(player)
            else:
                print(player, end=", ")
        print("\n""Guardians: ""\n", end="")
        for guardian in guardians:
            if guardian == guardians[-1]:
                print(guardian, end="\n\n")
            else:
                print(guardian, end=", ")
        input("Press Enter to continue...")
        clear_screen()
        welcome()
    except IndexError:
        print("\nThat is not a valid option. Please try again. \n")
    except ValueError:
        print("\nThat is not a valid option. Please try again. \n")


def main():
    while True:
        menu()
        command = input("Please enter the number for the COMMAND that you want >   ")
        print()
        if command == '1':
            sub_menu()
            option = input("Please enter the number for the OPTION that you want >   ")
            display_team_info(option)
            print()
            pass
        elif command == '2':
            clear_screen()
            print('Team Stats will display a submenu to choose which team stats to display')
            print('Help will display this message and the main menu')
            print('Quit will exit the program')
            print()
            continue
        elif command == '3':
            print("Thanks for checking in!!")
            print("Come back to get more Tony's Basketball stats! Good bye!\n\n")
            break
        else:
            print("\nThat is not a valid option. Please try again. \n")
            continue


if __name__ == "__main__":
    panthers, bandits, warriors, teams_list = divide_players(*clean_constants())
    clear_screen()
    welcome()

    main()
