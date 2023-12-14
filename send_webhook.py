import json
import requests
import time
from datetime import datetime
keys_json = "keys.json"
copyrighted = "webhooks/webhook_videocopyrighted.txt"
deleted = "webhooks/webhook_videodeleted.txt"
private = "webhooks/webhook_videoprivated.txt"
public = "webhooks/webhook_videopublic.txt"
tosd = "webhooks/webhook_tosd.txt"
unlisted = "webhooks/webhook_videounlisted.txt"
with open(keys_json) as keys_data:
    keys = json.load(keys_data)


discord_webhook = keys["discord_webhook"]
userid = keys["userid_to_ping"]

with open('video_visibility.json', 'r') as file:
    video_list = json.load(file)

def load_webhook_content(filename):
    with open(filename, 'r') as file:
        return json.load(file)
def replace_placeholders(template, replacements):
    for key, value in replacements.items():
        template = template.replace(f'{{{key}}}', str(value))
    return template


for video in video_list:
    video_id_compare = video.get("videoId", '')
    title = video.get("title", '')
    visibility = video.get("status", '')
    publishedAt = video.get("publishedAt", '')

    time_str = publishedAt
    dt_object = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
    unixtime = int(dt_object.timestamp())
    video_time = f"<t:{unixtime}:F>"

    webhook_content = load_webhook_content(f'webhooks/webhook_video{visibility.lower()}.txt')
    replacements = {
        'userid': userid,
        'title': title,
        'video_id_compare': video_id_compare,
        'video_time': video_time
    }
    webhook_content = replace_placeholders(json.dumps(webhook_content), replacements)
    requests.post(discord_webhook, json = json.loads(webhook_content))
    time.sleep(5)