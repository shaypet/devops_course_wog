import random
from currency_converter import CurrencyConverter


def get_exchange_rate():
    client = CurrencyConverter()
    response = client.convert(1, 'USD', 'ILS')
    return response


def get_money_interval(difficulty_level, amount_to_exchange):
    rate = get_exchange_rate()
    if rate is None:
        return None
    interval = 10 - difficulty_level
    amount_exchanged_value = rate*amount_to_exchange
    return {
        "min": amount_exchanged_value-interval,
        "max": amount_exchanged_value+interval
    }


def get_guess_from_user(amount_to_exchange):
    while True:
        user_str_number = input(f"guess the exchanged value of {amount_to_exchange}$ (USD) to ILS:")
        if user_str_number.count(".") < 2 and user_str_number.replace(".", "").isdigit():  # check for float value
            break
        print("wrong input, a numbers only (can be a fraction")
    return float(user_str_number)
    pass


def compare_results(interval, user_guess):
    return interval["min"] <= user_guess <= interval["max"]


def play(difficulty_level):
    amount_to_exchange = random.randint(1, 100)
    
    interval = get_money_interval(difficulty_level, amount_to_exchange)
    if interval is None:
        return None

    user_guess = get_guess_from_user(amount_to_exchange)
    result = compare_results(interval, user_guess)
    if result:
        print("Greate job! You guessed right!")
    else:
        print("You were wrong :(")

    print(f'\nthe guess range was {interval["min"]} to {interval["max"]}')

    return result
