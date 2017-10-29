#!/usr/bin/env python

import time
import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = 'https://dragonbound.net/'
username = 'username here'
password = 'password here'
page_timeout = 10


chrome_options = Options()
chrome_options.add_argument('--kiosk')
driver = webdriver.Chrome(chrome_options=chrome_options)


def init():
    driver.get(url)


def random_delay():
    return random.random() + 0.1


def wait_for_login_form():
    time.sleep(5)
    element_present = EC.presence_of_element_located((By.ID, 'LoginPass'))
    WebDriverWait(driver, page_timeout).until(element_present)


def login():
    user_div = driver.find_element_by_id('LoginUsername')

    time.sleep(random_delay())
    user_div.click()

    time.sleep(random_delay())

    for letter in username:
        time.sleep(random_delay())
        user_div.send_keys(letter)

    password_div = driver.find_element_by_id('LoginPass')

    time.sleep(random_delay())
    password_div.click()

    time.sleep(random_delay())

    for letter in password:
        time.sleep(random_delay())
        password_div.send_keys(letter)

    time.sleep(random_delay())
    driver.find_element_by_id('LoginSubmit').click()


def wait_for_server():
    time.sleep(5)
    element_present = EC.presence_of_element_located((By.ID, 'BrokerChannel2'))
    WebDriverWait(driver, page_timeout).until(element_present)


def pick_server():
    time.sleep(random_delay())
    driver.find_element_by_id('BrokerChannel2').click()  # Beginner Server


def wait_for_event_button():
    time.sleep(5)
    element_present = EC.presence_of_element_located((By.ID, 'event_button'))
    WebDriverWait(driver, page_timeout).until(element_present)


def click_event_button():
    time.sleep(random_delay())
    driver.find_element_by_id('event_button').click()


if __name__ == '__main__':
    init()

    wait_for_login_form()
    login()

    wait_for_server()
    pick_server()

    wait_for_event_button()
    click_event_button()

    # driver.quit()
