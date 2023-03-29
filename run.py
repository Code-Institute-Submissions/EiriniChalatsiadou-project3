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

# Here is the function for the username


def get_user_name():
    """
    This is the function that gets the name from the user
    """
    print('Welcome!\n')
    print('Do you like NBA? Explore the stats for season 2021-22\n')
    name_str = input("Please enter your name: ")
    clear_screen()
    print(f"Wow! This is a great name! Welcome {name_str.upper()}!!!!!\n")


# Function with players stats

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
    print(f"The data option provided is {data_option}\n")
    return data_option


# validate_username(username)

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
    except ValueError:
        print(
            "Invalid data. Please input a correct option integer [1-8]\n")


get_user_name()
player_stat = get_player_stat_option()
validate_player_stat_option(player_stat)

# data = player_total_stats.get_all_values()
# print(data)
