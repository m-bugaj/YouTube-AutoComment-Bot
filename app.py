import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import os
import random
import sys

def is_cookies_empty(filename="cookies.pkl"):
    # Check if the cookies file is empty
    return not os.path.exists(filename) or os.path.getsize(filename) == 0

def leave_a_comment(channel_url, comments):
    # Wait a moment to allow the page to load
    time.sleep(2)

    # Go to the channel
    driver.get(channel_url)

    time.sleep(2)

    # Go to the videos section
    try:
        videos_tab = driver.find_elements(By.XPATH, '//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[2]')
        if videos_tab:
            videos_tab[-1].click()
    except Exception as e:
        print(f"An error occurred while switching to videos tab: {e}")

    time.sleep(2)

    # Go to the first video
    try:
        element = driver.find_element(By.CSS_SELECTOR, '#contents > ytd-rich-item-renderer:nth-child(1)')
        element.click()
    except Exception as e:
        return

    time.sleep(3)

    # Scroll slightly to load the commenting section
    driver.execute_script("window.scrollBy(0, 500);")

    # Delay to load the comments section
    time.sleep(4)

    # Sprawdź, czy mój komentarz już jest
    if is_my_comment_on_top(driver, my_handle="@BUGIBEATZ"):
        print("Komentarz już istnieje – pomijam to wideo.")
        return

    # Click on the comment input box
    comment_input_box = driver.find_elements(By.XPATH, '//*[@id="placeholder-area"]')
    comment_input_box[-1].click()

    time.sleep(1)

    # Type a comment
    comment_text = get_random_comment(yt_comments)
    comment_input = driver.find_elements(By.XPATH, '//*[@id="contenteditable-root"] ')
    driver.execute_script('''
    var commentInput = arguments[0];
    commentInput.innerText = '{}';
'''.format(comment_text), comment_input[-1])
    comment_input[-1].send_keys('.')
    comment_input[-1].send_keys(Keys.BACKSPACE)

    time.sleep(1)

    # Publish the comment
    wait = WebDriverWait(driver, 10)
    comment_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-button"]//button'))
    )
    comment_button.click()
    # comment_button = driver.find_elements(By.XPATH, '//*[@id="submit-button"]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
    # comment_button[-1].click()

def is_my_comment_on_top(driver, my_handle="@BUGIBEATZ", max_comments_to_check=2):
    """
    Sprawdza pierwsze 1–2 komentarze na stronie.
    Zwraca True, jeśli autor któregokolwiek to my_handle (np. '@BUGIBEATZ').
    """
    try:
        # poczekaj, aż pojawi się sekcja komentarzy
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comment-thread-renderer"))
        )

        # pobierz pierwsze kilka wątków komentarzy
        comment_threads = driver.find_elements(By.CSS_SELECTOR, "ytd-comment-thread-renderer")[:max_comments_to_check]

        for thread in comment_threads:
            try:
                # znajdź element z nazwą autora
                author_el = thread.find_element(By.CSS_SELECTOR, "#author-text span")
                author_name = author_el.text.strip()

                # porównanie z handlem
                if author_name.lower().replace("@", "") == my_handle.lower().replace("@", ""):
                    print(f"Znaleziono mój komentarz: {author_name}")
                    return True
            except Exception:
                continue

    except Exception as e:
        print(f"Błąd przy sprawdzaniu komentarzy: {e}")

    return False

def get_random_comment(comments):
    return random.choice(comments)

def check_cookies(driver):
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


if __name__ == "__main__":
    # Initialize the browser with undetected_chromedriver
    driver = uc.Chrome()

    check_cookies(driver)

    channel_url_counter = 0
    yt_channels = []
    with open("channel_urls.txt", 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            yt_channels.append(cleaned_line)

    yt_comments = []
    with open("comments.txt", 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_line = line.strip()
            yt_comments.append(cleaned_line)
        
    for channel_url in yt_channels:
        try:
            leave_a_comment(channel_url, yt_comments)
            channel_url_counter += 1
        except Exception as e:
            print(f"Błąd podczas komentowania kanału {channel_url}: {e}")
        

    if channel_url_counter == len(yt_channels):
        print("SUCCESS")
    else:
        print(f"Zostawiono {channel_url_counter} / {len(yt_channels)} komentarzy!")

    # Wait a moment for the window to close
    time.sleep(5)

    driver.close()