import random
import requests

def get_money_interval(difficulty):
    USD = random.randrange(1,100)
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
    except Exception as e:
        print("Url is not reachable, quitting program")
        exit()
    target = USD * data['rates']['ILS']
    lower_interval = target - (5 - difficulty)
    upper_interval = target + (5 - difficulty)
    print(lower_interval)
    print(upper_interval)
    return lower_interval, upper_interval , USD

def get_guess_from_user():
    try:
        user_guess = float(input("Please guess the value in ILS: "))
        return user_guess
    except ValueError:
        print("invalid entry, Quitting program")
        exit()

def play(difficulty):
    lower_int, upper_int, USD = get_money_interval(difficulty)
    print(f"The value selected is {USD} USD")
    user_input = get_guess_from_user()
    if lower_int < user_input < upper_int:
        return True
    else:
        return False

if __name__ == "__main__":
    print(play(1))