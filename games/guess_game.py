import random


def generate_number(difficulty):
    random_number = random.randint(0, difficulty)
    print("Random number has been selected.")
    return random_number


def get_guess_from_user(difficulty):
    while True:
        user_str_number = input(f"guess a number between 0 and {difficulty}:")
        if user_str_number.isdecimal():
            break
        print("wrong input, numbers only")
    return int(user_str_number)


def compare_results(random_number, user_number):
    return random_number == user_number


def play(difficulty):
    random_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    if compare_results(random_number, user_number):
        print(f"You did it! You guessed right, the number was {random_number}")
        return True
    print(f"Wrong number, better luck next time. The number was {random_number}")
    return False
