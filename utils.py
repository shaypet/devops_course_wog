# CREDIT
# https://www.geeksforgeeks.org/clear-screen-python/

# import only system from os
from os import system, name


# define our clear function
def Screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



DATA_FILES_DIR = "saved_data_files"
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 403

def get_score():
    file_path = f'{DATA_FILES_DIR}/{SCORES_FILE_NAME}'
    try:
        file = open(file_path, "r")
        current_score = file.readline()
        file.close()
        if current_score.isdecimal():
            return int(current_score)
    except:
        return None
    return None

def calculate_points(difficulty_level):
    return difficulty_level*3 + 5