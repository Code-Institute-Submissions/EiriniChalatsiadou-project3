"""Main module"""
from operator import itemgetter
import gspread
from numpy import delete
from google.oauth2.service_account import Credentials
import pandas as pd
from tabulate import tabulate
from prettytable import PrettyTable
from user_input import get_number_of_players, get_player_stat_option, \
    get_top_bottom_players_option, get_user_name, get_user_wants_to_continue, \
    clear_screen

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
SHEET = GSPREAD_CLIENT.open("nba_stats_2021_2022")

player_total_stats = SHEET.worksheet("Player_Totals")

stat_options = {"1": "PTS", "2": "STL", "3": "BLK",
                "4": "TRB", "5": "FT%", "6": "2P%", "7": "3P%"}


def print_introduction():
    """
    Prints the program introduction.
    """
    print('Welcome!\n')
    print('Do you like NBA? Explore the stats for season 2021-22\n')


def get_stat_columns_to_be_removed(full_data):
    """
    From all the data, return the indexes of the columns that we want to
    remove-column names not in stat options plus Player and Pos columns
    """
    headers = full_data[0]
    stat_options['Player'] = 'Player'
    desired_stats = stat_options.values()

    column_positions_to_be_removed = [
        i for i, item in enumerate(headers) if item not in desired_stats]

    return column_positions_to_be_removed


def remove_unused_columns(full_data):
    """
    Removes from full stat data columns that we dont really need.
    """

    column_indexes_to_be_removed = get_stat_columns_to_be_removed(full_data)
    for ind, row in enumerate(full_data):
        full_data[ind] = delete(row, column_indexes_to_be_removed).tolist()

    return full_data


def calculate_data_stat_column_number(
        filtered_data,
        stat_option_number):
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
        if str == "":
            return 0.0

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
    x = PrettyTable()
    x.field_names = list[0]
    x.add_rows(list[1:])
    # df = pd.DataFrame(list)
    # print(tabulate(df, headers='firstrow', tablefmt='psql'))
    print(x)


def main():
    """
    Here is the main function
    """
    print_introduction()
    get_user_name()
    while True:
        player_stat = get_player_stat_option()
        stat_str = stat_options[player_stat]
        top_bottom_option = get_top_bottom_players_option(stat_str)
        from_top = top_bottom_option == "1"
        player_number_option = get_number_of_players(stat_str, from_top)

        data = player_total_stats.get_all_values()
        filtered_data = remove_unused_columns(data)
        filtered_data = convert_list_data_from_string_to_numbers(filtered_data)
        col_num = calculate_data_stat_column_number(filtered_data, player_stat)
        result = sort_list_by_stat_option(
            filtered_data, col_num, from_top, int(player_number_option))
        print(col_num, filtered_data[0])
        pretty_print(result)
        get_user_wants_to_continue()
        clear_screen()


main()
