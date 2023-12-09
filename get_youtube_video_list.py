import os
import google.auth
from googleapiclient.discovery import build
import json
keys_json = 'keys.json'
with open(keys_json) as keys_data:
    keys = json.load(keys_data)

api_key = keys['youtube_api_key']
channel_id = keys["channel_id"]

if not api_key:
    raise ValueError("api key not found! please place it inside keys.json")
if not channel_id:
    raise ValueError("channel id not found! please place it inside keys.json")



