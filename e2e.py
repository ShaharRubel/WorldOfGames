import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys


def test_scores_service(URL):
    # define driver
    driver = webdriver.Chrome()
    # get URL
    driver.get("http://127.0.0.1:8777")
    # Get score from response
    score = int(driver.find_element(By.ID, "score").text)
    # if between 1 and 1000 return true
    if 1 < score < 1000:
        return True
    # not between 1 and 1000 return false
    else:
        return False


def main_function():
    # if test_score_service returns True
    if test_scores_service("http://127.0.0.1:5000"):
        print("exit normally")
        sys.exit(0)
    # if test_score_service returns False exit with error
    else:
        print("exit with error")
        sys.exit(-1)


if __name__ == "__main__":
    main_function()