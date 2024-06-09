import random
import freecurrencyapi

FREE_CURRENCY_API_KEY = 'fca_live_Q50KqRg85aZyrrlqy50n1Jf39FEjNkSqqs4ftc3c'  # bad practice.
CURRENCY_TO_EXCHANGE = 'ILS'


def get_exchange_rate():
    client = freecurrencyapi.Client(FREE_CURRENCY_API_KEY)
    response = client.latest(currencies=[CURRENCY_TO_EXCHANGE])
    return response["data"][CURRENCY_TO_EXCHANGE]


def get_money_interval(difficulty_level, amount_to_exchange):
    rate = get_exchange_rate()
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
    try:
        # get_money_interval function use get_exchange_rate that use the api.
        # without internet connection it would fail. so we try.
        interval = get_money_interval(difficulty_level, amount_to_exchange)
    except:
        print("we are very sorry. seems like there was a problem getting the exchange rate.")
        return None

    user_guess = get_guess_from_user(amount_to_exchange)
    result = compare_results(interval, user_guess)
    if result:
        print("Greate job! You guessed right!")
    else:
        print("You were wrong :(")

    print(f"\nthe guess range was {interval["min"]} to {interval["max"]}")

    return result
