import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        wait = WebDriverWait(browser, 10)

        phrase_found = False
        for phrase in private_video:
            status = "private"
            element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
            result = {"videoId" : videoId, "title": title, "status" : status}
            with open('result.json', 'a') as result_file:
                json.dump(result, result_file, indent=2)
                result_file.write('\n')
            phrase_found = True
            break
        for phrase in deleted_video:
            status = "deleted"
            element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
            result = {"videoId" : videoId, "title": title, "status" : status}
            with open('result.json', 'a') as result_file:
                json.dump(result, result_file, indent=2)
                result_file.write('\n')
            phrase_found = True
            break
        for phrase in unlisted_video:
            status = "unlisted"
            element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
            result = {"videoId" : videoId, "title": title, "status" : status}
            with open('result.json', 'a') as result_file:
                json.dump(result, result_file, indent=2)
                result_file.write('\n')
            phrase_found = True
            break
        for phrase in tosd_video:
            status = "tosd"
            element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
            result = {"videoId" : videoId, "title": title, "status" : status}
            with open('result.json', 'a') as result_file:
                json.dump(result, result_file, indent=2)
                result_file.write('\n')
            phrase_found = True
            break
        for phrase in copyrighted_video:
            status = "copyrighted"
            element = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), phrase))
            result = {"videoId" : videoId, "title": title, "status" : status}
            with open('result.json', 'a') as result_file:
                json.dump(result, result_file, indent=2)
                result_file.write('\n')
            phrase_found = True
            break
        
        

finally:
    browser.quit()
