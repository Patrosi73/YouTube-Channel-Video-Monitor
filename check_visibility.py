import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
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

total_results = []

try:
    for video in video_list:
        videoId = video.get('videoId', '')
        title = video.get('title', '')
        publishedAt = video.get('publishedAt', '')
        url = f"https://www.youtube.com/watch?v={videoId}"
        browser.get(url)
        wait = WebDriverWait(browser, 1)
        print(f"checking visibility of video ID {videoId}")
        status = "public"
        for phrase in private_video:
            try:
                element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
                status = "privated"
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
                status = "tosd"
                break
            except TimeoutException:
                pass
        for phrase in copyrighted_video:
            try:
                element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
                status = "copyrighted"
                break
            except TimeoutException:
                pass
        result = {"videoId": videoId, "title": title, "status": status, "publishedAt": publishedAt}
        total_results.append(result)
finally:
    browser.quit()

with open('video_visibility.json', 'w') as result_file:
    json.dump(total_results, result_file, indent=2)
print("visibility written to video_visibility.json")
