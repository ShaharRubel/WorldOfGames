import random
from time import sleep

def generate_sequence(difficulty):
    target_numbers = random.sample(range(1, 102), difficulty)
    # print(target_numbers)
    return target_numbers

def get_list_from_user(difficulty):
    print(f"Please enter {difficulty} numbers in the following format: 5,2,1,4,2\n")
    user_input = input()
    user_numbers = list(map(int,user_input.split(",")))# split to list, map to turn into int map, list to turn into list
    return user_numbers

def is_list_equal(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for item1,item2 in zip(arr1,arr2):
        if item1 != item2:
            return False
    return True

def play(difficulty):
    target_nums = generate_sequence(difficulty)
    print("Get Ready")
    sleep(3)
    print(target_nums)
    sleep(0.7)
    print("\n"* 20)
    user_nums = get_list_from_user(difficulty)

    if is_list_equal(target_nums,user_nums):
        return True  # user won
    else:
        return False

if __name__ == "__main__":

    print(play(3))