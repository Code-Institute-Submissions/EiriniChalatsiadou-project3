import gspread
import os
from google.oauth2.service_account import Credentials
# Here is the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
# Here is the creds, sheet and the libraries
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("nba_stats_2022")

player_total_stats = SHEET.worksheet("Player_Totals")


def clear_screen():
    """ 
    Clear screen
    """
    os.system('clear')


def get_user_name():
    """
    This is the function that gets the name from the user
    """
    name_str = input("Please enter your name: ")
    return name_str


def get_player_stat_option():
    """
    This is the function with the players stats options
    """
    print('What do you want to know about? Please, choose an option 1-8')
    print('1) Points\n')
    print('2) Steals\n')
    print('3) Blocks\n')
    print('4) Rebounds\n')
    print('5) FT%\n')
    print('6) 2PT%\n')
    print('7) 3PT%\n')
    print('8) Quit\n')
    data_option = input('Please, enter your option (a number 1-8): ')
    return data_option


def validate_username(username):
    """
    If the username is empty raise ValueError
    """
    try:
        if username == "":
            raise ValueError()
    except ValueError:
        return False

    return True


def validate_player_stat_option(option):
    """
    Validate player_stat to be an integer number between 1-8
    Raises ValueError if not integer or if not in this range.
    Also prints the error.
    """
    try:
        player_int_option = int(option)
        if (player_int_option < 1 or player_int_option > 8):
            raise ValueError()
        if player_int_option == 8:
            print("Thank you for using our program! Bye!!")
            exit()
    except ValueError:
        return False

    return True


def print_introduction():
    """
    Prints the program introduction.
    """
    print('Welcome!\n')
    print('Do you like NBA? Explore the stats for season 2021-22\n')


def get_stat_columns_to_be_removed(full_data, stat_options):
    """
    From all the data, return the indexes of the columns that we want to 
    remove - column names not in stat options plus Player column
    """
    headers = full_data[0]
    stat_options['Player'] = 'Player'
    desired_stats = stat_options.values()
    
    column_positions_to_be_removed = [
        i for i, item in enumerate(headers) if item not in desired_stats]

    return column_positions_to_be_removed




stat_options = {1: "PTS", 2: "STL", 3: "BLK",
                4: "TRB", 5: "FT%", 6: "2P%", 7: "3P%"}


# def remove_unused_columns(full_data, stat_options ):


# print_introduction()
# while True:
#     username = get_user_name()
#     if validate_username(username):
#         clear_screen()
#         print(f"Wow! This is a great name! Welcome {username.upper()}!!!!!\n")
#         break
#     else:
#         clear_screen()
#         print("Invalid data. Please input a valid name\n")


# while True:
#     player_stat = get_player_stat_option()
#     if validate_player_stat_option(player_stat):
#         break
#     else:
#         clear_screen()
#         print("Invalid data. Please input a correct option integer [1-8]\n")


data = player_total_stats.get_all_values()

get_stat_columns_to_be_removed(data, stat_options)

print(data[0])
