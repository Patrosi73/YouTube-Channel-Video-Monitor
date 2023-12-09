import os
import json
keys_json = 'keys.json'
with open(keys_json) as keys_data:
    keys = json.load(keys_data)

api_key = keys['youtube_api_key']
channel_id = keys["channel_id"]
discord_webhook = keys["discord_webhook"]
if not (discord_webhook):
    print("discord webhook not found! please place it inside keys.json")
    quit()



