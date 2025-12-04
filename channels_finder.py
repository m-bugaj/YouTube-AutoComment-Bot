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
from utils.youtube_navigation import go_to_videos_tab, get_latest_videos, reject_cookies
from utils.common_navigation import scroll_to_bottom

class ChannelsFinder:
    def __init__(self):
        self.driver = uc.Chrome()

    def save_new_channel_urls(new_channel_urls):
        return
    
    def get_commentators_channels(self):
        authors = self.driver.find_elements(By.CSS_SELECTOR, "a#author-text")
        urls = []

        for a in authors:
            try:
                href = a.get_attribute("href")
                if href and "/@" in href or "/channel/" in href:
                    urls.append(href)
            except:
                continue

        urls = list(set(urls))
        return urls
    
    def save_urls_to_file(file_path, new_urls):
        if not os.path.exists(file_path):
            print(f"[INFO] File '{file_path}' not found. Creating new file...")
            open(file_path, "w", encoding="utf-8").close()
            existing_urls = set()
        else:
            with open(file_path, "r", encoding="utf-8") as f:
                existing_urls = set(line.strip() for line in f.readlines())

        existing_urls.update(new_urls)

        with open(file_path, "w", encoding="utf-8") as f:
            for url in sorted(existing_urls):
                f.write(url + "\n")

        print(f"[INFO] Saved {len(new_urls)} URLs (deduplicated total: {len(existing_urls)}).")

    def find_comentators_for_channel(self, channel_url, videos_count_to_handle=1):
        time.sleep(2)

        # Go to the channel
        self.driver.get(channel_url)

        go_to_videos_tab(self.driver)
        videos = get_latest_videos(self.driver, videos_count_to_handle)
        for video in videos:
            video.click()
            time.sleep(5)
            scroll_to_bottom(self.driver)
            urls = self.get_commentators_channels()
            print(urls)
            self.driver.back()

        time.sleep(5)



        return

    def run(self):
        videos_count_to_handle = 2
        yt_channels = []
        with open("channel_urls.txt", 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                yt_channels.append(cleaned_line)

        self.driver.get('https://www.youtube.com/')
        reject_cookies(self.driver)

        for channel_url in yt_channels:
            self.find_comentators_for_channel(channel_url, videos_count_to_handle)
