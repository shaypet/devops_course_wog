import random
from time import sleep
from utils import Screen_cleaner


# Constants for sequence values
MIN_NUMBER_FOR_ITEM = 1
MAX_NUMBER_FOR_ITEM = 101

# delay time to clear the screen after showing the sequence, in seconds
DELAY_TO_CLEAR = 0.7

# UNWRITTEN FEATURE
# if you want to check the sequences are identical (equal by values *and by order*) set CHECK_IDENTICAL to True,
# otherwise set to False
CHECK_IDENTICAL = True


method_str = 'identical'if CHECK_IDENTICAL else 'equal'


def generate_sequence(difficulty_level):
    sequence = []
    for i in range(0, difficulty_level):
        sequence.append(random.randint(MIN_NUMBER_FOR_ITEM, MAX_NUMBER_FOR_ITEM))
    return sequence


def get_list_from_user(difficulty_level):
    while True:
        user_sequence = []
        user_str_sequence = input("type your sequence using comma between numbers:")
        user_str_sequence = user_str_sequence.split(",")
        if len(user_str_sequence) != difficulty_level:
            print("wrong number of items. try again")
            continue

        for item in user_str_sequence:
            if not item.strip().isdecimal():
                break
            user_sequence.append(int(item.strip()))

        if len(user_str_sequence) != len(user_sequence):
            print("all items must be numbers. try again")
            continue

        return user_sequence
    return []


def is_list_equal(list1, list2):
    if not CHECK_IDENTICAL:
        list1.sort()
        list2.sort()
    return list1 == list2


def play(difficulty_level):
    sequence = generate_sequence(difficulty_level)
    print("Random numbers have been selected.")
    print(*sequence, sep=", ")  # print a list without [] and with ', ' as seperator
    sleep(DELAY_TO_CLEAR)
    Screen_cleaner()
    user_sequence = get_list_from_user(difficulty_level)
    if is_list_equal(sequence, user_sequence):
        print(f"Your memory is very good, the sequences are {method_str}")
        return True
    print(f"You need to practice your memory, the sequence aren't {method_str}")
    return False
