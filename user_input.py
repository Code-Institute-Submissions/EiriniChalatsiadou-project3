"""
Module user_input provides functionality regarding user input and
user validation.
"""
import os


def clear_screen():
    """
    Clear screen
    """
    os.system('clear')


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
    Validate player_stat to be an integer number between 0-7
    Raises ValueError if not integer or if not in this range.
    Also prints the error.
    """
    try:
        player_int_option = int(option)
        if (player_int_option < 0 or player_int_option > 7):
            raise ValueError()
        if player_int_option == 0:
            print("Thank you for using our program! Bye!!")
            exit()
    except ValueError:
        return False

    return True


def validate_top_bottom_option(option_string):
    """
     Validate top_bottom_option to be an integer number between 0-2
     Raises ValueError if not integer or if not in this range.
     Also prints the error.
    """
    try:
        top_bottom_option = int(option_string)
        if (top_bottom_option < 0 or top_bottom_option > 2):
            raise ValueError()
        if top_bottom_option == 0:
            print("Thank you for using our program! Bye!!")
            exit()
    except ValueError:
        return False

    return True


def validate_number_of_players(option_string):
    """
     Validate number_of_players to be an integer number between 0-200
     Raises ValueError if not integer or if not in this range.
     Also prints the error.
    """
    try:
        top_bottom_option = int(option_string)
        if (top_bottom_option < 0 or top_bottom_option > 200):
            raise ValueError()
        if top_bottom_option == 0:
            print("Thank you for using our program! Bye!!")
            exit()
    except ValueError:
        return False

    return True


def get_user_name():
    """
    This is the function that gets the name from the user
    """
    while True:
        username = input("Please enter your name: ")
        if validate_username(username):
            clear_screen()
            print(
                "Wow! This is a great name! " +
                f"Welcome {username.upper()}!!!!!\n")
            return username
        clear_screen()
        print("Invalid data. Please input a valid name\n")


def get_player_stat_option():
    """
    This is the function with the players stats options
    """
    while True:
        print('What do you want to know about? Please, choose an option 0-7')
        print('1) Points\n')
        print('2) Steals\n')
        print('3) Blocks\n')
        print('4) Rebounds\n')
        print('5) FT%\n')
        print('6) 2PT%\n')
        print('7) 3PT%\n')
        print('0) Quit\n')
        player_stat = input('Please, enter your option (a number 0-7): ')
        if validate_player_stat_option(player_stat):
            clear_screen()
            return player_stat
        clear_screen()
        print("Invalid data. Please input a correct option integer [1-8]\n")


def get_top_bottom_players_option(stat):
    """
    This is the function that you can choose between top or bottom players
    """
    while True:
        print(
            f'Regarding {stat}, do you want players from TOP or BOTTOM?')
        print('1) Top (best players)\n')
        print('2) Bottom (least best players)\n')
        print('0) Quit\n')
        top_bottom_option = input('Please, enter your option (a number 0-2): ')
        if validate_top_bottom_option(top_bottom_option):
            clear_screen()
            return top_bottom_option

        clear_screen()
        print("Invalid data. Please input a correct option integer [0-2]\n")


def get_number_of_players(stat, from_top):
    """
    This is the function that will get number of players from user
    """
    best_str = "" if from_top else "least "
    while True:
        print(
            'Please provide a number N. ' +
            f'This number will show the Nth {best_str}best players ' +
            f'regarding {stat}.\n')

        player_number_option = input(
            'Please, enter a number in range of [1-200] ' +
            'or press 0 to Quit: ')
        if validate_number_of_players(player_number_option):
            return player_number_option
        clear_screen()
        print("Invalid data. " +
              "Please input a correct option integer [0-200]\n")
