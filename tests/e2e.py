import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import FLASK_PORT
#from selenium.webdriver.chrome.options import Options


def test_scores_service():
    driver = webdriver.Chrome()
    driver.get(f'http://localhost:{FLASK_PORT}')

    error_check = driver.find_element(by=By.XPATH, value="/html/body/h1")
    if error_check.text == "ERROR:":
        return False
    score_box = driver.find_element(by=By.ID, value="score")
    score_value = score_box.text
    if score_value.isdecimal() and 1 <= int(score_value) <= 1000:
        return True
    return False

def main_function():
    if test_scores_service():
        sys.exit(0)
    else:
        sys.exit(-1)

main_function()