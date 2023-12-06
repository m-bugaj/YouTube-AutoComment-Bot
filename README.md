# 🔴 YouTube Auto Comment Bot

<p align="center">
  <img src="ytlogo.png" alt="Logo" width="150">
</p>

## Overview

YouTube Auto Comment Bot is a Python script utilizing Selenium to automate leaving comments on YouTube videos. It allows users to leave comments with customizable content on multiple channels.

## 🌟 Features

- **Channel Commenting**: The bot can automatically leave comments on videos of specified YouTube channels.
- **Customizable Comments**: Users can provide a list of comments, and the bot will randomly select and post them.
- **Cookie Management**: Utilizes cookies for YouTube login, allowing automated commenting without manual login each time.
- **Multiple Channel Support**: Supports commenting on multiple YouTube channels.

## ❗ Important info ❗

1) The bot is configured to select the latest video from the channel's video section and comment on it. This is especially useful for "type beat" music producers who want to leave comments on other producers' channels while waiting for feedback on their videos.
2) Bot is created for educational purposes and should be used responsibly. The author disclaims any responsibility for the consequences that may arise if the bot is misused, such as receiving a ban from Google on YouTube.

## 💻 Usage

1. Ensure you have Python installed on your machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a `channel_urls.txt` file with YouTube channel URLs.
4. Prepare a list of comments in a `comments.txt` file.
5. Run the script using `python app.py`.
6. Manually log in to your Google account when prompted on the browser window.
7. The bot will start leaving comments on the specified YouTube channels.
