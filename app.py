from games import memory_game, currency_roulette_game, guess_game
from score import add_score
from utils import calculate_points
# READ ME
# this version of app.py (with 'games'- list of dictionaries) was ready to send at the last submission.
# I didn't send it because I wasn't sure how part 2 requirements will fit to it.
# it's more dynamic, you can easily switch the games order and add games to the project.


def welcome():
    username = input("type in your username:")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    games = [
        {
            "menu_text": "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
            "play": memory_game.play
        },
        {
            "menu_text": "Guess Game - guess a number and see if you chose like the computer.",
            "play": guess_game.play
        },
        {
            "menu_text": "Currency Roulette - try and guess the value of a random amount of USD in ILS",
            "play": currency_roulette_game.play
        }
    ]
    while True:
        print("Please choose a game to play:")
        for index, game in enumerate(games):
            print(f"\t{index+1}. {game["menu_text"]}")
        game_chosen = input()

        if game_chosen.isdecimal() and 1 <= int(game_chosen) <= len(games):
            break
    game_chosen = int(game_chosen)

    while True:
        difficulty_level = input("select a difficulty level between 1 and 5:")
        if difficulty_level.isdecimal() and 1 <= int(difficulty_level) <= 5:
            break
    difficulty_level = int(difficulty_level)

    result = games[game_chosen - 1]["play"](difficulty_level)
    if result:
        add_score(calculate_points(difficulty_level))
