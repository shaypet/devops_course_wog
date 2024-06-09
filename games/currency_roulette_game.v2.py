import random

import freecurrencyapi

FREE_CURRENCY_API_KEY = 'fca_live_Q50KqRg85aZyrrlqy50n1Jf39FEjNkSqqs4ftc3c'
CURRENCY_TO_EXCHANGE = 'ILS'

# I took some creative freedom. and changed the nature of some functions. hope it's OK.
# I.E: I wanted to show the user all the information in the end.


def get_exchange_rate():
    client = freecurrencyapi.Client(FREE_CURRENCY_API_KEY)
    response = client.latest(currencies=[CURRENCY_TO_EXCHANGE])
    return response["data"][CURRENCY_TO_EXCHANGE]


def get_money_interval(difficulty_level):
    return 10 - difficulty_level


def get_exchanged_value(rate, amount_to_exchange):
    return rate*amount_to_exchange


def get_guess_from_user(amount_to_exchange):
    while True:
        user_str_number = input(f"guess the exchanged value of {amount_to_exchange}$ (USD) to ILS:")
        if user_str_number.count(".") < 2 and user_str_number.replace(".", "").isdigit():  # check for float value
            break
        print("wrong input, a numbers only (can be a fraction")
    return float(user_str_number)
    pass


def compare_results(exchanged_value, interval, user_guess):
    return abs(exchanged_value - user_guess) <= interval


def play(difficulty_level):
    try:
        rate = get_exchange_rate()
    except:
        print("we are very sorry. seems like there was a problem getting the exchange rate.")
        return False

    amount_to_exchange = random.randint(1, 100)
    interval = get_money_interval(difficulty_level)
    exchanged_value = get_exchanged_value(amount_to_exchange, rate)
    user_guess = get_guess_from_user(amount_to_exchange)
    return_result = compare_results(exchanged_value, interval, user_guess)
    if return_result:
        print("Greate job! you guessed right!")
    else:
        print("you were wrong :(")

    print(f"""
the exchange value was {exchanged_value} ILS (rate was {rate}).
the guess range was {exchanged_value+interval} to {exchanged_value-interval}""")

    return return_result
