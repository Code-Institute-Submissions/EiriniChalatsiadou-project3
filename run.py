from operator import itemgetter
import os
import gspread
from numpy import delete
from google.oauth2.service_account import Credentials
import pandas as pd
from tabulate import tabulate

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
    remove - column names not in stat options plus Player and Pos columns
    """
    headers = full_data[0]
    stat_options['Player'] = 'Player'
    stat_options['Pos'] = 'Pos'
    desired_stats = stat_options.values()

    column_positions_to_be_removed = [
        i for i, item in enumerate(headers) if item not in desired_stats]

    return column_positions_to_be_removed


def remove_unused_columns(full_data, column_indexes_to_be_removed):
    """
    Removes from full stat data columns that we dont really need.
    """
    for ind, row in enumerate(full_data):
        full_data[ind] = delete(row, column_indexes_to_be_removed).tolist()

    return full_data


def calculate_data_stat_column_number(
        filtered_data,
        stat_option_number,
        stat_options):
    """
    Take data headers and find the column number of given 
    option based on option number.
    """
    option_name = stat_options[stat_option_number]
    headers = filtered_data[0]
    column_number = headers.index(option_name)
    return column_number


def sort_list_by_stat_option(
        filtered_data,
        column_number,
        from_top,
        number_of_players):
    """
    Sort list by stat option and return only given number 
    of players from top/bottom. 
    """
    headers = filtered_data[0]
    del filtered_data[0]
    data_sorted_by_stat = sorted(filtered_data,
                                 key=itemgetter(column_number),
                                 reverse=from_top)
    filtered_data.insert(0, headers)
    result = data_sorted_by_stat[0:number_of_players]
    result.insert(0, headers)
    return result


def convert_string_to_float_or_integer(str):
    """
    Converts str to either integer or float if it can be converted.
    Else returns string.
    """
    try:
        integer_number = int(str)
        return integer_number
    except ValueError:
        pass

    try:
        float_number = float(str)
        return float_number
    except ValueError:
        pass

    return str


def convert_list_data_from_string_to_numbers(data_list):
    """
    data_list is a list of lists. Excluding the first row which is header
    convert the rest rows from string to either integer or float
    depending the data
    """
    for ind, row in enumerate(data_list):
        if ind != 0:
            # expression for item in iterable if condition == True
            data_list[ind] = [
                convert_string_to_float_or_integer(item) for item in row]

    return data_list


def pretty_print(list):
    """
    Formats and prints a list in rows / columns.
    """
    df = pd.DataFrame(list)
    print(tabulate(df, headers='keys', tablefmt='psql'))


stat_options = {1: "PTS", 2: "STL", 3: "BLK",
                4: "TRB", 5: "FT%", 6: "2P%", 7: "3P%"}

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

unused_columns = get_stat_columns_to_be_removed(data, stat_options)
filtered_data = remove_unused_columns(data, unused_columns)
filtered_data = convert_list_data_from_string_to_numbers(filtered_data)
n = calculate_data_stat_column_number(filtered_data, 4, stat_options)

r = sort_list_by_stat_option(filtered_data, n, True, 10)
print(n, filtered_data[0])
pretty_print(r)
