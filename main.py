import os
import json
from get_youtube_video_list import get_video_list
keys_json = 'keys.json'
with open(keys_json) as keys_data:
    keys = json.load(keys_data)

api_key = keys['youtube_api_key']
channel_id = keys["channel_id"]
discord_webhook = keys["discord_webhook"]

video_list = "video_list.json"

if not (discord_webhook):
    print("discord webhook not found! please place it inside keys.json")
    quit()
if not api_key:
    print("api key not found! please place it inside keys.json")
    quit()
if not channel_id:
    print("channel id not found! please place it inside keys.json")
    quit()
get_video_list(channel_id, api_key, video_list)



