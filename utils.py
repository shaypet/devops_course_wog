# CREDIT
# https://www.geeksforgeeks.org/clear-screen-python/

# import only system from os
from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 403
