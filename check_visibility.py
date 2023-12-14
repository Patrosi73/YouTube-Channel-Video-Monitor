import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

with open('differences.json', 'r') as file:
    video_list = json.load(file)

private_video = ["Private video"]
deleted_video = ["This video has been removed by the uploader", "This video isn't available anymore"]
unlisted_video = ["Unlisted"]
tosd_video = ["This video has been removed for violating YouTube's Terms of Service"]
copyrighted_video = ["This video contains content from", "Video unavailable"]

browser = webdriver.Firefox()
try:
    for video in video_list:
        videoId = video.get('videoId', '')
        title = video.get('title', '')
        url = f"https://www.youtube.com/watch?v={videoId}"
        browser.get(url)
        wait = WebDriverWait(browser, 1)

        status = "public"
        for phrase in private_video:
            try:
                element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
                status = "private"
                break
            except TimeoutException:
                pass
        for phrase in deleted_video:
            try:
                element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
                status = "deleted"
                break
            except TimeoutException:
                pass
        for phrase in unlisted_video:
            try:
                element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
                status = "unlisted"
                break
            except TimeoutException:
                pass
        for phrase in tosd_video:
            try:
                element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
                status = "deleted"
                break
            except TimeoutException:
                pass
        for phrase in copyrighted_video:
            try:
                element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
                status = "deleted"
                break
            except TimeoutException:
                pass
        
        result = {"videoId": videoId, "title": title, "status": status}
        with open('visibility.json', 'a') as result_file:
            json.dump(result, result_file, indent=2)
            result_file.write(',\n')
        
        

finally:
    browser.quit()
