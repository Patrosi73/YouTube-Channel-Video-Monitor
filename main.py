import os
import json

from get_youtube_video_list import get_video_list
keys_json = 'keys.json'

if not os.path.exists("keys.json"):
    keys_json_file = """
{
    "youtube_api_key" : "",
    "discord_webhook" : "",
    "channel_id" : "",
    "userid_to_ping" : ""
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

video_list = "video_list.json"

video_list_check = "video_list_check.json"


print("checking keys.json")
if not discord_webhook:
    print("discord webhook not found! please place it inside keys.json")
    quit()
if not api_key:
    print("api key not found! please place it inside keys.json")
    quit()
if not channel_id:
    print("channel id not found! please place it inside keys.json")
    quit()
if not userid_to_ping:
    print("discord user id to ping now found! please place it inside keys.json")
    quit()

print("checking for video_list.json")
if not os.path.exists("video_list.json"):
    print("first video_list.json not found, downloading now - this should only run once")
    get_video_list(channel_id, api_key, video_list)

print("all checks passed, starting now")
if os.path.exists("video_list.json"):
    print("downloading video_list_check.json:")
    get_video_list(channel_id, api_key, video_list_check)