from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def go_to_videos_tab(driver):
    time.sleep(2)
    try:
        videos_tab = driver.find_elements(
            By.XPATH, 
            '//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[2]'
            )
        if videos_tab:
            videos_tab[-1].click()
    except Exception as e:
        print(f"An error occurred while switching to videos tab: {e}")

def get_latest_videos(driver, count=1):
    # Returns a list of the first `count` video elements on the channel.
    time.sleep(2)
    videos = driver.find_elements(By.CSS_SELECTOR, '#contents > ytd-rich-item-renderer')
    return videos[:count]

def reject_cookies(driver):
    try:
        btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'ytd-button-renderer.style-scope:nth-of-type(2) button')
                )
            )
        btn.click()
        print("Cookies rejected.")
        time.sleep(2)
        return
    except Exception as e:
        print(f"An error occurred while rejecting the cookies: {e}")