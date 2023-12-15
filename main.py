import os
import json
import time
from check_jsons import find_json_differences
from get_youtube_video_list import get_video_list
keys_json = 'keys.json'

if not os.path.exists("keys.json"):
    keys_json_file = """
{
    "youtube_api_key" : "",
    "discord_webhook" : "",
    "channel_id" : "",
    "userid_to_ping" : ""
    "sleep_time_after_finish" : 900
}
"""
    with open("keys.json", "w") as file1:
        file1.write(keys_json_file)
    print("keys.json created. place the required stuff there")
    quit()

with open(keys_json) as keys_data:
    keys = json.load(keys_data)

api_key = keys['youtube_api_key']
channel_id = keys["channel_id"]
discord_webhook = keys["discord_webhook"]
userid_to_ping = keys["userid_to_ping"]
sleep_time_after_finish = keys["sleep_time_after_finish"]

video_list = "video_list.json"

video_list_check = "video_list_check.json"

print("checking for video_list.json")
if not os.path.exists("video_list.json"):
    print("first video_list.json not found, downloading now - this should only run once")
    get_video_list(channel_id, api_key, video_list)

print("all checks passed, starting now")
while True:
    print("downloading video_list_check.json:")
    get_video_list(channel_id, api_key, video_list_check)
    print("now comparing with previous JSON")
    with open("video_list.json", "r") as f1:
        video_list = json.loads(f1.read())
    with open("video_list_check.json", "r") as f2:
        video_list_check = json.loads(f2.read())
    find_json_differences(video_list_check, video_list, "differences.json")
    print("now checking the video's visibility (will open a browser - if it errors out here make sure you put geckodriver.exe in PATH)")
    with open("check_visibility.py") as f:
        exec(f.read())
    print("sending webhook message(s)")
    with open("send_webhook.py") as f:
        exec(f.read())
    print("all done - deleting JSONs and renaming video_list_check.json to video_list.json")
    os.remove("video_visibility.json")
    os.remove("differences.json")
    os.remove("video_list.json")
    os.rename("video_list_check.json", "video_list.json")
    print(f"Restarting in {sleep_time_after_finish} seconds")
    time.sleep(sleep_time_after_finish)
