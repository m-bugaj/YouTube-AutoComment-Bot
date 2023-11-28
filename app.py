import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle
import os
import random

def is_cookies_empty(filename="cookies.pkl"):
    # Check if the cookies file is empty
    return not os.path.exists(filename) or os.path.getsize(filename) == 0

# Initialize the browser with undetected_chromedriver
driver = uc.Chrome()

if is_cookies_empty():
    # Open the login page, user logs in manually
    driver.get("https://www.youtube.com/")
    input('Log in to your Google account and press Enter to continue...')
    
    # Save cookies to the file
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
else:
    # Load cookies if available
    driver.get("https://www.youtube.com/")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

# Wait a moment for the window to close
time.sleep(5)

driver.close()