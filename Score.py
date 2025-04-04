import Utils as utils

def add_score(difficulty):
    # try to read file if exist and save current score to variable
    try:
        with open(utils.SCORES_FILE_NAME, 'r') as file:
            print("file found")
            current_score = int(file.read())
    # file doesn't exist - create one and append 0 as score
    except:
        with open(utils.SCORES_FILE_NAME, 'a') as file:
            print("file doesn't exist, creating one")
            file.write("0")
            current_score = 0

    # add current score and write it to file
    with open(utils.SCORES_FILE_NAME, 'r+') as file:
        score = (difficulty * 3) + 5 + current_score
        file.write(str(score))

if __name__ == "__main__":
    add_score(3)