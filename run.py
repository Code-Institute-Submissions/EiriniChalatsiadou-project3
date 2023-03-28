import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("nba_stats_2022")

player_total_stats = SHEET.worksheet("Player_Totals")


def get_user_name():
    """
    Thgis isdfdsfdsf
    """
    print('Welcome to nba .... \n')
    print('This is a great application ....\n')
    name_str = input("Please enter your name: ")
    print(f"Wow! This is a nice name! Welcome {name_str.upper()}!!!!!\n")


data = player_total_stats.get_all_values()
get_user_name()
# print(data)



  
