import random

def generate_number(difficulty):
    secret_number = random.randrange(0, 10*difficulty)
    return secret_number
def get_guess_from_user(difficulty):
    try:
        return int(input(f"Please enter a number between 1 to {10*difficulty}: "))
    except ValueError:
        print("Please enter a valid number!")
def compare_results(target,userInput):
    if target == userInput:
        return True
    else:
        return False
def play(difficulty):
    target = generate_number(difficulty)
    # print(target)
    userInput = get_guess_from_user(difficulty)
    if compare_results(target, userInput):
        return True
    else:
        return False

if __name__ == "__main__":
    print(play(3))
